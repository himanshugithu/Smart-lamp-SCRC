import cv2
import time
from oneM2Mget import onem2m_get_request
from Speak import text_to_speech
from getLUX import calculate_luminance
from faceDistance import getDistance

# Initialize flag to track whether speech has been played
speech_played = False

cap = cv2.VideoCapture(1)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Calculate luminance from the captured frame
    luminance = calculate_luminance(frame)

    # Calculate distance from face to camera
    distance = getDistance(frame)
    print(distance)

    # Check if distance is valid (not None) and less than 40
    if distance is not None and distance < 40:
        # Check if speech has already been played for this detection
        if not speech_played:
            try:
                response_data = onem2m_get_request()
                con_value = response_data['m2m:cin']['con'].split(',')
                data = f"Welcome to Smart City Living Lab. The current value of CO2 is {con_value[1]}, temperature is {con_value[2]}, and humidity is {con_value[3]}."
                text_to_speech(data)
                print(response_data)
                # Set the flag to True to indicate that speech has been played
                speech_played = True
            except Exception as e:
                print(f"Error: {e}")
    else:
        # Reset the flag when no face is detected or face is too far
        speech_played = False

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
