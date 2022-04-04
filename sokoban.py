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

  #Derecha
  00 - Personaje, espacio -> [5,0] -> [0,5] 
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

  #Abajo
  12 - Espacio, personaje -> [0,5] -> [5.0]

  Derecha -> personaje_columna + 1
  Izquierda -> personaje_columna -1
  Abajo -> personaje_fila + 1
  Arriba -> personaje_fila - 1
  """
  
  mapa = [
      [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      [1,5,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
      [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1],
      [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,1],
      [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,1],
      [0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,3,1],
      [0,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0],
      [0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
      [0,0,1,0,4,0,0,0,0,0,0,1,0,0,4,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
      [0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
      [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0],
      [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
      [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
      [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],    
  ]

  #Posicion inicial del personaje en el mapa
  personaje_columna = 1
  personaje_fila = 1

  def imprimirMapa(self):
    """Imprime el mapa completo
    """
    for fila in self.mapa:
        print(fila)

  def moverDerecha(self):
    """Controla el movimiento del personaje a la derecha
    """
    #00 - Personaje, espacio -> [5,0] -> [0,5]
    if self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 0:
      self.mapa[self.personaje_fila][self.personaje_columna] = 0
      self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
      self.personaje_columna += 1

  def moverAbajo(self):
    """Controla el movimiento del muñeco hacia abajo
    12 -> [0]
    [0] -> [5]
    [5] -> [0]
    """
    #12 - Espacio, personaje -> [0,5] -> [0,5]
    if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 5:
      self.mapa[self.personaje_fila][self.personaje_columna] = 5
      self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
      self.personaje_fila -= 1

  def jugar(self):
    """Controla el flujo del juego
    """
    while True:
      self.imprimirMapa()
      opciones = "d-derecha, s-abajo"
      print(opciones)
      movimiento = input("Mover a: ")
      if movimiento == "d":
        self.moverDerecha()
      elif movimiento == "s":
        self.moverAbajo()
      elif movimiento == "q":
        break

juego = Sokoban()
juego.jugar()