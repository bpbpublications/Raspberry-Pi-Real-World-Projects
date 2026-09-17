import cv2
image_path = '/home/pi/mytest/fruit_test.jpg' 

# Read the image in color mode (default)
img_color = cv2.imread(image_path, cv2.IMREAD_COLOR)

# Read the same image in grayscale mode
img_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Check if images were loaded successfully
if img_color is None:
    print(f"Error: Could not load colour image from {image_path}. Please check the path and file.")
if img_gray is None:
    print(f"Error: Could not load grayscale image from {image_path}. Please check the path and file.")

if img_color is not None and img_gray is not None:
    # Display the color image
    cv2.imshow('Original Color Image', img_color)
    # Display the grayscale image
    cv2.imshow('Original Grayscale Image', img_gray)

    # Wait indefinitely until any key is pressed
    cv2.waitKey(0)

    # Destroy all OpenCV windows
    cv2.destroyAllWindows()
    print("Images displayed and windows closed.")
