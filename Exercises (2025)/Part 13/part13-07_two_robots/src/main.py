"""
Please create an animation where two robots move back and forth to the left and right. The lower robot should move at double the speed of the upper one.
"""


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


"""
#Suggested solution

import pygame
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
robot = pygame.image.load("robot.png")
 
x1 = 0
x2 = 0
speed1 = 1
speed2 = 2
 
clock = pygame.time.Clock()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 
    x1 += speed1
    if x1 == 0 or x1+robot.get_width() == width:
        speed1 = -speed1
    x2 += speed2
    if x2 == 0 or x2+robot.get_width() == width:
        speed2 = -speed2
 
    screen.fill((0, 0, 0))
    screen.blit(robot, (x1, 50))
    screen.blit(robot, (x2, 200))
    pygame.display.flip()
 
    clock.tick(60)
# WRITE YOUR SOLUTION HERE:
 
"""


