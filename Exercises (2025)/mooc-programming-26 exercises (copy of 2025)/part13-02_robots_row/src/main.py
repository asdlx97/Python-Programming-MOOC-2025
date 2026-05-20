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

#Draw 10 robots in a row
start_w = 40
constant_h = 70
for i in range(0,10):
    window.blit(robot,(start_w+(i*robot_w),constant_h))

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
