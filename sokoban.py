class Sokoban:
    """
  5 - Personaje
  0 - Espacio
  4 - Caja
  1 - Pared
  3 - Meta
  8 - Personaje_meta
  7 - Caja_meta
   
Reglas validas para moverse (Arriba, Derecha, Abajo, Izquierda)

  
  00 - Personaje, espacio 
  01 - Personaje, meta 
  02 - Personaje, caja, espacio 
  03 - Personaje, caja, meta 
  04 - Personaje, caja_meta, espacio 
  05 - Personaje, caja_meta, meta 
  06 - Personaje_meta, espacio 
  07 - Personaje_meta, meta 
  08 - Personaje_meta, caja, espacio  
  09 - Personaje_meta, caja, meta 
  10 - Personaje_meta, caja_meta, espacio 
  11 - Personaje_meta, caja_meta, meta 


  Derecha -> personaje_columna + 1
  Izquierda -> personaje_columna -1
  Abajo -> personaje_fila + 1
  Arriba -> personaje_fila - 1
    """

    mapa = []
    personaje_columna = 0
    personaje_fila = 0
    nivel = open("prueba.txt","r")

    def __init__(self):
        pass

    def cargarMapa(self):
        for ghy in self.nivel:
            columna = []
            for digito in ghy:
                if digito == "\n":
                    continue
                columna.append(int(digito))
            self.mapa.append(columna)

    
    def imprimirMapa(self):
        for fila in self.mapa:
            print(fila)

    def posPer(self):
        for linea in range(len(self.mapa)):
            for columna in range (len(self.mapa))
        
    
    def moverDerecha(self):
        """Controla el movimiento del personaje a la derecha
    """
        #00 - Personaje, espacio -> [5,0] -> [0,5]
        if self.mapa[self.personaje_fila][
                self.personaje_columna] == 5 and self.mapa[
                    self.personaje_fila][self.personaje_columna + 1] == 0:
            print("MovDer:Personaje, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 0
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.personaje_columna = self.personaje_columna + 1
        #01 -Personaje, meta -> [5,3] -> [0,8]
        elif self.mapa[self.personaje_fila][
                self.personaje_columna] == 5 and self.mapa[
                    self.personaje_fila][self.personaje_columna + 1] == 3:
            print("MovDer:Personaje, meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 0
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 8
            self.personaje_columna = self.personaje_columna + 1
        #02 - Personaje, caja, espacio -> [5,4,0] -> [0,5,4]
        elif self.mapa[self.personaje_fila][
                self.
                personaje_columna] == 5 and self.mapa[self.personaje_fila][
                    self.personaje_columna + 1] == 4 and self.mapa[
                        self.personaje_fila][self.personaje_columna + 2] == 0:
            print("MovDer:Personaje, caja, espacio ")
            self.mapa[self.personaje_fila][self.personaje_columna] = 0
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 4
            self.personaje_columna = self.personaje_columna + 1
        #03 - Personaje, caja, meta -> [5,4,3] -> [0,5,7]
        elif self.mapa[self.personaje_fila][
                self.
                personaje_columna] == 5 and self.mapa[self.personaje_fila][
                    self.personaje_columna + 1] == 4 and self.mapa[
                        self.personaje_fila][self.personaje_columna + 2] == 3:
            print("MovDer:Personaje, caja, meta ")
            self.mapa[self.personaje_fila][self.personaje_columna] = 0
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 7
            self.personaje_columna = self.personaje_columna + 1
        #04 - Personaje, caja_meta, espacio -> [5,7,0] -> [0,8,4]
        elif self.mapa[self.personaje_fila][
                self.
                personaje_columna] == 5 and self.mapa[self.personaje_fila][
                    self.personaje_columna + 1] == 7 and self.mapa[
                        self.personaje_fila][self.personaje_columna + 2] == 0:
            print("MovDer:Personaje, caja_meta, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 0
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 8
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 4
            self.personaje_columna = self.personaje_columna + 1
        #05 - Personaje, caja_meta, meta -> [5,7,3] -> [0,8,7]
        elif self.mapa[self.personaje_fila][
                self.
                personaje_columna] == 5 and self.mapa[self.personaje_fila][
                    self.personaje_columna + 1] == 7 and self.mapa[
                        self.personaje_fila][self.personaje_columna + 2] == 3:
            print("MovDer:Personaje, caja_meta, meta ")
            self.mapa[self.personaje_fila][self.personaje_columna] = 0
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 8
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 7
            self.personaje_columna = self.personaje_columna + 1
        #06 -Personaje_meta, espacio -> [8,0] -> [3,5]
        elif self.mapa[self.personaje_fila][
                self.personaje_columna] == 8 and self.mapa[
                    self.personaje_fila][self.personaje_columna + 1] == 0:
            print("MovDer:Personaje_meta, espacio ")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.personaje_columna = self.personaje_columna + 1
        #07 -Personaje_meta, meta -> [8,3] -> [3,8]
        elif self.mapa[self.personaje_fila][
                self.personaje_columna] == 8 and self.mapa[
                    self.personaje_fila][self.personaje_columna + 1] == 3:
            print("MovDer:Personaje_meta, meta  ")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 8
            self.personaje_columna = self.personaje_columna + 1
        #08 - Personaje_meta, caja, espacio -> [8,4,0] -> [3,5,4]
        elif self.mapa[self.personaje_fila][
                self.
                personaje_columna] == 8 and self.mapa[self.personaje_fila][
                    self.personaje_columna + 1] == 4 and self.mapa[
                        self.personaje_fila][self.personaje_columna + 2] == 0:
            print("MovDer:Personaje_meta, caja, espacio ")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 4
            self.personaje_columna = self.personaje_columna + 1
        #09 - Personaje_meta, caja, meta -> [8,4,3] -> [3,8,7]
        elif self.mapa[self.personaje_fila][
                self.
                personaje_columna] == 8 and self.mapa[self.personaje_fila][
                    self.personaje_columna + 1] == 4 and self.mapa[
                        self.personaje_fila][self.personaje_columna + 2] == 3:
            print("MovDer: Personaje_meta, caja, meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 8
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 7
            self.personaje_columna = self.personaje_columna + 1
        #10 - Personaje_meta, caja_meta, espacio -> [8,7,0] -> [3,8,4]
        elif self.mapa[self.personaje_fila][
                self.
                personaje_columna] == 8 and self.mapa[self.personaje_fila][
                    self.personaje_columna + 1] == 7 and self.mapa[
                        self.personaje_fila][self.personaje_columna + 2] == 0:
            print("MovDer:Personaje_meta, caja_meta, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 8
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 4
            self.personaje_columna = self.personaje_columna + 1
        #11 - Personaje_meta, caja_meta, meta -> [8,7,3] -> [3,8,7]
        elif self.mapa[self.personaje_fila][
                self.
                personaje_columna] == 8 and self.mapa[self.personaje_fila][
                    self.personaje_columna + 1] == 7 and self.mapa[
                        self.personaje_fila][self.personaje_columna + 2] == 3:
            print("MovDer:Personaje_meta, caja_meta, meta ")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 8
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 7
            self.personaje_columna = self.personaje_columna + 1

    def moverIzquierda(self):
        """controla el movimiento del personaje hacia la izquiera
    """
        #00 - Personaje, espacio -> [0,5] -> [5,0]
        if self.mapa[self.personaje_fila][
                self.personaje_columna] == 5 and self.mapa[
                    self.personaje_fila][self.personaje_columna - 1] == 0:
            print("MovIzq:Personaje, espacio ")
            self.mapa[self.personaje_fila][self.personaje_columna] = 0
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.personaje_columna = self.personaje_columna - 1
        #01 - Personaje, meta -> [3,5] -> [8,0]
        elif self.mapa[self.personaje_fila][
                self.personaje_columna] == 5 and self.mapa[
                    self.personaje_fila][self.personaje_columna - 1] == 3:
            print("MovIzq:Personaje, meta ")
            self.mapa[self.personaje_fila][self.personaje_columna] = 0
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 8
            self.personaje_columna = self.personaje_columna - 1
        #02 - Personaje, caja, espacio -> [0,4,5] -> [4,5,0]
        elif self.mapa[self.personaje_fila][
                self.
                personaje_columna] == 5 and self.mapa[self.personaje_fila][
                    self.personaje_columna - 1] == 4 and self.mapa[
                        self.personaje_fila][self.personaje_columna - 2] == 0:
            print("MovIzq: Personaje, caja, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 0
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 4
            self.personaje_columna = self.personaje_columna - 1
        #03 - Personaje, caja, meta -> [3,4,5] -> [7,5,0]
        elif self.mapa[self.personaje_fila][
                self.
                personaje_columna] == 5 and self.mapa[self.personaje_fila][
                    self.personaje_columna - 1] == 4 and self.mapa[
                        self.personaje_fila][self.personaje_columna - 2] == 3:
            print("MovIzq:Personaje, caja, meta ")
            self.mapa[self.personaje_fila][self.personaje_columna] = 0
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 7
            self.personaje_columna = self.personaje_columna - 1
        #04 - Personaje, caja_meta, espacio -> [0,7,5] -> [4,8,0]
        elif self.mapa[self.personaje_fila][
                self.
                personaje_columna] == 5 and self.mapa[self.personaje_fila][
                    self.personaje_columna - 1] == 7 and self.mapa[
                        self.personaje_fila][self.personaje_columna - 2] == 0:
            print("MovIzq:Personaje, caja_meta, espacio ")
            self.mapa[self.personaje_fila][self.personaje_columna] = 0
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 8
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 4
            self.personaje_columna = self.personaje_columna - 1
        #05 - Personaje, caja_meta, meta -> [3,7,5] -> [7,8,0]
        elif self.mapa[self.personaje_fila][
                self.
                personaje_columna] == 5 and self.mapa[self.personaje_fila][
                    self.personaje_columna - 1] == 7 and self.mapa[
                        self.personaje_fila][self.personaje_columna - 2] == 3:
            print("MovIzq:Personaje, caja_meta, meta ")
            self.mapa[self.personaje_fila][self.personaje_columna] = 0
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 8
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 7
            self.personaje_columna = self.personaje_columna - 1
        #06 - Personaje_meta, espacio -> [0,8] -> [5,3]
        elif self.mapa[self.personaje_fila][
                self.personaje_columna] == 8 and self.mapa[
                    self.personaje_fila][self.personaje_columna - 1] == 0:
            print("MovIzq:Personaje_meta, espacio ")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.personaje_columna = self.personaje_columna - 1
        #07 - Personaje_meta, meta -> [3,8] -> [8,3]
        elif self.mapa[self.personaje_fila][
                self.personaje_columna] == 8 and self.mapa[
                    self.personaje_fila][self.personaje_columna - 1] == 3:
            print("MovIzq:Personaje_meta, meta ")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 8
            self.personaje_columna = self.personaje_columna - 1
        #08 - Personaje_meta, caja, espacio -> [0,4,8] -> [4,5,3]
        elif self.mapa[self.personaje_fila][
                self.
                personaje_columna] == 8 and self.mapa[self.personaje_fila][
                    self.personaje_columna - 1] == 4 and self.mapa[
                        self.personaje_fila][self.personaje_columna - 2] == 0:
            print("MovIzq:Personaje_meta, caja, espacio ")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 4
            self.personaje_columna = self.personaje_columna - 1
        #09 - Personaje_meta, caja, meta -> [3,4,8] -> [7,8,3]
        elif self.mapa[self.personaje_fila][
                self.
                personaje_columna] == 8 and self.mapa[self.personaje_fila][
                    self.personaje_columna - 1] == 4 and self.mapa[
                        self.personaje_fila][self.personaje_columna - 2] == 3:
            print("MovIzq:Personaje_meta, caja, meta  ")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 8
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 7
            self.personaje_columna = self.personaje_columna - 1
        #10 - Personaje_meta, caja_meta, espacio -> [0,7,8] -> [4,8,3]
        elif self.mapa[self.personaje_fila][
                self.
                personaje_columna] == 8 and self.mapa[self.personaje_fila][
                    self.personaje_columna - 1] == 7 and self.mapa[
                        self.personaje_fila][self.personaje_columna - 2] == 0:
            print("MovIzq:Personaje_meta, caja_meta, espacio ")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 8
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 4
            self.personaje_columna = self.personaje_columna - 1
        #11 - Personaje_meta, caja_meta, meta -> [3,7,8] -> [7,8,3]
        elif self.mapa[self.personaje_fila][
                self.
                personaje_columna] == 8 and self.mapa[self.personaje_fila][
                    self.personaje_columna - 1] == 7 and self.mapa[
                        self.personaje_fila][self.personaje_columna - 2] == 3:
            print("MovIzq:Personaje_meta, caja_meta, meta ")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 8
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 7
            self.personaje_columna = self.personaje_columna - 1

    def moverAbajo(self):
        """Controla el movimiento del muñeco hacia abajo
    """
        #00 - Personaje, espacio -> [5,0] -> [0,5]
        if self.mapa[self.personaje_fila][
                self.personaje_columna] == 5 and self.mapa[
                    self.personaje_fila + 1][self.personaje_columna] == 0:
            print("MovAbaj: Personaje, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 0
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
            self.personaje_fila = self.personaje_fila + 1
        #01 - Personaje, meta -> [5,3] -> [0,8]
        elif self.mapa[self.personaje_fila][
                self.personaje_columna] == 5 and self.mapa[
                    self.personaje_fila + 1][self.personaje_columna] == 3:
            print("MovAbaj: Personaje, meta ")
            self.mapa[self.personaje_fila][self.personaje_columna] = 0
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 8
            self.personaje_fila = self.personaje_fila + 1
        #02 - Personaje, caja, espacio -> [5,4,0] -> [0,5,4]
        elif self.mapa[self.personaje_fila][
                self.personaje_columna] == 5 and self.mapa[
                    self.personaje_fila +
                    1][self.personaje_columna] == 4 and self.mapa[
                        self.personaje_fila + 2][self.personaje_columna] == 0:
            print("MovAbaj: Personaje, caja, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 0
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 4
            self.personaje_fila = self.personaje_fila + 1
        #03 - Personaje, caja, meta -> [5,4,3] -> [0,5,7]
        elif self.mapa[self.personaje_fila][
                self.personaje_columna] == 5 and self.mapa[
                    self.personaje_fila +
                    1][self.personaje_columna] == 4 and self.mapa[
                        self.personaje_fila + 2][self.personaje_columna] == 3:
            print("MovAbaj: Personaje, caja, meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 0
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 7
            self.personaje_fila = self.personaje_fila + 1
        #04 - Personaje, caja_meta, espacio -> [5,7,0] -> [0,8,4]
        elif self.mapa[self.personaje_fila][
                self.personaje_columna] == 5 and self.mapa[
                    self.personaje_fila +
                    1][self.personaje_columna] == 7 and self.mapa[
                        self.personaje_fila + 2][self.personaje_columna] == 0:
            print("MovAbaj: Personaje, caja_meta, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 0
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 8
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 4
            self.personaje_fila = self.personaje_fila + 1
        #05 - Personaje, caja_meta, meta -> [5,7,3] -> [0,8,7]
        elif self.mapa[self.personaje_fila][
                self.personaje_columna] == 5 and self.mapa[
                    self.personaje_fila +
                    1][self.personaje_columna] == 7 and self.mapa[
                        self.personaje_fila + 2][self.personaje_columna] == 3:
            print("MovAbaj: Personaje, caja_meta, meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 0
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 8
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 7
            self.personaje_fila = self.personaje_fila + 1
        #06 - Personaje_meta, espacio -> [8,0] -> [3,5]
        elif self.mapa[self.personaje_fila][
                self.personaje_columna] == 8 and self.mapa[
                    self.personaje_fila + 1][self.personaje_columna] == 0:
            print("MovAbaj: Personaje_meta, espacio ")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
            self.personaje_fila = self.personaje_fila + 1
        #07 - Personaje_meta, meta -> [8,3] -> [3,8]
        elif self.mapa[self.personaje_fila][
                self.personaje_columna] == 8 and self.mapa[
                    self.personaje_fila + 1][self.personaje_columna] == 3:
            print("MovAbaj: Personaje_meta, meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 8
            self.personaje_fila = self.personaje_fila + 1
        #08 - Personaje_meta, caja, espacio -> [8,4,0] -> [3,5,4]
        elif self.mapa[self.personaje_fila][
                self.personaje_columna] == 8 and self.mapa[
                    self.personaje_fila +
                    1][self.personaje_columna] == 4 and self.mapa[
                        self.personaje_fila + 2][self.personaje_columna] == 0:
            print("MovAbaj: Personaje_meta, caja, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 4
            self.personaje_fila = self.personaje_fila + 1
        #09 - Personaje_meta, caja, meta -> [8,4,3] -> [3,8,7]
        elif self.mapa[self.personaje_fila][
                self.personaje_columna] == 8 and self.mapa[
                    self.personaje_fila +
                    1][self.personaje_columna] == 4 and self.mapa[
                        self.personaje_fila + 2][self.personaje_columna] == 3:
            print("MovAbaj: Personaje_meta, caja, meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 8
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 7
            self.personaje_fila = self.personaje_fila + 1
        #10 - Personaje_meta, caja_meta, espacio -> [8,7,0] -> [3,8,4]
        elif self.mapa[self.personaje_fila][
                self.personaje_columna] == 8 and self.mapa[
                    self.personaje_fila +
                    1][self.personaje_columna] == 7 and self.mapa[
                        self.personaje_fila + 2][self.personaje_columna] == 0:
            print("MovAbaj: Personaje_meta, caja_meta, espacio")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 8
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 4
            self.personaje_fila = self.personaje_fila + 1
        #11 - Personaje_meta, caja_meta, meta -> [8,7,3] -> [3,8,7]
        elif self.mapa[self.personaje_fila][
                self.personaje_columna] == 8 and self.mapa[
                    self.personaje_fila +
                    1][self.personaje_columna] == 7 and self.mapa[
                        self.personaje_fila + 2][self.personaje_columna] == 3:
            print("MovAbaj: Personaje_meta, caja_meta, meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 8
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 7
            self.personaje_fila = self.personaje_fila + 1

    def moverArriba(self):
        """Controla el movimiento del muñeco hacia arriba
    """
        #00 - Espacio, personaje -> [0,5] -> [5,0]
        if self.mapa[self.personaje_fila][
                self.personaje_columna] == 5 and self.mapa[
                    self.personaje_fila - 1][self.personaje_columna] == 0:
            print("MovArrib: Espacio, personaje")
            self.mapa[self.personaje_fila][self.personaje_columna] = 0
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.personaje_fila = self.personaje_fila - 1
        #01 - Meta, personaje -> [3,5] -> [8,0]
        elif self.mapa[self.personaje_fila][
                self.personaje_columna] == 5 and self.mapa[
                    self.personaje_fila - 1][self.personaje_columna] == 3:
            print("MovArrib: Meta, personaje")
            self.mapa[self.personaje_fila][self.personaje_columna] = 0
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 8
            self.personaje_fila = self.personaje_fila - 1
        #02 - Espacio, caja, personaje -> [0,4,5] -> [4,5,0]
        elif self.mapa[self.personaje_fila][
                self.personaje_columna] == 5 and self.mapa[
                    self.personaje_fila -
                    1][self.personaje_columna] == 4 and self.mapa[
                        self.personaje_fila - 2][self.personaje_columna] == 0:
            print("MovArrib: Espacio, caja, personaje")
            self.mapa[self.personaje_fila][self.personaje_columna] = 0
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 4
            self.personaje_fila = self.personaje_fila - 1
        #03 - Meta, caja, personaje -> [3,4,5] -> [7,5,0]
        elif self.mapa[self.personaje_fila][
                self.personaje_columna] == 5 and self.mapa[
                    self.personaje_fila -
                    1][self.personaje_columna] == 4 and self.mapa[
                        self.personaje_fila - 2][self.personaje_columna] == 3:
            print("MovArrib: Meta, caja, personaje")
            self.mapa[self.personaje_fila][self.personaje_columna] = 0
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 7
            self.personaje_fila = self.personaje_fila - 1
        #04 - Espacio, caja_meta, personaje -> [0,7,5] -> [4,8,0]
        elif self.mapa[self.personaje_fila][
                self.personaje_columna] == 5 and self.mapa[
                    self.personaje_fila -
                    1][self.personaje_columna] == 7 and self.mapa[
                        self.personaje_fila - 2][self.personaje_columna] == 0:
            print("MovArrib: Espacio, caja_meta, personaje")
            self.mapa[self.personaje_fila][self.personaje_columna] = 0
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 8
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 4
            self.personaje_fila = self.personaje_fila - 1
        #05 - Meta, caja_meta, personaje -> [3,7,5] -> [7,8,0]
        elif self.mapa[self.personaje_fila][
                self.personaje_columna] == 5 and self.mapa[
                    self.personaje_fila -
                    1][self.personaje_columna] == 7 and self.mapa[
                        self.personaje_fila - 2][self.personaje_columna] == 3:
            print("MovArrib: Meta, caja_meta, personaje")
            self.mapa[self.personaje_fila][self.personaje_columna] = 0
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 8
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 7
            self.personaje_fila = self.personaje_fila - 1
        #06 - Espacio, personaje_meta -> [0,8] -> [5,3]
        elif self.mapa[self.personaje_fila][
                self.personaje_columna] == 8 and self.mapa[
                    self.personaje_fila - 1][self.personaje_columna] == 0:
            print("MovArrib: Espacio, personaje_meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.personaje_fila = self.personaje_fila - 1
        #07 - Meta, personaje_meta -> [3,8] -> [8,3]
        elif self.mapa[self.personaje_fila][
                self.personaje_columna] == 8 and self.mapa[
                    self.personaje_fila - 1][self.personaje_columna] == 3:
            print("MovArrib: Meta, personaje_meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 8
            self.personaje_fila = self.personaje_fila - 1
        #08 - Espacio, caja, personaje_meta -> [0,4,8] -> [4,5,3]
        elif self.mapa[self.personaje_fila][
                self.personaje_columna] == 8 and self.mapa[
                    self.personaje_fila -
                    1][self.personaje_columna] == 4 and self.mapa[
                        self.personaje_fila - 2][self.personaje_columna] == 0:
            print("MovArrib: Espacio, caja, personaje_meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 4
            self.personaje_fila = self.personaje_fila - 1
        #09 - Espacio, caja, personaje_meta -> [0,4,8] -> [4,5,3]
        elif self.mapa[self.personaje_fila][
                self.personaje_columna] == 8 and self.mapa[
                    self.personaje_fila -
                    1][self.personaje_columna] == 4 and self.mapa[
                        self.personaje_fila - 2][self.personaje_columna] == 0:
            print("MovArrib: Espacio, caja, personaje_meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 4
            self.personaje_fila = self.personaje_fila - 1
        #09 - Meta, caja, personaje_meta -> [3,4,8] -> [7,5,3]
        elif self.mapa[self.personaje_fila][
                self.personaje_columna] == 8 and self.mapa[
                    self.personaje_fila -
                    1][self.personaje_columna] == 4 and self.mapa[
                        self.personaje_fila - 2][self.personaje_columna] == 3:
            print("MovArrib: Meta, caja, personaje_meta ")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 7
            self.personaje_fila = self.personaje_fila - 1
        #10 - Espacio, caja_meta, personaje_meta -> [0,7,8] -> [4,8,3]
        elif self.mapa[self.personaje_fila][
                self.personaje_columna] == 8 and self.mapa[
                    self.personaje_fila -
                    1][self.personaje_columna] == 7 and self.mapa[
                        self.personaje_fila - 2][self.personaje_columna] == 0:
            print("MovArrib: Espacio, caja_meta, personaje_meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 8
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 4
            self.personaje_fila = self.personaje_fila - 1
        #11 - Meta, caja_meta, personaje_meta -> [3,7,8] -> [7,8,3]
        elif self.mapa[self.personaje_fila][
                self.personaje_columna] == 8 and self.mapa[
                    self.personaje_fila -
                    1][self.personaje_columna] == 7 and self.mapa[
                        self.personaje_fila - 2][self.personaje_columna] == 3:
            print("MovArrib: Meta, caja_meta, personaje_meta")
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 8
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 7
            self.personaje_fila = self.personaje_fila - 1

    def jugar(self):
        """Controla el flujo del juego
    """
        while True:
            self.cargarMapa()
            self.imprimirMapa()
            opciones = "d-derecha, s-abajo, a-izquierda, w-arriba, q-salir"
            print(opciones)
            movimiento = input("Mover a: ")
            if movimiento == "d":
                self.moverDerecha()
            elif movimiento == "s":
                self.moverAbajo()
            elif movimiento == "a":
                self.moverIzquierda()
            elif movimiento == "w":
                self.moverArriba()
            elif movimiento == "q":
                break
juego = Sokoban()
juego.jugar()