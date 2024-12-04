import unittest
from unittest.mock import Mock, MagicMock, create_autospec
import pygame
from src.collision import CollisionManager
from src.entidades.meteoro_especial import MeteoroEspecial

class TestCollisionManager(unittest.TestCase):

    def setUp(self):
        # Mock para o jogador
        self.player = Mock()
        self.player.lives = 3
        self.player.lose_life = Mock()

        # Mock para grupos de sprites
        self.meteor_group = MagicMock(spec=pygame.sprite.Group)
        self.laser_group = MagicMock(spec=pygame.sprite.Group)

        # Mock para pygame.sprite.spritecollide
        pygame.sprite.spritecollide = Mock(return_value=[Mock()])  # Simula colisão

        # Mock para gerenciadores
        self.score_manager = Mock()
        self.sound_manager = Mock()

        # Instancia o CollisionManager com os mocks
        self.collision_manager = CollisionManager(
            self.player, self.meteor_group, self.laser_group, self.sound_manager
        )

    def test_handle_laser_meteor_collisions(self):
        # Simula lasers e meteoros colidindo
        laser = Mock()
        meteoro_normal = Mock()
        meteoro_especial = create_autospec(MeteoroEspecial, instance=True)  # Mocka um MeteoroEspecial
        #type(meteoro_especial).__name__ = 'MeteoroEspecial'

        # Configura os resultados das colisões
        self.laser_group.__iter__.return_value = [laser]
        pygame.sprite.spritecollide.return_value = [meteoro_normal, meteoro_especial]

        # Chama o método
        self.collision_manager.handle_laser_meteor_collisions(self.score_manager)

        # Verifica se o laser foi removido
        laser.kill.assert_called_once()

        # Verifica se os meteoros foram removidos
        meteoro_normal.kill.assert_called_once() # Garante que o meteoro foi eliminado
        meteoro_especial.kill.assert_called_once() # Garante que o especial foi eliminado

        # Verifica se a pontuação foi adicionada corretamente
        self.score_manager.add_score.assert_any_call(10)  # Para meteoro normal
        self.score_manager.add_score.assert_any_call(50)  # Para meteoro especial

        # Verifica se o som de explosão foi tocado
        self.sound_manager.play_explosion.assert_called_once()

    def test_handle_player_meteor_collision_game_over(self):
        # Configura o jogador para ter 1 vida antes da colisão
        self.player.lives = 1

        # Define o comportamento de is_alive para verificar o número de vidas
        def is_alive():
            return self.player.lives > 0

        self.player.is_alive = Mock(side_effect=is_alive)

        # Define o comportamento de lose_life para reduzir o número de vidas
        def lose_life():
            self.player.lives -= 1

        self.player.lose_life = Mock(side_effect=lose_life)

        # Simula uma colisão entre jogador e meteoro
        pygame.sprite.spritecollide.return_value = [Mock()]

        # Chama o método
        result = self.collision_manager.handle_player_meteor_collision()

    # Verifica se o jogador perdeu todas as vidas
        self.assertFalse(self.player.is_alive())  # Confirma que o jogador está sem vidas
        self.assertTrue(result)  # Retorna True para indicar "Game Over"


if __name__ == '__main__':
    unittest.main()
