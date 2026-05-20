"""
Please write a program where two players each direct their own robot. One of the players should use the arrow keys while the other could use, for example, the w-s-a-d keys. 
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
        "v":2,
        "up":False,
        "down":False,
        "left":False,
        "right":False,
        "keys":"wsad"
    },
    {
        "x":0,
        "y":50,
        "v":2,
        "up":False,
        "down":False,
        "left":False,
        "right":False,
        "keys":"arrows"
    }
]

##Movement key trackers
# arobot["right"] = False
# arobot["left"] = False
# arobot["up"] = False
# arobot["down"] = False



## Clock initialization
clock = pygame.time.Clock()

### Main loop of program
while True:
    for event in pygame.event.get():  # returns a list of any events collected since the previous iteration
        for arobot in [robot for robot in robots if robot["keys"] == "arrows"]:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    arobot["left"] = True
                if event.key == pygame.K_RIGHT:
                    arobot["right"] = True
                if event.key == pygame.K_UP:
                    arobot["up"] = True
                if event.key == pygame.K_DOWN:
                    arobot["down"] = True
                if event.key == pygame.K_LSHIFT:
                    for arobot in robots:
                        arobot["v"] = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    arobot["left"] = False
                if event.key == pygame.K_RIGHT:
                    arobot["right"] = False
                if event.key == pygame.K_UP:
                    arobot["up"] = False
                if event.key == pygame.K_DOWN:
                    arobot["down"] = False
                if event.key == pygame.K_LSHIFT:
                    for arobot in robots:
                        arobot["v"] = 2

        for arobot in [robot for robot in robots if robot["keys"] == "wsad"]:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    arobot["left"] = True
                if event.key == pygame.K_d:
                    arobot["right"] = True
                if event.key == pygame.K_s:
                    arobot["up"] = True
                if event.key == pygame.K_w:
                    arobot["down"] = True
                if event.key == pygame.K_LSHIFT:
                    for arobot in robots:
                        arobot["v"] = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    arobot["left"] = False
                if event.key == pygame.K_d:
                    arobot["right"] = False
                if event.key == pygame.K_s:
                    arobot["up"] = False
                if event.key == pygame.K_w:
                    arobot["down"] = False
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
        if arobot["left"] and arobot["x"] > 0:
            arobot["x"] -= arobot["v"]
        if arobot["right"] and arobot["x"]+robot_w < window_w:
                arobot["x"] += arobot["v"]
        if arobot["up"] and arobot["y"] > 0:
            arobot["y"] -= arobot["v"]
        if arobot["down"] and arobot["y"]+robot_h < window_h:
            arobot["y"] += arobot["v"]
        
    # robot_x += robot_velocity #Velocity pixels to the right for eacht iteration
    clock.tick(60) #Indicates that the loop should be executed 60 times a second

"""
import pygame
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
robot = pygame.image.load("robot.png")
 
# positions of robots
positions = [[0, 0],
          [width-robot.get_width(), height-robot.get_height()]]
 
controls = []
# key, which robot moves, horizontal movement, vertical movement
controls.append((pygame.K_LEFT, 0, -2, 0))
controls.append((pygame.K_RIGHT, 0, 2, 0))
controls.append((pygame.K_UP, 0, 0, -2))
controls.append((pygame.K_DOWN, 0, 0, 2))
controls.append((pygame.K_a, 1, -2, 0))
controls.append((pygame.K_d, 1, 2, 0))
controls.append((pygame.K_w, 1, 0, -2))
controls.append((pygame.K_s, 1, 0, 2))
 
clock = pygame.time.Clock()
 
key_pressed = {}
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            key_pressed[event.key] = True
 
        if event.type == pygame.KEYUP:
            del key_pressed[event.key]
 
        if event.type == pygame.QUIT:
            exit()
 
    for key in controls:
        if key[0] in key_pressed:
            positions[key[1]][0] += key[2]
            positions[key[1]][1] += key[3]
 
    screen.fill((0, 0, 0))
    for i in range(2):
        screen.blit(robot, (positions[i][0], positions[i][1]))
    pygame.display.flip()
 
    clock.tick(60)
"""