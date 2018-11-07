

class Jugador:
    name=None
    simbol=None
    estado=None
    inteligencia=None

    def __init__(self,name,simbol,qlearning):
        self.name=name
        self.simbol=simbol
        self.estado=False
        self.inteligencia=qlearning

    def get_simbol(self):
        return self.simbol

    def get_name(self):
        return self.name

    def set_estado(self, estado):
        self.estado = estado

    def ganaste(self):
        return self.estado

    def tengo_ai(self):
        res = False
        if(self.inteligencia != None):
            res=True
        return res

    def ai_play(self, estado_actual):
        posicion = self.inteligencia.siguiente_estado(estado_actual)
        return posicion

    def aprender(self, resultado_game):
        if(self.inteligencia != None):
            if(self.estado==True):
                self.inteligencia.aplicar_recompensa(5)
            elif(resultado_game=="Empate"):
                self.inteligencia.aplicar_recompensa(-2)
            else:
                self.inteligencia.aplicar_recompensa(-5)

    def reset(self):
        self.estado=False
        self.inteligencia.vaciar_acciones()

    def set_aprendizaje(self, tabla):
        if self.inteligencia != None:
            self.inteligencia.set_aprendizaje(tabla)

    def get_inteligencia(self):
        return self.inteligencia.get_aprendizaje()