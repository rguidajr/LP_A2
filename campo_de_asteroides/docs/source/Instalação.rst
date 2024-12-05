==========================
Guia de Instalação e Uso
==========================

Este documento descreve como instalar e rodar o jogo **Campo de Asteroides**.

Pré-requisitos
==============

Certifique-se de ter o seguinte instalado no seu sistema:

- **Python** (versão 3.9 ou superior).
- **Pygame**, que será instalado automaticamente ao seguir as instruções abaixo.

Passos para Instalação
=======================

1. **Clonar ou Baixar o Projeto**
   - Clone o repositório do GitHub usando o comando:
   
     .. code-block:: bash

        git clone https://github.com/rguidajr/LP_A2.git

   - Ou baixe o projeto como arquivo ZIP e extraia o conteúdo.

2. **Instalar Dependências**
   - Navegue até o diretório principal do projeto, onde está localizado o arquivo ``requirements.txt``:

     .. code-block:: bash

        cd campo_de_asteroides

   - Instale as dependências necessárias executando o seguinte comando:

     .. code-block:: bash

        pip install -r requirements.txt

Passos para Rodar o Jogo
========================

1. Navegue até o diretório ``src`` onde está o arquivo principal do jogo ``main.py``:

   .. code-block:: bash

      cd src

2. Execute o jogo com o seguinte comando:

   .. code-block:: bash

      python main.py

Pronto! O jogo será iniciado.