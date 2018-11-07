import csvManager
import os

class tictactoe:
    iterations = 0
    p1s = 0
    p2s = 0
    ties = 0
    pure_ai = True
    tablero = None
    jugadores = None
    resultado_game="Tie"
    lista_posiciones = [[(0, 0), (0, 1), (0, 2)],
                        [(1, 0), (1, 1), (1, 2)],
                        [(2, 0), (2, 1), (2, 2)],
                        [(0, 0), (1, 0), (2, 0)],
                        [(0, 1), (1, 1), (2, 1)],
                        [(0, 2), (1, 2), (2, 2)],
                        [(0, 0), (1, 1), (2, 2)],
                        [(2, 0), (1, 1), (0, 2)]]

    def __init__(self, tablero, jugadores):
        self.jugadores=jugadores
        self.tablero=tablero
        self.csvManager=csvManager.csvManager(jugadores)
        for j in jugadores:
            if j.tengo_ai() == False:
                self.pure_ai = False
                break

    def jugar(self):
        self.iterations += 1
        self.tablero.imprimir()
        while(self.end_game() != True):
            for jugador in self.jugadores:
                if(jugador.tengo_ai()):
                    posicion = jugador.ai_play(self.tablero.get_tablero())
                else:
                    print("ingrese jugada")
                    posicion = self.solicitar_jugada()
                    while(posicion == None):
                        posicion = self.solicitar_jugada()
                self.tablero.marcar_casilla(jugador.get_simbol(),posicion[0],posicion[1])
                self.verificar_jugada_ganadora(jugador)
                os.system('cls')
                self.tablero.imprimir()
                if (self.end_game()):
                    break

        self.tablero.imprimir()

        ganador = self.show_ganador()
        if self.resultado_game == "Tie":
            self.ties += 1
        elif self.resultado_game == "player1":
            self.p1s += 1
        elif self.resultado_game == "player2":
            self.p2s += 1
        self.aprender()
        if not self.pure_ai or self.iterations % 100 == 0:
            os.system('cls')
            self.tablero.imprimir()
            print("Statistics", self.iterations, "ties", self.ties, "p1", self.p1s, "p2", self.p2s)

        print(ganador, self.iterations, self.ties)
        #self.new_game()


    def end_game(self):
        res = False
        ganador=self.buscar_ganador()
        if(ganador!=None):
            res= True
        if(self.tablero.lleno()):
            res = True
        return res

    def new_game(self,t=None):
        print(self.pure_ai)
        if self.pure_ai == False:
            print("Press R to play again")
            tecla = input()
        else:
            if t == None:
                print("Playing again !")
                tecla = "R"
                if(tecla=="r" or tecla=="R"):
                    self.tablero.reiniciar_juego()
                    for jugador in self.jugadores:
                        jugador.reset()
                    self.jugar()
            else:
                self.csvManager.guardarAprendizaje(self.jugadores)



    def verificar_jugada_ganadora(self,jugador):
        estado_tablero = self.tablero.get_tablero()
        for casilla in self.lista_posiciones:
            p1 = casilla[0]
            p2 = casilla[1]
            p3 = casilla[2]
            if(estado_tablero[p1[0]][p1[1]].simbol == jugador.get_simbol() and estado_tablero[p2[0]][p2[1]].simbol == jugador.get_simbol() and estado_tablero[p3[0]][p3[1]].simbol==jugador.get_simbol()):
                jugador.set_estado(True)
                self.resultado_game=jugador.get_name()
                break

    def buscar_ganador(self):
        res = None
        for jugador in self.jugadores:
            if(jugador.ganaste()==True):
                res = jugador
                self.resultado_game = jugador.get_name()
        return res

    def parser_jugada(self, pocision):
        res = None
        if(pocision == 'a1' or pocision == 'A1'):
            res = (0,0)
        if (pocision == 'a2' or pocision == 'A2'):
            res = (0,1)
        if (pocision == 'a3' or pocision == 'A3'):
            res = (0,2)
        if (pocision == 'b1' or pocision == 'B1'):
            res = (1,0)
        if (pocision == 'b2' or pocision == 'B2'):
            res = (1,1)
        if (pocision == 'b3' or pocision == 'B3'):
            res = (1,2)
        if (pocision == 'c1' or pocision == 'C1'):
            res = (2,0)
        if (pocision == 'c2' or pocision == 'C2'):
            res = (2,1)
        if (pocision == 'c3' or pocision == 'C3'):
            res = (2,2)
        return res

    def solicitar_jugada(self):
        cadena = input()
        cadena = self.validar_entrada(cadena)
        if(cadena != None):
            res =  self.parser_jugada(cadena)
            if(self.tablero.marcada(res[0],res[1]) == True):
                print("pocicion ya fue marcada ingrece otra")
                res=None
        else:
            print("Ingrece un movimiento valido")
            res=None
        return res

    def validar_entrada(self, cadena):
        res=None
        if(len(cadena)==2):
            if(cadena[0]=='a' or cadena[0]== 'b' or cadena[0]=='c' or cadena[0]=='A' or cadena[0]== 'B' or cadena[0]=='C'):
                if(cadena[1]=='1' or cadena[1]=='2' or cadena[1]=='3'):
                    res=cadena
        return res

    def show_ganador(self):
        return self.resultado_game

    def aprender(self):
        for jugador in self.jugadores:
            jugador.aprender(self.resultado_game)

    def encender(self):
        print('load csv data')
        self.jugar()

    def entrenar(self, iteraciones):
        #jugador 1
        #jugador 2
        #entrenando
        print(iteraciones)