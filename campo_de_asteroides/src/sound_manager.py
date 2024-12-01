import pygame
import os

class SoundManager:
    """
    Classe responsável por gerenciar os sons do jogo.
    """

    def __init__(self):
        """Inicializa o mixer do Pygame e carrega os sons."""
        pygame.mixer.init()  # Inicializa o mixer de som

        # Caminhos dos arquivos de som
        #base_path = os.path.dirname(__file__)
        base_path = os.path.dirname(os.path.abspath(__file__))


        self.laser_path = os.path.join(base_path, '../assets/sons/laser.ogg')
        self.explosion_path = os.path.join(base_path, '../assets/sons/explosion.wav')
        self.music_path = os.path.join(base_path, '../assets/sons/music.wav')

        # Teste os caminhos gerados
        print(f"Laser Path: {self.laser_path}")
        print(f"Explosion Path: {self.explosion_path}")
        print(f"Music Path: {self.music_path}")

        # Certifique-se de que os caminhos são válidos
        if not os.path.exists(self.laser_path):
            raise FileNotFoundError(f"Arquivo não encontrado: {self.laser_path}")

        # Carrega os sons
        self.laser_sound = pygame.mixer.Sound(self.laser_path)
        self.laser_sound.set_volume(0.5)  # Volume do som do laser

        self.explosion_sound = pygame.mixer.Sound(self.explosion_path)
        self.explosion_sound.set_volume(1.4)  # Volume da explosão

        # Configura a música de fundo
        pygame.mixer.music.load(self.music_path)
        pygame.mixer.music.set_volume(0.1)  # Volume da música de fundo

    def play_laser(self):
        """Reproduz o som do disparo do laser."""
        self.laser_sound.play()

    def play_explosion(self):
        """Reproduz o som de explosão."""
        self.explosion_sound.play()

    def play_music(self):
        """Inicia a música de fundo em loop infinito."""
        pygame.mixer.music.play(-1)

    def stop_music(self):
        """Para a música de fundo."""
        pygame.mixer.music.stop()

    def set_music_volume(self, volume):
        """Define o volume da música de fundo."""
        pygame.mixer.music.set_volume(volume)

    def set_effects_volume(self, volume):
        """Define o volume dos efeitos sonoros."""
        self.laser_sound.set_volume(volume)
        self.explosion_sound.set_volume(volume)
