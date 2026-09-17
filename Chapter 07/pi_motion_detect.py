import cv2
import time

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video stream. Check camera connection/setup.")
else:
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Capture first frame
    ret, frame1 = cap.read()
    if not ret:
        print("Failed to grab initial frame.")
    else:
        gray_frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        gray_frame1 = cv2.GaussianBlur(gray_frame1, (21, 21), 0)

        while True:
            ret, frame2 = cap.read()
            if not ret:
                print("Failed to grab frame, exiting...")
                break

            gray_frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
            gray_frame2 = cv2.GaussianBlur(gray_frame2, (21, 21), 0)

            # Frame difference
            frame_diff = cv2.absdiff(gray_frame1, gray_frame2)

            # Threshold difference
            thresh = cv2.threshold(frame_diff, 25, 255, cv2.THRESH_BINARY)[1]
            thresh = cv2.dilate(thresh, None, iterations=2)

            # Contours
            contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                if cv2.contourArea(contour) < 500:
                    continue
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Show results
            cv2.imshow("Motion Detected", frame2)
            cv2.imshow("Thresholded Motion", thresh)

            # Update reference frame
            gray_frame1 = gray_frame2

            # Exit on 'q'
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    cap.release()
    cv2.destroyAllWindows()
    print("Motion detection ended.")
