

class Casilla:
    simbol = ""
    marcado = None

    def __init__(self):
        self.simbol = "-"
        self.marcado = False

    def reset(self):
        self.simbol="-"

    def marcado(self):
        return self.marcado

    def marcar(self, simbolo):
        self.simbol = simbolo
        self.marcado = True

    def get_simbol(self):
        return self.simbol
