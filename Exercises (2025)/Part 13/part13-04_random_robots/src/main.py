"""
Please write a program which draws a thousand robots in random places.
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

window.fill(
    (255,160,122)
)  # fill method fills the window with the RGB tuple passed as an argument
# window.blit(
#     robot, (100, 50)
# )  # .blit method draws the image with the top left!! of image at tuple(width, height)
# window.blit(
#     robot, (window_w/2-robot_w/2, window_h/2-robot_h/2)
# )  # .blit method draws the image in the middle

#Draw 1000 robots in a random spot
for i in range(0,1000):
    random_w = randint(0, window_w-robot_w)
    random_h = randint(0, window_h-robot_h)
    window.blit(robot, (random_w, random_h))

pygame.display.flip()  # updates the contents of the window.

### Main loop of program
while True:
    for (
        event
    ) in (
        pygame.event.get()
    ):  # returns a list of any events collected since the previous iteration
        if event.type == pygame.QUIT:
            exit()

"""
#Suggested solution

import pygame
from random import randint
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((640, 480))
 
robot = pygame.image.load("robot.png")
 
screen.fill((0, 0, 0))
for i in range(1000):
    x = randint(0,width-robot.get_width())
    y = randint(0,height-robot.get_height())
    screen.blit(robot, (x,y))
pygame.display.flip()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

#Review
My solution results in the same output, the suggested one
didn't define robot width and height variables.
"""