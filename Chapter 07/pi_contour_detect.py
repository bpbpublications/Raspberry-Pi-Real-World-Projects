import cv2

image_path = 'pi_captured_photo.jpg'
img_color = cv2.imread(image_path, cv2.IMREAD_COLOR)

if img_color is None:
    print(f"Error: Could not load image from {image_path}. Please check the path and file.")
else:
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    img_blurred = cv2.GaussianBlur(img_gray, (5, 5), 0)
    ret, thresh = cv2.threshold(img_blurred, 127, 255, cv2.THRESH_BINARY_INV)

    contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    img_contours = img_color.copy()

    cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 2)

    print(f"Found {len(contours)} contours.")

    cv2.imshow("Original Image", img_color)
    cv2.imshow("Thresholded Image", thresh)
    cv2.imshow("Contours Detected", img_contours)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Contours detected and displayed.")
