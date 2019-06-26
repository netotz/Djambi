from jugador import *

def crearJugadores(tablero):
	jugadores = list()
	for i in range(1,5):
		jugadores.append( Player(i, tablero) )
	return jugadores

def crearMatriz(char, fil, col):
	matriz = [[char for j in range(col)] for i in range (fil)]
	return matriz

def inicializarTablero():
	tablero = crearMatriz("",9,9)
	jug = 4
	for i in range(0,9,8):
		for j in range(0,9,8):
			P = str(jug)
			tablero[i][j] = P+"C"
			if i-1 < 0:
				if j-1 < 0:
					tablero[i][j+1] = P+"A"
					tablero[i][j+2] = P+"M"
					tablero[i+1][j+2] = P+"M"
					tablero[i+1][j+1] = P+"D"
					tablero[i+2][j+2] = P+"N"
					tablero[i+1][j] = P+"R"
					tablero[i+2][j] = P+"M"
					tablero[i+2][j+1] = P+"M"
				else:
					tablero[i][j-1] = P+"A"
					tablero[i][j-2] = P+"M"
					tablero[i+1][j-2] = P+"M"
					tablero[i+1][j-1] = P+"D"
					tablero[i+2][j-2] = P+"N"
					tablero[i+1][j] = P+"R"
					tablero[i+2][j] = P+"M"
					tablero[i+2][j-1] = P+"M"
			else:
				if j-1 < 0:
					tablero[i][j+1] = P+"A"
					tablero[i][j+2] = P+"M"
					tablero[i-1][j+2] = P+"M"
					tablero[i-1][j+1] = P+"D"
					tablero[i-2][j+2] = P+"N"
					tablero[i-1][j] = P+"R"
					tablero[i-2][j] = P+"M"
					tablero[i-2][j+1] = P+"M"
				else:
					tablero[i][j-1] = P+"A"
					tablero[i][j-2] = P+"M"
					tablero[i-1][j-2] = P+"M"
					tablero[i-1][j-1] = P+"D"
					tablero[i-2][j-2] = P+"N"
					tablero[i-1][j] = P+"R"
					tablero[i-2][j] = P+"M"
					tablero[i-2][j-1] = P+"M"
			if jug == 3:
				jug = 1
			elif jug == 1:
				jug = 2
			else:
				jug -= 1

	return tablero