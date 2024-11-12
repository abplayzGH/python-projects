import cv2
import numpy as np
import turtle as trtl
import random 

t = trtl.Turtle()

def mapf(x, in_min, in_max, out_min, out_max):
    """
    Maps a float value 'x' from one range [in_min, in_max] to another range [out_min, out_max].
    
    :param x: Value to be mapped (float).
    :param in_min: Lower bound of the input range (float).
    :param in_max: Upper bound of the input range (float).
    :param out_min: Lower bound of the output range (float).
    :param out_max: Upper bound of the output range (float).
    
    :return: Mapped value (float) in the output range [out_min, out_max].
    """
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def make_shape(r, g, b, x ,y):
    
    t.goto(x,y)
    # t.setheading(random.randint(0,360))
    t.setheading(45)
    color = (r, g, b)
    t.color(color)
    t.begin_fill()
    # t.circle(random.randint(5,25), steps = random.randint(1,9))
    t.circle(10, steps = 4)
    t.end_fill()
    
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
    image_path = './image2.png'  # Change this to your image file path
    
    rgb_array = image_to_rgb_array(image_path)
    turtle_rgb = []
    
    
    for pixel in rgb_array:
            a = mapf(pixel[0], 0, 255, 0, 1)
            b = mapf(pixel[1], 0, 255, 0, 1)
            c = mapf(pixel[2], 0, 255, 0, 1)
            turtle_rgb.append([a, b, c])
                 
    print(rgb_array)
    
    for i in range(len(turtle_rgb)):
        r = turtle_rgb[i][0]
        g = turtle_rgb[i][1]
        b = turtle_rgb[i][2]
        print(f"I:{i}, R:{r}, G:{g}, B:{b}")
        make_shape(r, g, b, i*20, 100)
    
    
    # if rgb_array is not None:
    #     print("RGB Values Array:")
    #     print(rgb_array)

# trtl.update()
wn = trtl.Screen()
wn.mainloop()