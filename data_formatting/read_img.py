import cv2

# Read the image from file
image_path = "/media/radar/00cb8602-b2ed-4b7e-8a79-cc67689c6748/calibration_radar_latest/scene5/folder0/image_2023-09-01-13-28-08.852602.jpg"  # Replace this with the actual path to your image file
image = cv2.imread(image_path)

# Check if the image was successfully loaded
if image is None:
    print("Error: Unable to load the image.")
else:
    # Resize the image to 720x1080
    desired_width = 640
    desired_height = 480
    resized_image = cv2.resize(image, (desired_width, desired_height))

    # Display the resized image using imshow
    cv2.imshow("Resized Image", resized_image)

    # Wait for a key press and then close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    




