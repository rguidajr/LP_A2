import pygame
import os
import random

class Meteoro(pygame.sprite.Sprite):
    """
    Classe que representa um meteoro inimigo.

    Atributos:
        image (pygame.Surface): Imagem do meteoro carregada a partir de um arquivo.
        rect (pygame.Rect): Retângulo para posicionamento e colisão do meteoro.
        speed (int): Velocidade do meteoro.
    """

    def __init__(self, screen_width, screen_height):
        """
        Inicializa o meteoro.

        Args:
            screen_width (int): Largura da tela.
            screen_height (int): Altura da tela.
        """
        super().__init__()

        # Caminho para a imagem do meteoro
        base_path = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_path, '../../assets/imagens/meteor.png')

        try:
            # Carregar a imagem do meteoro
            self.image = pygame.image.load(image_path).convert_alpha()
        except pygame.error as e:
            print(f"Erro ao carregar a imagem do meteoro: {image_path}\n{e}")
            # Caso a imagem não seja encontrada, cria um meteoro simples
            self.image = pygame.Surface((50, 50))
            self.image.fill((128, 128, 128))  # Cinza como fallback

        # Define o rect do meteoro
        self.rect = self.image.get_rect()

        # Posiciona o meteoro no topo da tela, em uma posição horizontal aleatória
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = -self.rect.height  # Começa fora da tela, acima do topo

        # Define a velocidade do meteoro
        self.speed = random.randint(3, 8)  # Velocidade variável

    def update(self):
        """
        Atualiza a posição do meteoro, movendo-o para baixo.
        """
        self.rect.y += self.speed
        # Remove o meteoro se ele sair da tela
        if self.rect.top > self.rect.height + self.rect.bottom:  
            self.kill() # Exclui fora da tela
