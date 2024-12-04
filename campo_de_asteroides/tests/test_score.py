class ScoreManager:
    """
    Gerencia a pontuação do jogo.
    """

    def __init__(self):
        """
        Inicializa o gerenciador de pontuação.
        """
        self.score = 0

    def add_score(self, points):
        """
        Adiciona pontos à pontuação atual.

        Args:
            points (int): Pontos a serem adicionados.
        """
        self.score += points
        #print(f"Pontuação: {self.score}")

    def get_score(self):
        """
        Retorna a pontuação atual.

        Returns:
            int: Pontuação atual.
        """
        return self.score
    
    def reset(self):
        """
        Reinicia a pontuação para zero.
        """
        self.score = 0
        
