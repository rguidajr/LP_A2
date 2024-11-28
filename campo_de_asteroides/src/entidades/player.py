import pygame, sys, os
#from settings import Settings

class Nave:
    """Criacao e gerenciamento da espaçonave"""

    def __init__(self, screen) -> None:
        """inicializa a espaçonave e ajusta a posição inicial"""
        self.screen = screen 
        

        # Caminho absoluto para a imagem da nave
        base_path = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_path, '../../assets/imagens/ship.png')

        # Carregar a imagem da nave
        try:
            self.image = pygame.image.load(image_path).convert_alpha()
            self.rect = self.image.get_rect()
            # Posiciona a nave no centro inferior da tela
            self.rect.midbottom = (screen.get_width() // 2, screen.get_height() - 20)
        except pygame.error as e:
            print(f"Erro ao carregar a imagem da nave: {image_path}\n{e}")
            self.image = pygame.Surface((50, 50))  # Placeholder em caso de erro
            self.image.fill((255, 0, 0))  # Cor vermelha para identificar o erro
            self.rect = self.image.get_rect()
            self.rect.midbottom = (screen.get_width() // 2, screen.get_height() - 20)

        # Atributos de movimentacao
        self.moving_direita = False


    def update(self):
        """Atualiza o movimento da espaçonave"""
        if self.moving_direita:
            self.rect.x += 1



    def draw(self):
        """Desenha a nave na tela."""
        self.screen.blit(self.image, self.rect)
