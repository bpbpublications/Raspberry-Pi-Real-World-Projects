import cv2

image_path = 'pi_captured_photo.jpg' # Use a photo captured from your Pi
img_color = cv2.imread(image_path, cv2.IMREAD_COLOR)

if img_color is None:
    print(f"Error: Could not load image from {image_path}. Please check the path and file.")
else:
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    ret, thresh_binary = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
    ret, thresh_binary_inv = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

    cv2.imshow("Original Grayscale", img_gray)
    cv2.imshow("Binary Threshold", thresh_binary)
    cv2.imshow("Binary Inverse Threshold", thresh_binary_inv)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Images thresholded and displayed.")
