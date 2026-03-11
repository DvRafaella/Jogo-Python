import pygame

class Button:

    def __init__(self,text,x,y,width,height,font):

        self.rect = pygame.Rect(x,y,width,height)
        self.text = text
        self.font = font

        self.color = (200,200,200)
        self.text_color = (0,0,0)

    def draw(self,screen):

        pygame.draw.rect(screen,self.color,self.rect)

        text_surface = self.font.render(self.text,True,self.text_color)

        screen.blit(
            text_surface,
            (
                self.rect.centerx - text_surface.get_width()//2,
                self.rect.centery - text_surface.get_height()//2
            )
        )

    def clicked(self,pos):

        return self.rect.collidepoint(pos)