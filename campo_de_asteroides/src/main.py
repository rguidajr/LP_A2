
import pygame, sys, os
from settings import Settings


class GameManager:
		
    def __init__(self) -> None:
        # Inicializa os módulos do Pygame
        pygame.init()

        # Cria um relógio para controlar o FPS (quadros por segundo)
        self.clock = pygame.time.Clock()

        # Inicializa as configurações do jogo, como tamanho da tela e plano de fundo
        self.settings = Settings()

    def run_game(self):
        """Loop principal do jogo."""
        running = True  # Variável para manter o jogo em execução

        while running:
            # Captura e trata eventos, como o fechamento da janela
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Desenha o plano de fundo
            self.settings.draw_background()

            # Atualiza o conteúdo da tela
            pygame.display.flip()

        # Finaliza o Pygame e encerra o programa corretamente
        pygame.quit()
        sys.exit()



if __name__ == '__main__':
    # Inicializa e executa o jogo
    game = GameManager()
    game.run_game()                   
