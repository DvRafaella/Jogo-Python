import pygame
import random

class Enemy:

    def __init__(self):

        img = pygame.image.load("player1_idle.png").convert_alpha()
        img = pygame.transform.scale(img,(120,120))

        self.image = img

        self.x = random.randint(900,1100)
        self.y = 330

        self.rect = self.image.get_rect(topleft=(self.x,self.y))

        self.dead = False
        self.speed = random.randint(2,4)


    def update(self):

        if not self.dead:

            self.x -= self.speed

            if self.x < -150:
                self.x = random.randint(900,1100)

        self.rect.x = self.x
        self.rect.y = self.y


    def draw(self,screen):

        if not self.dead:
            screen.blit(self.image,(self.x,self.y))