# LP_A2

# Campo de Asteroides

**Campo de Asteroides** é um projeto desenvolvido em Python utilizando a biblioteca Pygame. Este trabalho faz parte da disciplina **Linguagem de Programação** do curso de Matemática Aplicada da **FGV**, sob orientação do **Prof. Matheus**, e será avaliado como nota da segunda prova.

O objetivo do jogo é criar um ambiente onde o jogador controla uma nave espacial para desviar ou atirar contra asteroides que colidem espontaneamente com a tela. A seguir, detalhamos a estrutura do projeto e as funcionalidades implementadas até agora.

---

## Organização do Projeto

O código está organizado da seguinte forma:

campo_de_asteroides/
├── assets/
│   ├── imagens/               # Recursos visuais do jogo, como o plano de fundo
│   └── sons/                  # Recursos de áudio do jogo (em desenvolvimento)
├── docs/
│   └── documentacao.tex       # Documentação do projeto em LaTeX
├── requirements.txt           # Dependências do projeto
├── src/
│   ├── audio/                 # Módulo para gerenciar sons (em desenvolvimento)
│   ├── entidades/             # Entidades do jogo, como nave e asteroides (em desenvolvimento)
│   ├── settings.py            # Configurações do jogo, como tamanho da tela e plano de fundo
│   └── main.py                # Arquivo principal para execução do jogo
├── tests/
│   └── test_entidades.py      # Testes unitários das classes e funcionalidades
└── venv/                      # Ambiente virtual para dependências


---

## Principais Arquivos e Suas Funções

### 1. `main.py`
Este é o arquivo principal do projeto, responsável por iniciar o jogo e gerenciar o loop principal.

- **Funções principais:**
  - `GameManager.__init__`: 
    - Inicializa os módulos do Pygame.
    - Configura o relógio para controlar os quadros por segundo (FPS).
    - Carrega as configurações do jogo (como tamanho da tela e plano de fundo).
  - `GameManager.run_game`: 
    - Executa o loop principal do jogo.
    - Gerencia eventos, como o fechamento da janela.
    - Atualiza a tela com o plano de fundo.

---

### 2. `settings.py`
Este módulo centraliza as configurações globais do jogo, como dimensões da tela e plano de fundo.

- **Funções principais:**
  - `Settings.__init__`: 
    - Configura a tela com dimensões de 1200x720.
    - Carrega a imagem de fundo de `assets/imagens/background.png`.
    - Implementa um fallback para uma tela preta caso a imagem não seja encontrada.
  - `Settings.draw_background`: 
    - Desenha o plano de fundo na tela.
  - `Settings.update`: 
    - Método reservado para futuras alterações dinâmicas das configurações do jogo.

---

<<<<<<< HEAD
Alunos:

Romolo Guida  
Maia Ribeiro
=======
>>>>>>> main

