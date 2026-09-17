import cv2
import numpy as np

image_path = "pi_captured_photo.jpg"
img_color = cv2.imread(image_path, cv2.IMREAD_COLOR)

if img_color is None:
    print(f"Error: Could not load image from {image_path}.")
else:
    # Convert to grayscale
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    # Sobel edge detection (combined)
    sobelx = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, ksize=5)
    sobelx = np.uint8(np.absolute(sobelx))
    sobely = np.uint8(np.absolute(sobely))
    sobel_combined = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

    # Canny edge detection
    canny_edges = cv2.Canny(img_gray, 100, 200)

    # Show results
    cv2.imshow("Grayscale Image", img_gray)
    cv2.imshow("Sobel Edges", sobel_combined)
    cv2.imshow("Canny Edges", canny_edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
