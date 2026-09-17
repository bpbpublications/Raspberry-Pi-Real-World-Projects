import cv2
import numpy as np

def draw_on_pi_image(input_path='pi_captured_photo.jpg', output_path='pi_annotated_photo.jpg'):
    """
    Reads a captured image, draws text, a rectangle, and a circle on it, displays, and saves.
    """
    img = cv2.imread(input_path)

    if img is None:
        print(f"Error: Could not load image from {input_path}. Please ensure you ran Step 2 first.")
        return

    annotated_img = img.copy()

    cv2.putText(annotated_img, "Hello Raspberry Pi Vision!", (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)

    cv2.rectangle(annotated_img, (100, 100), (400, 300), (0, 255, 0), 3)

    center_x = annotated_img.shape[1] // 2
    center_y = annotated_img.shape[0] // 2
    cv2.circle(annotated_img, (center_x, center_y), 50, (255, 0, 0), -1)

    cv2.imshow("Original Pi Image", img)
    cv2.imshow("Annotated Pi Image", annotated_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    success = cv2.imwrite(output_path, annotated_img)
    if success:
        print(f"Annotated image saved as {output_path}")
    else:
        print(f"Error: Could not save annotated image to {output_path}")

draw_on_pi_image()

