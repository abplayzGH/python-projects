import cv2
import numpy as np
import turtle as trtl

t = trtl.Turtle()
wn = trtl.Screen()
wn.colormode(255)  # Set the color mode to 255 for RGB values

screen = trtl.Screen()
screen.setup(1920, 1080)
t.speed(0)

# trtl.tracer(0,0)
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

def make_shape(r, g, b, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(45)
    color = (r, g, b)
    t.color(color)
    t.begin_fill()
    t.circle(5, steps=4)  # Draw a small square
    t.end_fill()

def image_to_rgb_array(image_path):
    """
    Converts an image to a 2D array of RGB values.

    :param image_path: Path to the image file.
    :return: 2D array of RGB values or None if the image cannot be read.
    """
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not read the image.")
        return None

    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return rgb_image

# Main code
if __name__ == "__main__":
    image_path = './brenden2.jpg'  # Change this to your image file path
    rgb_array = image_to_rgb_array(image_path)
    
    if rgb_array is not None:
        height, width, _ = rgb_array.shape
        for y in range(height):
            for x in range(width):
                r, g, b = rgb_array[y, x]
                # make_shape(r, g, b, x * 5 - width * 5, height * 5 - y * 5)
                make_shape(r, g, b, x, y)
                
        trtl.update()
        wn.mainloop()