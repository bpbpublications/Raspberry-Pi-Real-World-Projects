import cv2

# Open default camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video stream. Ensure camera is connected.")
else:
    # Set resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame, exiting stream...")
            break

        cv2.imshow("Live Camera Feed", frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Video stream ended.")
