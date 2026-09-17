import cv2

image_path = 'fruit_test.jpg' # Ensure this image exists
img_color = cv2.imread(image_path, cv2.IMREAD_COLOR)

if img_color is None:
    print(f"Error: Could not load image from {image_path}. Please check the path and file.")
else:
    # Convert the color image to grayscale
    img_gray_converted = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    # Convert the color image to HSV
    img_hsv_converted = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV)

    # Display both original color and converted images
    cv2.imshow('Original Color Image', img_color)
    cv2.imshow('Converted Grayscale Image', img_gray_converted)
    cv2.imshow('Converted HSV Image', img_hsv_converted)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Color space conversions displayed.")
