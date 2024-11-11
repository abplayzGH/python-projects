import cv2
import numpy as np
# import turtle as trtl

# t = trtl.Turtle()

def map_range(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min


def image_to_rgb_array(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        print("Error: Could not read the image.")
        return None

    # Convert the image from BGR to RGB format
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Flatten the image array and convert it to a list
    rgb_values = rgb_image.reshape(-1, 3)

    return rgb_values




# Main code
if __name__ == "__main__":
    # Specify the path to your image file
    image_path = './image.jpg'  # Change this to your image file path
    
    rgb_array = image_to_rgb_array(image_path)
    # turtle_rgb = []
    # for pixel in rgb_array:
    #     for i in range(3):
    #         turtle_rgb.append([map_range(rgb_array[pixel][i], )])
    
    if rgb_array is not None:
        print("RGB Values Array:")
        print(rgb_array)

# trtl.update()
# wn = trtl.Screen()
# wn.mainloop()