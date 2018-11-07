import casilla as casilla

class Tablero:
    tablero = None
    casillas_vacias=9

    def __init__(self):
        self.reiniciar_juego()


    def reiniciar_juego(self):
        self.tablero=[[casilla.Casilla(),casilla.Casilla(),casilla.Casilla()],
                      [casilla.Casilla(),casilla.Casilla(),casilla.Casilla()],
                      [casilla.Casilla(),casilla.Casilla(),casilla.Casilla()]]
        self.casillas_vacias=9

    def imprimir(self):
        lista_jugadas=[]
        for fila in self.tablero:
            for casilla in fila:
                simbolo = casilla.get_simbol()
                if(simbolo == "-"):
                    lista_jugadas.append(' ')
                else:
                    lista_jugadas.append(casilla.get_simbol())
        cadena_res = self.insertar_simbolos(lista_jugadas)
        print(cadena_res)


    def insertar_simbolos(self, lista_simbolos):

        res = '       1     2      3         \n' \
              '          |     |            \n' \
              'A     '+lista_simbolos[0]+'   |  '+lista_simbolos[1]+'  |  '+lista_simbolos[2]+'         \n' \
              '          |     |            \n' \
              '   ---------------------\n' \
              '          |     |            \n' \
              'B     '+lista_simbolos[3]+'   |  '+lista_simbolos[4]+'  |  '+lista_simbolos[5]+'         \n' \
              '          |     |            \n' \
              '   ---------------------\n' \
              '          |     |            \n' \
              'C     '+lista_simbolos[6]+'   |  '+lista_simbolos[7]+'  |  '+lista_simbolos[8]+'         \n' \
              '          |     |            \n'
        return  res

    def marcada(self,fila,columna):
        casilla = self.tablero[fila][columna]
        res = False
        if(casilla.marcado == True):
            res = True
        return res

    def marcar_casilla(self,simbol, fila, columna):
        casilla = self.tablero[fila][columna]
        casilla.marcar(simbol)
        self.casillas_vacias=self.casillas_vacias-1

    def get_tablero(self):
        return self.tablero

    def lleno(self):
        res = False
        if(self.casillas_vacias==0):
            res = True
        return res


