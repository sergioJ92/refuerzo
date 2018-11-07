import os
import pathlib
import csv

class csvManager:
    nombre_file=""
    nombre_carpeta=""
    csvFile=""
    def __init__(self,listaJugadores):
        self.nombre_file = "Train.csv"
        self.nombre_carpeta = "train"
        self.crearFile()
        self.cargarAprendizaje(listaJugadores)

    def crearFile(self):
        archivos = os.listdir(self.nombre_carpeta)
        path = self.nombre_carpeta+"/"+self.nombre_file
        if not self.nombre_file in archivos:
            self.csvFile = open(path,'x')
            self.csvFile.close()

    def cargarAprendizaje(self,lista_jugadores):
        file = open(self.nombre_carpeta+"/"+self.nombre_file, 'r')
        if file.mode == 'r':
            files = file.readlines()
            for fila in files:
                vector = fila.replace("\n","")
                vector = vector.split(",")
                tabla_decimal = self.parcer_vector(vector)
                self.asignarAprendizaje(tabla_decimal, lista_jugadores)

    def asignarAprendizaje(self,lista_valores,jugadores):
        for jugador in jugadores:
            if jugador.tengo_ai():
                jugador.set_aprendizaje(lista_valores)

    def parcer_vector(self, vector):
        index = 0
        matriz=[]
        for i in range(0,3):
            array = []
            for j in range(0,3):
                cadena = vector[index]
                valor_decimal = float(cadena)
                array.append(valor_decimal)
                index = index + 1
            matriz.append(array)
        print(matriz)
        return matriz

    def guardarAprendizaje(self, jugadores):
        objetoCsv = open(self.nombre_carpeta+"/"+self.nombre_file, "w")
        for jugador in jugadores:
            if jugador.tengo_ai():
                matriz = jugador.get_inteligencia()
                for i in range(0, 3):
                    for j in range(0, 3):
                        objetoCsv.write(str(matriz[i][j]))
                        if not (i==2 and j==2):
                            objetoCsv.write(",")
                objetoCsv.write("\n")
        objetoCsv.close()

    #def parcerCsv(self):




