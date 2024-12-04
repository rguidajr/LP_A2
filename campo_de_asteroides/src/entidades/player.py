import pygame
import os



class Player(pygame.sprite.Sprite):
    """
    Classe que representa a nave do jogador.

    Atributos:
        image (pygame.Surface): Imagem da nave carregada a partir de um arquivo.
        rect (pygame.Rect): Retângulo para posicionamento e colisão da nave.
        screen_width (int): Largura da tela.
        screen_height (int): Altura da tela.
    """

    def __init__(self, groups, screen_width, screen_height, settings):
        """
        Inicializa a nave e a posiciona no centro inferior da tela.

        Args:
            group (pygame.sprite.Group): Grupo ao qual a nave será adicionada.
            screen_width (int): Largura da tela.
            screen_height (int): Altura da tela.
        """
        super().__init__(groups)

         # Velocidade de movimento e quantidade de vidas do jogador
        self.settings = settings
        self.lives = 3

        # Caminho para a imagem da nave
        base_path = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_path, '../../assets/imagens/ship.png')

        try:
            # Tenta carregar a imagem da nave
            self.image = pygame.image.load(image_path).convert_alpha()
        except pygame.error as e:
            print(f"Erro ao carregar a imagem da nave: {image_path}\n{e}")
            # Caso a imagem não seja encontrada, cria uma nave simples
            self.image = pygame.Surface((50, 50))  # Dimensão padrão para fallback
            self.image.fill((255, 0, 0))  # Vermelho como indicação de erro

        # Configura o rect com base na imagem e posiciona no centro inferior da tela
        self.rect = self.image.get_rect(midbottom=(screen_width / 2, screen_height - 20))
        
        # Armazena as dimensões da tela para controle de movimentação
        self.screen_width = screen_width
        self.screen_height = screen_height

        

    def lose_life(self):
        """função para controlar perda de vidas"""
        self.lives -= 1
        print( f"Vidas restantes: {self.lives}")
              
    def is_alive(self):
        """Checa que o player ainda tem vidas"""
        return self.lives > 0

    def input_position(self, delta_time):
        """
        Atualiza a posição da nave com base nas teclas pressionadas e a velocidade em funcao do delta time
        """
        keys = pygame.key.get_pressed()

        dx = 0
        dy = 0
        speed = self.settings.player_speed * self.settings.delta_time

        # Movimenta a nave para a esquerda ou direita
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:  # Setas ou tecla 'A'
            self.rect.x -= speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:  # Setas ou tecla 'D'
            self.rect.x += speed

        # Movimenta a nave para cima ou para baixo
        if keys[pygame.K_UP] or keys[pygame.K_w]:  # Setas ou tecla 'W'
            self.rect.y -= speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:  # Setas ou tecla 'S'
            self.rect.y += speed
        
            
        # Limita o movimento da nave aos limites da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height

        
