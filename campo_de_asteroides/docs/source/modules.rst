Estrutura dos módulos
=====
Jogo Espacial com Pygame
Visão Geral do Projeto
------------------------
Este é um jogo espacial desenvolvido usando Pygame, onde o jogador controla uma nave espacial e enfrenta meteoros.
**Estrutura do Projeto**

1. Módulos Principais
-----------------------

main.py
^^^^^^^
- Ponto de entrada principal do jogo
- Inicializa a janela de jogo
- Gerencia o loop principal do jogo
- Coordena a interação entre diferentes componentes

settings.py
^^^^^^^^^^^
- Armazena configurações globais do jogo
- Define constantes como:
  * Dimensões da tela
  * Cores
  * Configurações de FPS
  * Parâmetros iniciais do jogo

collision.py
^^^^^^^^^^^^
- Implementa a lógica de detecção de colisões
- Gerencia interações entre diferentes entidades:
  * Colisão player-meteoro
  * Colisão laser-meteoro
  * Outras interações críticas de colisão

score.py
^^^^^^^^
- Gerencia o sistema de pontuação
- Funções para:
  * Atualizar pontuação

sound_manager.py
^^^^^^^^^^^^^^^^
- Controla todos os efeitos sonoros do jogo
- Gerencia:
  * Sons de fundo
  * Efeitos sonoros de colisão
  * Música do jogo

difficulty.py
^^^^^^^^^^^^^
- Define níveis de dificuldade


2. Módulo de Entidades
------------------------

entidades/player.py
^^^^^^^^^^^^^^^^^^

Classe que representa o jogador
Métodos para:

Movimento da nave
Posição da nave
Estado do jogador



entidades/laser.py
^^^^^^^^^^^^^^^^^

Gerencia os lasers disparados pelo jogador
Controla:

Movimento do laser
Dano causado
Desaparece com laser após sumir da tela



entidades/meteoro.py
^^^^^^^^^^^^^^^^^^^

Classe base para meteoros
Implementa:

Movimento aleatorio
Frequencia de aparecimento




entidades/meteoro_especial.py
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Subclasse de meteoro com comportamentos especiais

Persegue a nave
Maior velocidade







.. toctree::
   :maxdepth: 4

