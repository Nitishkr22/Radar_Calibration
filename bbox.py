import cv2

def draw_box_on_image(image_path, x1, y1, x2, y2):
    # Load the image
    image = cv2.imread(image_path)
    
    # Draw the box on the image
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
    # org = (914, 267)
    # forge = (1090, 358)
    # font = cv2.FONT_HERSHEY_SIMPLEX
    # color = (0, 0, 255)
    # cv2.putText(image, 'x1y1', org, font, 0.5, color, 1, cv2.LINE_AA, False)
    # cv2.putText(image, 'x2y2', forge, font, 0.5, color, 1, cv2.LINE_AA, False)
    
    # Display the image with the box
    cv2.imshow('Image with Box', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path = '/home/radar/Documents/camera/trial_frames/1/image_2023-06-30-15-28-27.697716.jpg'  # Replace with the actual path to your image
x1, y1 = 1,90  # Top-left coordinates of the box
x2, y2 = 487,480  # Bottom-right coordinates of the box
draw_box_on_image(image_path, x1, y1, x2, y2)