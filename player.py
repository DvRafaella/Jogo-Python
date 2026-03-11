import pygame

class Player:

    def __init__(self):

        img = pygame.image.load("player2_idle.png").convert_alpha()
        img = pygame.transform.scale(img,(120,120))

        self.image = img

        self.x = 100
        self.y = 330

        self.rect = self.image.get_rect(topleft=(self.x,self.y))

        self.life = 3
        self.attacking = False


    def attack(self):

        self.attacking = True


    def update(self):

        self.rect.x = self.x
        self.rect.y = self.y

        self.attacking = False


    def draw(self,screen):

        screen.blit(self.image,(self.x,self.y))