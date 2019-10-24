import pygame, sys
from pygame.locals import *
import os

mn=input("???:")

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 50
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Hello World!')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
BLACK = (0, 0, 0)

X=50
Y=0

fontObj = pygame.font.Font(None, 80-len(mn))
textSurfaceObj = fontObj.render(mn,True, BLACK, WHITE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (10, SCREEN_HEIGHT/2)
# bgm = pygame.mixer.music.load('fancy.mp3')
# pygame.mixer.music.play(1)

while True: # main game loop
    screen.fill(WHITE)
    score_text = fontObj.render(mn, True, (0, 0, 0))
    screen.blit(score_text, (X, Y))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

