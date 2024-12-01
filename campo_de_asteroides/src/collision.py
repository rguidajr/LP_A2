import pygame
from score import ScoreManager
from sound_manager import SoundManager

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
        self.sound_manager = sound_manager  # Adicionado para gerenciar sons

    def handle_laser_meteor_collisions(self, score_manager):
        """
        Verifica e lida com colisões entre lasers e meteoros.
        """
        for laser in self.laser_group:
            hit_meteoros = pygame.sprite.spritecollide(laser, self.meteor_group, True)
            if hit_meteoros:
                laser.kill()
                score_manager.add_score(len(hit_meteoros) * 10)
                self.sound_manager.play_explosion()
                print("Colisão: Laser atingiu meteoro!")

    def handle_player_meteor_collision(self):
        """
        Verifica e lida com colisões entre o jogador e meteoros.

        Returns:
            bool: True se o jogador perdeu todas as vidas, False caso contrário.
        """
        if pygame.sprite.spritecollide(self.player, self.meteor_group, True):
            self.sound_manager.play_explosion()  # Adiciona o som de explosão
            self.player.lose_life()
            #if not self.player.is_alive():
                #print("Game Over!")
            return True  
        return False


