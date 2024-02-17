import cv2

# Function to calculate luminance (brightness) from an image
def calculate_luminance(image):
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Calculate mean pixel intensity (luminance)
    luminance = gray_image.mean()
    return luminance

# Create a VideoCapture object to capture video from the default camera (index 0)
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Loop to continuously capture frames from the camera and calculate luminance
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if the frame is read correctly
    if not ret:
        print("Error: Could not read frame.")
        break

    # Calculate luminance from the frame
    luminance = calculate_luminance(frame)
    
    # Display the luminance value
    print("Luminance:", luminance, "lux")

    # Check for the 'q' key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
