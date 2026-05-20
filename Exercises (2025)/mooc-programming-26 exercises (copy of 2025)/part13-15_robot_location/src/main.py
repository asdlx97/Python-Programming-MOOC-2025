# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window_w = 640 #width
window_h = 480 #height
window = pygame.display.set_mode((window_w, window_h))

robot = pygame.image.load("robot.png")
robot_w = robot.get_width() #returns the width of the image in pixels
robot_h = robot.get_height() #returns the length of the image in pixels

robot_x = 0
robot_y = 0
target_x = 0
target_y = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # target_x = event.pos[0]-robot.get_width()/2
            # target_y = event.pos[1]-robot.get_height()/2
            if event.pos[0] > robot_x and event.pos[0] < robot_x+robot_w and event.pos[1] > robot_y and event.pos[1] < robot_y + robot_h:
                target_x = random.randint(0,window_w-int(robot.get_width()))
                target_y = random.randint(0,window_h-int(robot.get_height()))

        if event.type == pygame.QUIT:
            exit(0)

    # if robot_x > target_x:
    #     robot_x -= 1
    # if robot_x < target_x:
    #     robot_x += 1
    # if robot_y > target_y:
    #     robot_y -= 1
    # if robot_y < target_y:
    #     robot_y += 1
    robot_x = target_x
    robot_y = target_y

    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()

    clock.tick(60)