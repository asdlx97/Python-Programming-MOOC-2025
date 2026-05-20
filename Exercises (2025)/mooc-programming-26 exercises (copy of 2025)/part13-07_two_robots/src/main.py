# WRITE YOUR SOLUTION HERE:
import pygame  # Imports pygame module
from random import randint

###Initialization commands
pygame.init()  # Initializes pygame modules

#Creating my own window size variables
window_w = 640 #width
window_h = 480 #height

# .display Creates a window
# .set_mode takes windows dimensions as a tuple(width, height) in pixels
window = pygame.display.set_mode(
    (window_w, window_h)
)  # window variable can be used later to access it

#Creating my own variables for the four corners of the window
window_ul = (0,0)
window_ur = (window_w,0)
window_ll = (0, window_h)
window_lr = (window_w, window_h)

window_corners = [window_ul, window_ur, window_ll, window_lr]

## Robot initialization
robot = pygame.image.load(
    "robot.png"
)  # loads the image in the file and stores a reference to it in the variable
robot_w = robot.get_width() #returns the width of the image in pixels
robot_h = robot.get_height() #returns the length of the image in pixels

robots = [
    {
        "x":0,
        "y":50,
        "v":1
    },
    {
        "x":0,
        "y":150,
        "v":2
    }
]
robot_x = 0
robot_y = 0
robot_velocity = 1

robot2_x = 0
robot2_y = 50
robot2_velocity = 2

## Clock initialization
clock = pygame.time.Clock()

### Main loop of program
while True:
    for (
        event
    ) in (
        #pygame.event.get()
    ):  # returns a list of any events collected since the previous iteration
        print(event)
        if event.type == pygame.QUIT:
            exit()
        
    ##Window initialization
    window.fill(
        (255,160,122)
    )  # fill method fills the window with the RGB tuple passed as an argument
    for arobot in robots:
        x = int(arobot["x"])
        y = int(arobot["y"])
        window.blit(robot,(x, y))
    pygame.display.flip()  # updates the contents of the window.

    ##Movement updates
    for arobot in robots:
        arobot["x"] += arobot["v"]

    ##Movement boundaries
    for arobot in robots:
        if arobot["v"] > 0 and arobot["x"]+robot_w >= window_w:
            arobot["v"] = -arobot["v"]
        if arobot["v"] < 0 and arobot["x"] <= 0: 
            arobot["v"] = -arobot["v"]
    

    # robot_x += robot_velocity #Velocity pixels to the right for eacht iteration
    clock.tick(60) #Indicates that the loop should be executed 60 times a second


