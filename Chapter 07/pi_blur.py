import cv2

# Read the input image
img = cv2.imread("pi_captured_photo.jpg")

if img is None:
    print("Error: Could not load image. Please ensure you ran Step 2 first.")
else:
    # Show original image
    cv2.imshow("Original Image", img)

    # Apply Averaging Blur
    avg_blurred = cv2.blur(img, (5, 5))
    cv2.imshow("Averaging Blurred", avg_blurred)
    cv2.imwrite("pi_blurred_avg.jpg", avg_blurred)

    # Apply Gaussian Blur
    gaussian_blurred = cv2.GaussianBlur(img, (5, 5), 0)
    cv2.imshow("Gaussian Blurred", gaussian_blurred)
    cv2.imwrite("pi_blurred_gaussian.jpg", gaussian_blurred)

    # Apply Median Blur
    median_blurred = cv2.medianBlur(img, 5)
    cv2.imshow("Median Blurred", median_blurred)
    cv2.imwrite("pi_blurred_median.jpg", median_blurred)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
