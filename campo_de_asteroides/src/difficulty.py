class DifficultyManager:
    """
    Gerencia os níveis de dificuldade do jogo.
    """

    def __init__(self, settings):
        """
        Inicializa o gerenciador de dificuldade.

        Args:
            settings (Settings): Instância das configurações globais do jogo.
        """
        self.settings = settings
        self.current_difficulty = None  # Inicializa a dificuldade como indefinida

    def set_beginner(self):
        """Configura o jogo para o nível iniciante."""
        self.settings.meteor_speed = 300
        self.settings.player_speed = 400
        self.settings.laser_speed = 700
        self.settings.configure_timers(1500) # Configurado para 1,5 s
        
    def set_experienced(self):
        """Configura o jogo para o nível experiente."""
        self.settings.meteor_speed = 500
        self.settings.player_speed = 500
        self.settings.laser_speed = 900
        self.settings.configure_timers(1000) # configurado para 1,0 s
        
    def reset(self):
        """ Zera os noveis de dificuldade quando jogo acionado pela tela game_over _screen"""
        self.current_difficulty = None
