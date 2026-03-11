import pygame
from settings import *


class Inimigo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.state = "walk"
        self.frame_atual = 0
        self.ultimo_update = pygame.time.get_ticks()
        self.velocidade_animacao = 100
        self.velocidade = VELOCIDADE_INIMIGO
        self.direcao = -1  # -1 para esquerda, 1 para direita

        self.animacoes = {"walk": [], "death": []}
        self.carregar_animacoes()

        if self.animacoes["walk"]:
            self.image = self.animacoes["walk"][0]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y - self.rect.height

    def carregar_animacoes(self):
        try:
            # idle = pygame.image.load("assets/images/enemy_idle.png").convert_alpha()
            walk = pygame.image.load("assets/images/enemy_walk.png").convert_alpha()
            death = pygame.image.load("assets/images/enemy_death.png").convert_alpha()

            self.animacoes["walk"] = self.extrair_frames(walk)
            self.animacoes["death"] = self.extrair_frames(death)

            print("✅ Inimigo carregado")

        except Exception as e:
            print(f"❌ Inimigo: {e}")
            surf = pygame.Surface((40, 60))
            surf.fill(VERMELHO)
            self.animacoes["walk"] = self.extrair_frames(walk)
            self.animacoes["death"] = self.extrair_frames(death)

    def extrair_frames(self, sheet, frame_width=128):
        frames = []
        num_frames = sheet.get_width() // frame_width
        altura = sheet.get_height()

        for i in range(num_frames):
            rect = pygame.Rect(i * frame_width, 0, frame_width, altura)
            frame = sheet.subsurface(rect)
            frames.append(frame)
        return frames

    def update(self):
        if self.state == "walk":
            self.rect.x += self.velocidade * self.direcao

        agora = pygame.time.get_ticks()
        if agora - self.ultimo_update > self.velocidade_animacao:
            self.ultimo_update = agora
            self.frame_atual += 1

            frames = self.animacoes[self.state]

            if self.frame_atual >= len(frames):
                if self.state == "death":
                    return False
                self.frame_atual = 0

            self.image = frames[self.frame_atual]

            if self.direcao == -1:
                self.image = pygame.transform.flip(self.image, True, False)

        return True

    def morrer(self):
        if self.state != "death":
            self.state = "death"
            self.frame_atual = 0
            return True
        return False