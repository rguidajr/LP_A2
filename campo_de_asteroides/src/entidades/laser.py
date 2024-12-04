import pygame
import os


class Laser(pygame.sprite.Sprite):
    """
    Classe que representa o laser disparado pela nave.

    Atributos:
        image (pygame.Surface): Superfície do laser carregada a partir de um arquivo.
        rect (pygame.Rect): Retângulo para posicionamento e colisão do laser.
    """

    def __init__(self,pos, speed_settings):
        """
        Inicializa o laser com uma imagem e posiciona-o no topo da nave.

        Args:
            pos (tuple): Posição inicial do laser no formato (x, y), com base na nave.
        """
        super().__init__()
        
        # Caminho absoluto para a imagem do laser
        base_path = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_path, '../../assets/imagens/laser.png')

        # Carregar a imagem do laser
        try:
            self.image = pygame.image.load(image_path).convert_alpha()
        except pygame.error as e:
            print(f"Erro ao carregar a imagem do laser: {image_path}\n{e}")
            # Caso a imagem não seja encontrada, criar um laser simples
            self.image = pygame.Surface((5, 20))
            self.image.fill((255, 0, 0))  # Vermelho como fallback

        # Define o rect do laser com o ponto inicial no midtop
        self.rect = self.image.get_rect()
        self.rect.midtop = pos  # Alinha corretamente ao ponto inicial do Player
        
        # Ajusta a posição para compensar a altura extra da imagem
        # (se o laser estiver deslocado, ajuste o valor abaixo)
        self.rect.y -= 45 

        # Velocidade do laser
        self.speed = speed_settings.laser_speed


    def update(self,delta_time):
        """
        Atualiza a posição do laser, movendo-o para cima.
        Remove o laser do grupo se sair da tela.
        """
        self.rect.y -= self.speed * delta_time # Velocidade vertical do laser

        # Remove o laser se sair da tela
        if self.rect.bottom < 0:
            self.kill()

