import pygame
import random
from paddle import Paddle
from ball import Ball

def main():
    pygame.init()

    pygame.display.set_caption("Lab2")
    WIDTH = 800
    HEIGHT = 480
    FPS = 60
    VELOCITY = random.randrange(-10, 10)
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.update()

    #WALLS
    wcolor = pygame.Color("purple")
    BORDER = 20
    #top wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,0),(WIDTH,BORDER)))
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,0),(BORDER,HEIGHT)))
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,HEIGHT-BORDER),(WIDTH,HEIGHT)))

    #Ball init
    x0 = WIDTH - Ball.RADIUS
    y0 = HEIGHT // 2
    vx0 = abs(VELOCITY)-10
    vy0 = VELOCITY
    print(vy0, vx0)
    b0 = Ball(x0, y0, vx0, vy0, screen, "white", "black", WIDTH, HEIGHT, BORDER)
    b0.show("white")

    pygame.display.update()

    running = True
    clock = pygame.time.Clock()

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            
        pygame.display.update()
        clock.tick(FPS)
        #Ball movement
        b0.update()

main()