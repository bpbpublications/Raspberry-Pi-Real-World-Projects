import cv2
import time # For a short delay

def capture_and_save_photo(output_filename='pi_captured_photo.jpg'):
    """
    Captures a single photo from the default camera, displays it, and saves it.
    """
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera. Check connection, permissions, or if enabled in raspi-config.")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    time.sleep(3) # Gives camera time to adjust

    ret, frame = cap.read()

    cap.release()

    if not ret:
        print("Error: Failed to capture photo.")
        return

    cv2.imshow('Captured Photo from Pi', frame)
    cv2.waitKey(0)

    success = cv2.imwrite(output_filename, frame)

    if success:
        print(f"Photo saved successfully as {output_filename}")
    else:
        print(f"Error: Could not save photo to {output_filename}")

    cv2.destroyAllWindows()
    print("Windows closed.")

capture_and_save_photo()



