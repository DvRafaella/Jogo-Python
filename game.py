import pygame
from settings import *
from player import Player
from enemy import Enemy

class Game:

    def __init__(self,screen):

        self.screen = screen
        self.clock = pygame.time.Clock()

        bg = pygame.image.load("player1_idle.png").convert_alpha()
        self.background = pygame.transform.scale(bg,(WIDTH,HEIGHT))

        self.player = Player()

        self.enemies = [Enemy(),Enemy()]

        self.score = 0
        self.game_over = False

        self.font = pygame.font.SysFont(None,40)


    def update(self):

        if self.game_over:
            return

        self.player.update()

        for enemy in self.enemies:

            enemy.update()

            if self.player.rect.colliderect(enemy.rect):

                if self.player.attacking:

                    enemy.dead = True
                    self.score += 1

                else:

                    self.player.life -= 1
                    enemy.x = 1000

                    if self.player.life <= 0:
                        self.game_over = True


    def draw(self):

        self.screen.blit(self.background,(0,0))

        self.player.draw(self.screen)

        for enemy in self.enemies:
            enemy.draw(self.screen)

        score = self.font.render(f"Score: {self.score}",True,(255,255,255))
        life = self.font.render(f"Vida: {self.player.life}",True,(255,255,255))

        self.screen.blit(score,(20,20))
        self.screen.blit(life,(20,60))

        if self.game_over:

            txt = self.font.render("GAME OVER",True,(255,0,0))

            self.screen.blit(
                txt,
                (WIDTH//2 - txt.get_width()//2, HEIGHT//2)
            )


    def run(self):

        running = True

        while running:

            self.clock.tick(FPS)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_SPACE:
                        self.player.attack()

            self.update()
            self.draw()

            pygame.display.update()