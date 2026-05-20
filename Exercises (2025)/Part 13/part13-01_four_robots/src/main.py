
"""
Please write a program which draws a robot in each of the four corners of the window.
"""

# The exercises in this part of the course have no automated tests, as the results as visually verified.
# The tests grant points automatically as you submit your solution to the server, no matter what your implementation.
# Only submit your solution when you are ready, and your solution matches the exercise description.
# The exercises may not have automatic tests, but the course staff will still see your solution.
# If your solution clearly does not match the exercise description, you may lose the points granted for the exercises in this part.

# WRITE YOUR SOLUTION HERE:

import pygame  # Imports pygame module

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
    (000, 000, 000)
)  # fill method fills the window with the RGB tuple passed as an argument
# window.blit(
#     robot, (100, 50)
# )  # .blit method draws the image with the top left!! of image at tuple(width, height)
# window.blit(
#     robot, (window_w/2-robot_w/2, window_h/2-robot_h/2)
# )  # .blit method draws the image in the middle

#Draw a robot on each corner of window
window.blit(robot, (window_ul)) #upper left
window.blit(robot, (0,window_h-robot_h)) #lower left
window.blit(robot, (window_w-robot_w, 0)) #upper right
window.blit(robot, (window_w-robot_w, window_h-robot_h)) #lower right

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
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
robot = pygame.image.load("robot.png")
 
right_x = width-robot.get_width()
down_y = height-robot.get_height()
 
screen.fill((0, 0, 0))
screen.blit(robot, (0, 0))
screen.blit(robot, (right_x, 0))
screen.blit(robot, (0, down_y))
screen.blit(robot, (right_x, down_y))
pygame.display.flip()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

#Review
My solution results in the same output, the suggested one
defined other variables than I did.
"""