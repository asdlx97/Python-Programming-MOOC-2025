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
robots = []
time_interval = 1500 # 200 milliseconds == 0.2 seconds
next_object_time = 0 
# robot = pygame.image.load(
#     "robot.png"
# )  # loads the image in the file and stores a reference to it in the variable
# robot_w = robot.get_width() #returns the width of the image in pixels
# robot_h = robot.get_height() #returns the length of the image in pixels

# robot["current_w"] = 0
# robot["current_h"] = 0
# robot["velo_x"] = 0
# robot["velo_y"] = 1

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
    current_time = pygame.time.get_ticks()
    if current_time > next_object_time:
        next_object_time += time_interval
        robots.append({"image":pygame.image.load("robot.png"), "current_w":randint(0, 640-pygame.image.load("robot.png").get_width()), "current_h":-pygame.image.load("robot.png").get_height(), "velo_x":0, "velo_y":1})

    for robot in robots:
        window.blit(robot["image"],(robot["current_w"], robot["current_h"]))
        robot["current_w"] += robot["velo_x"]
        robot["current_h"] += robot["velo_y"]

    pygame.display.flip()  # updates the contents of the window.
    
    ##Movement updates
    # robot["current_h"] += robot["velo_y"]
    # robot["current_w"] += robot["velo_x"]

    ##Movement boundaries
    for robot in robots:
        # if robot["velo_x"] > 0 and robot["current_w"]+pygame.image.load("robot.png").get_width() >= window_w:
        #     robot["velo_x"] = 1
        #     robot["velo_y"] = 0
        # if robot["velo_x"] < 0 and robot["current_w"] <= 0: 
        #     robot["velo_x"] = -1
        #     robot["velo_y"] = 0
        if robot["velo_y"] > 0 and robot["current_h"]+pygame.image.load("robot.png").get_height() >= window_h:
            if robot["current_w"]+pygame.image.load("robot.png").get_width() >= window_w/2:
                robot["velo_x"] = 1
                robot["velo_y"] = 0
            else:
                robot["velo_x"] = -1
                robot["velo_y"] = 0
        # if robot["velo_y"] < 0 and robot["current_h"] <= 0: 
        #     robot["velo_x"] = 0
        #     robot["velo_y"] = 1

    # robot["current_w"] += robot_velocity #Velocity pixels to the right for eacht iteration
    clock.tick(60) #Indicates that the loop should be executed 60 times a second