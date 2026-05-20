
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
        "v":2
    },
]

##Movement key trackers
to_right = False
to_left = False
to_up = False
to_down = False

## Clock initialization
clock = pygame.time.Clock()

### Main loop of program
while True:
    for event in pygame.event.get():  # returns a list of any events collected since the previous iteration
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_UP:
                to_up = True
            if event.key == pygame.K_DOWN:
                to_down = True
            if event.key == pygame.K_LSHIFT:
                for arobot in robots:
                    arobot["v"] = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                to_up = False
            if event.key == pygame.K_DOWN:
                to_down = False
            if event.key == pygame.K_LSHIFT:
                for arobot in robots:
                    arobot["v"] = 2

        if event.type == pygame.QUIT:
            exit()
        

        
    ##Window initialization
    window.fill(
        (255,160,122)
    )  # fill method fills the window with the RGB tuple passed as an argument
    for arobot in robots:
        x = arobot["x"]
        y = arobot["y"]
        window.blit(robot,(x, y))
    pygame.display.flip()  # updates the contents of the window.

    ##Movement updates if within boundaries
    for arobot in robots:
        if to_left and arobot["x"] > 0:
            arobot["x"] -= arobot["v"]
        if to_right and arobot["x"]+robot_w < window_w:
                arobot["x"] += arobot["v"]
        if to_up and arobot["y"] > 0:
            arobot["y"] -= arobot["v"]
        if to_down and arobot["y"]+robot_h < window_h:
            arobot["y"] += arobot["v"]
        
    # robot_x += robot_velocity #Velocity pixels to the right for eacht iteration
    clock.tick(60) #Indicates that the loop should be executed 60 times a second
