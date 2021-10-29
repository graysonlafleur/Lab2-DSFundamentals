import pygame
class Ball:
    RADIUS = 10

    def __init__(self, x, y, vx, vy, screen, color, bgcolor, WIDTH, HEIGHT, BORDER):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.screen = screen
        self.bgcolor = bgcolor
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.BORDER = BORDER

    def show(self, color):
        pygame.draw.circle(self.screen, color, (self.x, self.y), self.RADIUS)

    def update(self):
        self.show(self.bgcolor)
        if self.x + self.vx - self.RADIUS <= self.BORDER:
            self.vx = -self.vx
        if self.y + self.vy - self.RADIUS <= self.BORDER:
            self.vy = -self.vy
        if self.y + self.vy + self.RADIUS >= self.HEIGHT-self.BORDER:
            self.vy = -self.vy
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(self.color)
