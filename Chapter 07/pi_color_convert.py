import cv2

# Read the input image in colour
img_colour = cv2.imread("pi_captured_photo.jpg", cv2.IMREAD_COLOR)

if img_colour is None:
    print("Error: Could not load image. Please ensure you ran Step 2 first.")
else:
    # Show original image
    cv2.imshow("Original Colour Image", img_colour)

    # Convert to Grayscale
    img_gray = cv2.cvtColor(img_colour, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image", img_gray)
    cv2.imwrite("pi_converted_grayscale.jpg", img_gray)

    # Convert to HSV
    img_hsv = cv2.cvtColor(img_colour, cv2.COLOR_BGR2HSV)
    cv2.imshow("HSV Image", img_hsv)
    cv2.imwrite("pi_converted_hsv.jpg", img_hsv)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
