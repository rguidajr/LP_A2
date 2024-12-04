import pygame, sys, os, random
from settings import Settings
from entidades.player import Player
from entidades.laser import Laser
from entidades.meteoro import Meteoro
from collision import CollisionManager
from score import ScoreManager
from sound_manager import SoundManager
from entidades.meteoro_especial import MeteoroEspecial
from difficulty import DifficultyManager


class GameManager:
    """
    Gerencia o ciclo principal e os componentes do jogo Campo de Asteroides.

    Atributos:
        settings (Settings): Configurações do jogo, como dimensões da tela e delta time.
        player_group (pygame.sprite.GroupSingle): Grupo que contém o sprite do jogador.
        laser_group (pygame.sprite.Group): Grupo que contém os sprites dos lasers disparados.
        meteor_group (pygame.sprite.Group): Grupo que contém os sprites dos meteoros.
        player (Player): O jogador controlado pelo usuário.
        sound_manager (SoundManager): Gerenciador de sons do jogo.
        collision_manager (CollisionManager): Gerenciador de colisões entre objetos do jogo.
        score_manager (ScoreManager): Gerenciador de pontuação do jogo.
        difficulty_manager (DifficultyManager): Gerenciador do nível de dificuldade do jogo.
        allow_shooting (bool): Controle para habilitar disparos pelo jogador.
        last_shot_time (int): Registro do tempo da última ação de disparo.
        shoot_cooldown (int): Tempo mínimo (em milissegundos) entre disparos consecutivos.
        running (bool): Indica se o jogo está ativo.
    """
		
    def __init__(self) -> None:
        """
        Inicializa os componentes essenciais do jogo e define os estados iniciais.

        Responsabilidades:
        - Inicializa o Pygame e configurações globais.
        - Configura os grupos de sprites para gerenciar o jogador, lasers e meteoros.
        - Cria os principais gerenciadores do jogo, incluindo som, colisões, pontuação e dificuldade.
        - Define os controles para disparos e o estado inicial do jogo.

        Raises:
        pygame.error: Caso ocorra um erro ao inicializar módulos do Pygame.
    """
        
        # Inicializa os módulos do Pygame
        pygame.init()

        # Inicializa as configurações do jogo
        self.settings = Settings()
        
        # Cria os grupos de sprites
        self.player_group = pygame.sprite.GroupSingle()
        self.laser_group = pygame.sprite.Group()
        self.meteor_group = pygame.sprite.Group()

        # Cria o sprite do jogador
        self.player = Player(self.player_group, self.settings.width, self.settings.height, self.settings)

        # Inicializa gerenciadores
        self.sound_manager = SoundManager()
        self.sound_manager.play_music()  # Inicia a música de fundo
        self.collision_manager = CollisionManager(self.player, self.meteor_group, self.laser_group, self.sound_manager)
        self.score_manager = ScoreManager()

        # inicializa o novel de dificuldade
        self.difficulty_manager = DifficultyManager(self.settings)

        # Controle para ignorar disparos iniciais
        self.allow_shooting = False
        self.last_shot_time = 0  # Para cooldown do disparo
        self.shoot_cooldown = 250  # Cooldown de 500ms (meio segundo)

        # Inicializa o estado do jogo como ativo
        self.running = True
        
    def handle_events(self):
        """Trata eventos do jogo."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if not self.allow_shooting:
                    self.allow_shooting = True  # Ativa o disparo após o jogo começar
                elif event.key == pygame.K_SPACE and self.allow_shooting:
                    current_time = pygame.time.get_ticks()  # Tempo atual em milissegundos
                    if current_time - self.last_shot_time > self.shoot_cooldown:
                        laser_pos = self.player.rect.midtop
                        self.laser_group.add(Laser(laser_pos, self.settings))
                        self.sound_manager.play_laser()
                        self.last_shot_time = current_time

            if event.type == self.settings.meteor_timer:
            # Chance de gerar um meteoro especial (10% de probabilidade, por exemplo)
                if random.random() < 0.2:  # 20% de chance
                    meteoro = MeteoroEspecial(self.settings.width, self.settings.height, self.settings, self.player)
                else:
                    meteoro = Meteoro(self.settings.width, self.settings.height, self.settings)
                self.meteor_group.add(meteoro)
  
    def update_game(self):
        """Atualiza os estados do jogo.""" 

        delta_time = self.settings.delta_time        

        # Atualiza as entidades
        self.player.input_position(delta_time)
        self.laser_group.update(delta_time)
        self.meteor_group.update(delta_time)

        # Verifica colisões entre lasers e meteoros
        self.collision_manager.handle_laser_meteor_collisions(self.score_manager)

        # Verifica colisões entre player e o meteoro
        if self.collision_manager.handle_player_meteor_collision():
            if not self.player.is_alive():
                self.running = False  # O jogo termina
            else:
                self.reset_after_collision()  # Reconfigura o estado do jogador

    def draw_game(self):
        """Desenha os elementos do jogo."""
        self.settings.draw_background()
        self.player_group.draw(self.settings.screen)
        self.laser_group.draw(self.settings.screen)
        self.meteor_group.draw(self.settings.screen)  

        # Exibe a pontuação
        font = pygame.font.Font(None, 36)  # Fonte padrão do pygame
        score_text = font.render(f"Pontuação: {self.score_manager.get_score()}", True, (255, 255, 255))
        self.settings.screen.blit(score_text, (10, 10))

        # Exibe as vidas restantes
        font = pygame.font.Font(None, 36)
        lives_text = font.render(f"Vidas: {self.player.lives}", True, (255, 255, 255))
        self.settings.screen.blit(lives_text, (10, 50))

    def game_over_screen(self):
        """Exibe a tela de 'Game Over'."""
        self.settings.draw_background()

        # Texto de Game Over
        font = pygame.font.Font(None, 74)
        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        self.settings.screen.blit(game_over_text, (self.settings.width // 2 - 200, self.settings.height // 2 - 100))

        # Texto de pontuação final
        font_small = pygame.font.Font(None, 36)
        score_text = font_small.render(f"Pontuação Final: {self.score_manager.get_score()}", True, (255, 255, 255))
        self.settings.screen.blit(score_text, (self.settings.width // 2 - 150, self.settings.height // 2))

        # Instruções para reiniciar ou sair
        restart_text = font_small.render("Pressione R para reiniciar ou Q para sair", True, (255, 255, 255))
        self.settings.screen.blit(restart_text, (self.settings.width // 2 - 200, self.settings.height // 2 + 50))

        pygame.display.flip()

        # Espera entrada do jogador para reiniciar ou sair
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # Reiniciar o jogo
                        python = sys.executable  
                        os.execl(python, python, *sys.argv)
                    elif event.key == pygame.K_q:  # Sair do jogo
                        pygame.quit()
                        sys.exit()

    def reset_after_collision(self):
        """Reinicializa o estado do jogo após uma colisão com o jogador."""
        # Limpar meteoros da tela
        self.meteor_group.empty()   
       
        if self.player.is_alive():
            # Resetar a posição do jogador
            self.player.rect.midbottom = (self.settings.width / 2, self.settings.height - 20)
            # Pausar o jogo momentaneamente
            pygame.time.delay(1000)  # 1 segundo de pausa
        else:
            # Caso contrário, termina o jogo
            self.running = False
     
    def reset_game(self):
        
        self.running = True  # Reativa o loop do jogo
        self.player.lives = 3  # Reinicia as vidas do jogador
        self.score_manager.reset()  # Reinicia a pontuação
        self.meteor_group.empty()  # Remove meteoros
        self.laser_group.empty()  # Remove lasers
        self.player.rect.midbottom = (self.settings.width // 2, self.settings.height - 20)  # Reposiciona o jogador
        self.sound_manager.play_music()  # Reinicia a música de fundo
        
        # Reinicia o gerenciador de dificuldade
        self.difficulty_manager.reset()

    def show_start_screen(self):
        """Exibe a tela inicial com os botões de dificuldade."""

        # Carrega a imagem de fundo
        base_path = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_path, '../assets/imagens/abertura.png')

        try:
            background = pygame.image.load(image_path).convert()
            background = pygame.transform.scale(background, (self.settings.width, self.settings.height))
        except pygame.error as e:
            print(f"Erro ao carregar a imagem de fundo: {e}")
            background = pygame.Surface((self.settings.width, self.settings.height))
            background.fill((0, 0, 0))  # Preto como fallback

        # Desenha a imagem de fundo
        self.settings.screen.blit(background, (0, 0))

        font_small = pygame.font.Font(None, 50)
        beginner_text = font_small.render("1 - Iniciante", True, (0,0,0))
        experienced_text = font_small.render("2 - Experiente", True, (0,0,0))
        quit_text = font_small.render("3 - Sair", True, (0,0,0))

        self.settings.screen.blit(beginner_text, (self.settings.width // 2 - 100, self.settings.height // 2 - 100))
        self.settings.screen.blit(experienced_text, (self.settings.width // 2 - 100, self.settings.height // 2 - 50))
        self.settings.screen.blit(quit_text, (self.settings.width // 2 - 100, self.settings.height // 2))
        
        pygame.display.flip()

            # Aguarda interação do usuário
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:  # Nível fácil
                        self.difficulty_manager.set_beginner()
                        selected_difficulty = "Iniciante"
                        return

                    elif event.key == pygame.K_2:  # Nível difícil
                            self.difficulty_manager.set_experienced()
                            selected_difficulty = "Experiente"
                            return
                           
                    elif event.key == pygame.K_3:
                        pygame.quit()
                        sys.exit()

    def run_game(self):

        """Loop principal do jogo."""
        self.running = True

        while self.running:
            self.settings.update() # delta time e FPS
            self.handle_events()  # Eventos 
            self.update_game()  # Estados
            self.draw_game()  # Renderizacao
            pygame.display.flip()
    
            # Exibe a tela de "Game Over" após o loop terminar
        self.game_over_screen()
         
if __name__ == '__main__':
    # Inicializa e executa o jogo
    game = GameManager()
    game.show_start_screen()
    game.run_game() 