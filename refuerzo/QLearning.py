class QLearning:
    estado_actual=None  ##
    valor_aprendizaje=0
    factor_descuento=0

    acciones=None
    tabla_aprendizaje=None

    def __init__(self):
        self.tabla_aprendizaje=[[0.0, 0.0, 0.0],
                                [0.0, 0.0, 0.0],
                                [0.0, 0.0, 0.0]]
        self.acciones=[]
        self.valor_aprendizaje=0.9
        self.factor_descuento=0.1

    def buscar_valor(self, pocision_tablero):
        res = self.tabla_aprendizaje[pocision_tablero[0]],[pocision_tablero[1]]
        return res

    def siguiente_estado(self,tablero):
        res = None
        for i in range(0,3):
            for j in range(0,3):
                if(tablero[i][j].marcado==False):
                    valor_movimiento=self.tabla_aprendizaje[i][j]
                    if(res==None):
                        res=(i,j)
                    elif(valor_movimiento > self.tabla_aprendizaje[res[0]][res[1]]):
                        res=(i,j)
        self.acciones.append(res)
        return res

    def aplicar_recompensa(self, recompensa):
        print(recompensa)
        pocision=self.acciones[0]
        self.tabla_aprendizaje[pocision[0]][pocision[1]] = self.tabla_aprendizaje[pocision[0]][pocision[1]]+self.valor_aprendizaje*(1+self.factor_descuento*self.aplicarRecompensa(1,recompensa))
        self.imprimir_entrenamiento()

    def vaciar_acciones(self):
        self.acciones = []

    def aplicarRecompensa(self,index ,recompensa):
        if(index==len(self.acciones)):
            res = recompensa
        else:
            pocision = self.acciones[index]
            value = self.tabla_aprendizaje[pocision[0]][pocision[1]]+self.valor_aprendizaje*(1+self.factor_descuento*self.aplicarRecompensa(index+1,recompensa))
            self.tabla_aprendizaje[pocision[0]][pocision[1]]=value
            res = self.tabla_aprendizaje[pocision[0]][pocision[1]]
        return res

    def imprimir_entrenamiento(self):
        res=''
        for i in range(0,3):
            for j in range(0,3):
                res=res+str(self.tabla_aprendizaje[i][j])+'  '
            res=res+'\n'
        print(res)

    def set_aprendizaje(self, matriz):
        self.tabla_aprendizaje = matriz

    def get_aprendizaje(self):
        return self.tabla_aprendizaje