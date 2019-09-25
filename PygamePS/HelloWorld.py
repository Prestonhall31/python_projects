import pygame
import sys

pygame.init()

windowSize = (800, 600)

screen = pygame.display.set_mode(windowSize)

myriadProFont = pygame.font.SysFont("Myriad Pro", 48)

helloWorld = myriadProFont.render("Hello World", 1, (255, 0, 255), (255, 255, 255))

x, y = 0, 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:_sys.exit()

    screen.fill((0,0,0))

    screen.blit(helloWorld, (x, y))

    x += 1

    pygame.display.update()