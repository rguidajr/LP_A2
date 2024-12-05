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


## Como Rodar o Jogo

### Pré-requisitos
- **Python**: Certifique-se de ter o Python instalado (versão 3.9 ou superior).
- **Dependências**: As dependências necessárias para rodar o jogo estão listadas no arquivo `requirements.txt`.

### Passos para Rodar
1. **Clonar ou Baixar o Projeto**
   - Caso esteja hospedado no GitHub, use o comando:
     ```bash
     git clone https://github.com/rguidajr/LP_A2.git
     ```
   - Ou baixe o projeto como arquivo ZIP e extraia o conteúdo.

2. **Instalar Dependências**
   - Navegue até o diretório principal do projeto onde está localizado o arquivo `requirements.txt`. Com base na estrutura do projeto, o caminho correto é:
     ```bash
     cd campo_de_asteroides
     ```
   - Instale as dependências executando:
     ```bash
     pip install -r requirements.txt
     ```

3. **Executar o Jogo**
   - Navegue para o diretório `src`, onde está localizado o arquivo `main.py`. Use o comando:
     ```bash
     cd src
     ```
   - Execute o jogo:
     ```bash
     python main.py
     ```

---

## Como Jogar

### Tela Inicial
- Ao iniciar o jogo, uma tela inicial será exibida com três opções:
  - **1**: Iniciante (nível fácil).
  - **2**: Experiente (nível difícil).
  - **3**: Sair do jogo.

### Controles
- **Movimentação da Nave**:
  - Use as **setas direcionais** ou as teclas **WASD**:
    - **Esquerda/Direita**: Movimenta a nave horizontalmente.
    - **Cima/Baixo**: Movimenta a nave verticalmente.
- **Disparar Lasers**:
  - Pressione a **barra de espaço** para atirar e destruir os meteoros.

### Objetivo do Jogo
- **Sobreviver**: Evite que sua nave colida com os meteoros.
- **Destruir Meteoros**: Acerte os meteoros com lasers para ganhar pontos.
- **Atenção às Vidas**: Você perde uma vida ao colidir com meteoros. O jogo termina quando todas as vidas acabam.

### Game Over
- Após perder todas as vidas, será exibida a tela de "Game Over".
- Você pode:
  - Pressionar **R** para retornar à tela inicial.
  - Pressionar **Q** para sair do jogo.

---

## Como Acessar a Documentação

A documentação foi gerada utilizando o **Sphinx** e está disponível no formato HTML.

1. Navegue até o diretório `docs/build/html`:
   ```bash
   cd campo_de_asteroides/docs/build/html

## Autores

Este projeto foi desenvolvido por:

- **Romolo Guida**
- **Maia Ribeiro**
- **Antonio Batista**

**Divirta-se jogando Campo de Asteroides! 🚀**