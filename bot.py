from random import randint

vizinhos_index = [(-1, 0), (-1, -1), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

class Bot:
    def __init__(self):
        self.tries = []

    def robot_try(self):
        x = randint(0, 5)
        y = randint(0, 5)
        #não faz tentativas repetidas
        while (x, y) in self.tries:
            x = randint(0, 5)
            y = randint(0, 5)
        self.tries.append((x, y))
        return (x, y)

    #tentar acertar vizinhos de satélite derrubado
    def robot_next_try(self, tabuleiro):
        x = self.tries[len(self.tries) - 1][0]
        y = self.tries[len(self.tries) - 1][1]
        while True:
            vizinho = 0
            while (vizinho < 7):
                if (tabuleiro.in_bounds(x + vizinhos_index[vizinho][0]) and tabuleiro.in_bounds(y + vizinhos_index[vizinho][1])):
                    break
                vizinho += 1
            linha = x + vizinhos_index[vizinho][0]
            coluna = y + vizinhos_index[vizinho][1]
            if ((linha, coluna) not in self.tries):
                return (x, y)
