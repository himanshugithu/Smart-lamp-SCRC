import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
KNOWN_DISTANCE = 60.0  # Assume the distance in centimeters (e.g., 60 cm)
KNOWN_FACE_WIDTH = 16.5  # Assume the average face width in centimeters (e.g., 16.5 cm)
FOCAL_LENGTH = 500.0  # Assume the focal length of the camera (e.g., 500 pixels)

def getDistance(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    if len(faces) == 1:
        (x, y, w, h) = faces[0]
        face_width_pixels = w
        distance = (KNOWN_FACE_WIDTH * FOCAL_LENGTH) / face_width_pixels       # Calculate distance
        return distance
    elif len(faces) == 0:
        print("No face detected")
    else:
        print("Multiple faces detected")

cap = cv2.VideoCapture(1)

if __name__ == "__main__":
    pass
