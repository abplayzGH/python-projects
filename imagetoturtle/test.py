import cv2
import numpy as np
import turtle as trtl

# Initialize the turtle
t = trtl.Turtle()
t.speed(0)  # Set the fastest drawing speed
t.hideturtle()

# Function to map a value from one range to another
def mapf(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Function to draw a shape based on RGB values
def make_shape(r, g, b, x, y):
    t.penup()  # Make sure turtle doesn't draw a line while moving to the position
    t.goto(x, y)  # Go to the specified position
    t.pendown()  # Start drawing
    t.setheading(45)  # Set an arbitrary angle
    
    # Normalize the RGB values to the range [0.0, 1.0]
    color = (r / 255.0, g / 255.0, b / 255.0)  # Convert to float in [0, 1]
    t.color(color)  # Set the fill color
    t.begin_fill()
    t.circle(10, steps=4)  # Draw a square shape with 4 steps (circle with 4 points)
    t.end_fill()

# Function to convert the image to an RGB array
def image_to_rgb_array(image_path, scale_factor=10):
    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        print("Error: Could not read the image.")
        return None

    # Get the original image dimensions
    height, width, _ = image.shape

    # Calculate new width and height based on the scale factor
    new_width = max(1, width // scale_factor)
    new_height = max(1, height // scale_factor)

    # Resize the image while maintaining valid dimensions
    resized_image = cv2.resize(image, (new_width, new_height))

    # Convert the image from BGR to RGB format
    rgb_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

    # Flatten the image array and return as a 2D NumPy array
    rgb_values = rgb_image.reshape(-1, 3)

    return rgb_values, new_width, new_height

# Main code to generate the turtle drawing
if 1==1:
    # Specify the path to your image file
    image_path = './image2.png'  # Change this to your image file path

    # Convert the image to RGB values and get the resized image dimensions
    rgb_array, new_width, new_height = image_to_rgb_array(image_path, scale_factor=20)

    # Set up the turtle screen
    wn = trtl.Screen()
    wn.bgcolor("white")
    wn.setup(width=800, height=600)

    # Starting position for the turtle
    start_x = -new_width * 10 // 2  # Start position for x-axis (centered)
    start_y = new_height * 10 // 2  # Start position for y-axis (centered)

    # Draw shapes based on the RGB values of the image
    for i in range(len(rgb_array)):
        r, g, b = rgb_array[i]
        
        # Calculate position in a grid based on the index
        x = start_x + (i % new_width) * 20  # Spread out horizontally
        y = start_y - (i // new_width) * 20  # Spread out vertically
        
        # Draw the shape
        make_shape(r, g, b, x, y)

    # Finish drawing and keep the screen open
    wn.mainloop()
