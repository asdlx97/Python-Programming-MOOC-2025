# WRITE YOUR SOLUTION HERE:
import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

amount = 10
angle = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    for i in range(amount):
        offset = (2 * math.pi / amount) * i
        x = 320 + math.cos(angle + offset) * 150 - robot.get_width() / 2
        y = 240 + math.sin(angle + offset) * 150 - robot.get_height() / 2
        window.blit(robot, (x, y))

    pygame.display.flip()

    angle += 0.01
    clock.tick(60)