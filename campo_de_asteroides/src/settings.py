import pygame,os

class Settings:

    """classe que armazena as configurações do jogo campo de asteróides """
    def __init__(self):

        # Configurações de tela
        self.width = 1200 # Largura da tela
        self.height = 720 # Altura da tela
        
        # Inicialização da tela
        self.screen = pygame.display.set_mode((self.width, self.height))  # Inicializa a janela
        pygame.display.set_caption('Campo de Asteroides')

        # Caminho absoluto para a imagem de fundo
        base_path = os.path.dirname(os.path.abspath(__file__)) # Diretório atual
        image_path = os.path.join(base_path, '../assets/imagens/background.png') # Caminho relativo ao fundo

        try:
            # Carrega o pano de fundo e ajusta seu tamanho para preencher a tela
            self.background = pygame.image.load(image_path).convert()
            self.background = pygame.transform.scale(self.background, (self.width, self.height))
        except pygame.error as e:
            # Caso o arquivo não seja encontrado ou não carregue, exibe um erro e usa uma tela de fundo preto
            print(f"Erro ao carregar o pano de fundo: {e}")
            self.background = pygame.Surface((self.width, self.height))
            self.background.fill((0, 0, 0))  # Fundo preto 

        # Configuração do relógio e Delta Time
        self.clock = pygame.time.Clock()
        self.delta_time = 0

        # Temporizador para eventos no jogo
        self.meteor_timer = pygame.USEREVENT + 1
        #self.meteor_spawn_time = 1500  # Tempo em milissegundos (1.5 segundos)
        

    def configure_timers(self, spawn_time):
        """Configura os temporizadores do jogo."""
        pygame.time.set_timer(self.meteor_timer, 0)  # Cancela qualquer temporizador ativo
        pygame.time.set_timer(self.meteor_timer,spawn_time)


    def draw_background(self):
        """Desenha o pano fundo na tela. Esta como funcao para upgrades futuros no caso de multiploa niveis"""
        self.screen.blit(self.background, (0, 0))

    def update(self):
        """
        Atualiza configurações globais do jogo, como Delta Time e FPS.
        """
        # Atualiza o Delta Time
        self.delta_time = min(self.clock.tick(60) / 1000, 0.033)

        # Exibe os FPS no título da janela (opcional)
        fps = self.clock.get_fps()
        pygame.display.set_caption(f"Campo de Asteroides - FPS: {fps:.2f}")