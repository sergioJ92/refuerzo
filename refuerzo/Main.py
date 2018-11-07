from time import sleep

import Tictactoe
import Tablero
import Jugador
import QLearning

ai=QLearning.QLearning()
ai2=QLearning.QLearning()

jugador1=Jugador.Jugador("player1",'X',ai)
jugador2=Jugador.Jugador("player2",'O',None)

jugadores=[]
jugadores.append(jugador1)
jugadores.append(jugador2)

tablero=Tablero.Tablero()
game=Tictactoe.tictactoe(tablero,jugadores)

game.encender()


#while True:
#    game.new_game()
#    if game.iterations == 3:
#        game.new_game(t="q")
#        break