#import random
import math
from entidades.meteoro import Meteoro

class MeteoroEspecial(Meteoro):
    """
    Classe que representa um meteoro especial com características únicas:
    - Mais rápido que os meteoros comuns.
    - Movimenta-se na direção do jogador.
    - Concede uma vida extra ao jogador se destruído.
    """
    def __init__(self, screen_width, screen_height, settings, player):
        """
        Inicializa o meteoro especial.

        Args:
            screen_width (int): Largura da tela.
            screen_height (int): Altura da tela.
            settings (Settings): Instância das configurações globais do jogo.
            player (Player): Referência ao jogador para direcionar o meteoro.
        """
        super().__init__(screen_width, screen_height, settings)

        self.player = player  # Referência ao jogador

        # Aumentar a velocidade base em 80%
        self.speed *= 1.8

    def update(self, delta_time):
        """
        Atualiza a posição do meteoro, movendo-o em direção ao jogador.

        Args:
            delta_time (float): Delta Time para ajuste de velocidade.
        """
        # Calcula o vetor de direção em direção ao jogador
        direction_x = self.player.rect.centerx - self.rect.centerx
        direction_y = self.player.rect.centery - self.rect.centery
        magnitude = math.sqrt(direction_x**2 + direction_y**2)
        direction_x /= magnitude
        direction_y /= magnitude

        # Atualiza a posição com base na direção normalizada e velocidade
        self.rect.x += direction_x * self.speed * delta_time
        self.rect.y += direction_y * self.speed * delta_time

        # Remove o meteoro se ele sair da tela
        if self.rect.bottom < 0 or self.rect.top > self.settings.height or self.rect.right < 0 or self.rect.left > self.settings.width:
            self.kill()
