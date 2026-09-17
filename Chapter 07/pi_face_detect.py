import cv2

# Load the pre-trained Haar Cascade classifier for face detection
# Make sure the XML file is in the same directory as your script
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Initialize the camera capture object
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video stream. Ensure camera is connected and enabled.")
    exit()

# Optional: Set resolution for better performance on the Pi
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame, exiting...")
        break

    # Convert the frame to grayscale for the face detection algorithm
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    # The detectMultiScale() function returns a list of rectangles (x, y, w, h)
    faces = face_cascade.detectMultiScale(
        gray_frame,
        scaleFactor=1.1, # How much the image size is reduced at each image scale
        minNeighbors=5,  # How many neighbors each candidate rectangle should have
        minSize=(30, 30) # Minimum possible object size
    )

    # Draw a rectangle around each detected face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the result
    cv2.imshow('Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and destroy all windows
cap.release()
cv2.destroyAllWindows()
print("Face detection stream ended.")
