
import cv2
image_path = 'example.jpg' # Ensure this image exists
output_path_gray = 'example_grayscale.jpg'
# Read the image in colour
img_color = cv2.imread(image_path, cv2.IMREAD_COLOR)
if img_color is None:
    print(f"Error: Could not load image from {image_path}. Please check the path and file.")
else:
    # Convert to grayscale
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    # Save the grayscale image
    success = cv2.imwrite(output_path_gray, img_gray)
    if success:
        print(f"Grayscale image saved successfully to {output_path_gray}")
    else:
        print(f"Error: Could not save image to {output_path_gray}")
    # Optionally display the grayscale image to confirm
    cv2.imshow('Saved Grayscale Image', img_gray)
    cv2.waitKey(0)
