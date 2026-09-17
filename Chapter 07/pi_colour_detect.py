import cv2
import numpy as np

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video stream. Check camera connection/setup.")
else:
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Define HSV color ranges
    color_ranges = {
        "blue": ([100, 50, 50], [130, 255, 255]),
        "green": ([40, 40, 40], [80, 255, 255]),
        "red_lower": ([0, 100, 100], [10, 255, 255]),
        "red_upper": ([170, 100, 100], [180, 255, 255]),
        "yellow": ([20, 100, 100], [30, 255, 255]),
    }

    # Choose target color
    target_color_name = "red"

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame, exiting...")
            break

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        if target_color_name == "red":
            lower_bound1 = np.array(color_ranges["red_lower"][0])
            upper_bound1 = np.array(color_ranges["red_lower"][1])
            lower_bound2 = np.array(color_ranges["red_upper"][0])
            upper_bound2 = np.array(color_ranges["red_upper"][1])
            mask1 = cv2.inRange(hsv, lower_bound1, upper_bound1)
            mask2 = cv2.inRange(hsv, lower_bound2, upper_bound2)
            mask = cv2.bitwise_or(mask1, mask2)
        else:
            lower_bound = np.array(color_ranges[target_color_name][0])
            upper_bound = np.array(color_ranges[target_color_name][1])
            mask = cv2.inRange(hsv, lower_bound, upper_bound)

        # Clean up the mask
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.erode(mask, kernel, iterations=1)
        mask = cv2.dilate(mask, kernel, iterations=1)

        # Find and draw contours
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            if cv2.contourArea(contour) > 500:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, target_color_name.capitalize(), (x, y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

        # Show results
        cv2.imshow("Color Detection", frame)
        cv2.imshow("Color Mask", mask)

        # Exit on 'q'
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Color object detection ended.")
