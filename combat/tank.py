import pygame
import math as m
from config import *


def draw_tank(s):
    angle1 = 0
    angle2 = 0
    # player 1
    tank1 = pygame.Rect(120, 325, 0, 0)
    tank1_image = pygame.image.load("tank1.png")

    # player 2
    tank2 = pygame.Rect(1010, 325, 0, 0)
    tank2_image = pygame.image.load("tank2.png")

    def move(obj, velocity, angle):
        dx = pygame.Vector2(0, velocity).rotate(-angle)
        obj.rect += dx
        obj.rect.center = round(obj.rect[0]), round(obj.rect[1])

    for event in pygame.event.get():
        # Quits if you close the window
        if event.type == pygame.QUIT:
            pygame.display.quit()
            exit()

        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            tank1.x += 5

        if key[pygame.K_a]:
            move(tank1, 5, angle1)

        if key[pygame.K_d]:

        if key[pygame.K_UP]:
            tank2.x -= 5

        if key[pygame.K_RIGHT]:

        if key[pygame.K_LEFT]:

    # Spawn Players
    s.blit(tank1_image, (tank1.x, tank1.y))
    s.blit(tank2_image, (tank2.x, tank2.y))
