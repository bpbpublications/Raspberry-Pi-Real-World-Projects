import cv2

image_path = 'pi_captured_photo.jpg' # Use a photo captured from your Pi
img_color = cv2.imread(image_path, cv2.IMREAD_COLOR)

if img_color is None:
    print(f"Error: Could not load image from {image_path}. Please check the path and file.")
else:
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    thresh_mean = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                        cv2.THRESH_BINARY, 11, 2)

    thresh_gaussian = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                            cv2.THRESH_BINARY, 11, 2)

    cv2.imshow("Original Grayscale", img_gray)
    cv2.imshow("Adaptive Mean Threshold", thresh_mean)
    cv2.imshow("Adaptive Gaussian Threshold", thresh_gaussian)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Images with adaptive thresholding displayed.")
