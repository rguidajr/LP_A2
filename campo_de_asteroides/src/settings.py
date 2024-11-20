import pygame,os

class Settings:

    """classe que armazena as configurações do jogo campo de asteróides """
    # Screen
    def __init__(self):

        # Configurações de tela
        self.width = 1200 # Largura da tela
        self.height = 720 # Altura da tela
        screen_size = (self.width, self.height)

        # Inicialização da tela
        self.screen = pygame.display.set_mode((self.width, self.height))  # Inicializa a janela
        #self.screen.fill((0, 0, 0))
        pygame.display.set_caption('Campo de Asteroides')

        # Caminho absoluto para a imagem de fundo
        base_path = os.path.dirname(os.path.abspath(__file__)) # Diretório atual
        image_path = os.path.join(base_path, '../assets/imagens/background.png') # Caminho relativo ao fundo

        try:
            # Carrega a imagem de fundo e ajusta seu tamanho para preencher a tela
            self.background = pygame.image.load(image_path).convert()
            self.background = pygame.transform.scale(self.background, (self.width, self.height))
        except pygame.error as e:
            # Caso o arquivo não seja encontrado ou não carregue, exibe um erro e usa uma tela de fundo preto
            print(f"Erro ao carregar a imagem de fundo: {e}")
            self.background = pygame.Surface((self.width, self.height))
            self.background.fill((0, 0, 0))  # Fundo preto 

    def draw_background(self):
        """Desenha o fundo na tela."""
        self.screen.blit(self.background, (0, 0))

    def update(self):
        pass
        
        
    

    
        