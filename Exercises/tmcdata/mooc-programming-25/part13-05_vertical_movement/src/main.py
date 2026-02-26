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

robot_x = 0
robot_y = 0
robot_velocity = 1

## Clock initialization
clock = pygame.time.Clock()

### Main loop of program
while True:
    for (
        event
    ) in (
        pygame.event.get()
    ):  # returns a list of any events collected since the previous iteration
        if event.type == pygame.QUIT:
            exit()
        
    ##Window initialization
    window.fill(
        (255,160,122)
    )  # fill method fills the window with the RGB tuple passed as an argument
    window.blit(robot,(robot_x, robot_y))
    pygame.display.flip()  # updates the contents of the window.

    ##Movement updates
    robot_y += robot_velocity

    ##Movement boundaries
    if robot_velocity > 0 and robot_y+robot_h >= window_h:
        robot_velocity = -robot_velocity
    if robot_velocity < 0 and robot_y <= 0: 
        robot_velocity = -robot_velocity

    # robot_x += robot_velocity #Velocity pixels to the right for eacht iteration
    clock.tick(60) #Indicates that the loop should be executed 60 times a second





