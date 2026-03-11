import pygame
from settings import *
from button import Button
from game import Game

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("2D Pygame Game")

clock = pygame.time.Clock()

bg = pygame.image.load("player2_idle.png").convert_alpha()
menu_bg = pygame.transform.scale(bg,(WIDTH,HEIGHT))

font = pygame.font.SysFont(None,40)

btn1 = Button("PLAYER 1",400,200,200,60,font)
btn2 = Button("PLAYER 2",400,300,200,60,font)

running = True

while running:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            if btn1.clicked(event.pos):

                game = Game(screen)
                game.run()

            if btn2.clicked(event.pos):

                game = Game(screen)
                game.run()

    screen.blit(menu_bg,(0,0))

    btn1.draw(screen)
    btn2.draw(screen)

    pygame.display.update()

pygame.quit()