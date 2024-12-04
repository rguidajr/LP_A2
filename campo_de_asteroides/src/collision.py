import pygame
from score import ScoreManager
from sound_manager import SoundManager
from entidades.meteoro_especial import MeteoroEspecial


class CollisionManager:
    """
    Gerencia todas as colisões do jogo.
    """

    def __init__(self, player, meteor_group, laser_group, sound_manager):
        """
        Inicializa o gerenciador de colisões.

        Args:
            player (pygame.sprite.Sprite): Nave do jogador.
            meteor_group (pygame.sprite.Group): Grupo contendo os meteoros.
            laser_group (pygame.sprite.Group): Grupo contendo os lasers.
        """
        self.player = player
        self.meteor_group = meteor_group
        self.laser_group = laser_group
        self.sound_manager = sound_manager  

    def handle_laser_meteor_collisions(self, score_manager):
        """
        Verifica e lida com colisões entre lasers e meteoros.
        """
        for laser in self.laser_group:
            hit_meteoros = pygame.sprite.spritecollide(laser, self.meteor_group, True)
            if hit_meteoros:
                laser.kill() # remove o laser após colisão
                for meteoro in hit_meteoros:
                    # Verifica se é um MeteoroEspecial
                    if isinstance(meteoro, MeteoroEspecial):
                        score_manager.add_score(50)  # 50 pontos oara meteoro especial
                    else:
                        score_manager.add_score(10)  # Pontuação padrão para meteoros normais
                    meteoro.kill()
                self.sound_manager.play_explosion()
                
    def handle_player_meteor_collision(self):
        """
        Verifica e lida com colisões entre o jogador e meteoros.

        Returns:
            bool: True se o jogador perdeu todas as vidas, False caso contrário.
        """
        if pygame.sprite.spritecollide(self.player, self.meteor_group, True):
            self.sound_manager.play_explosion()  # Adiciona o som de explosão
            self.player.lose_life()

            # Verifica se o jogador ainda tem vidas
            if not self.player.is_alive():
                return True  
        return False


