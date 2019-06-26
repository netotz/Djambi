from re import search as rsrch

class Player:
	def __init__(jug, x, tablero):
		jug.num = x
		jug.piezas = guardarPiezas(x, tablero)

	jefe = True
	necro = True
	cerrado = False
	presi = False

def guardarPiezas(num, tablero):
	vector = list()
	for i in range(9):
		for j in range(9):
			if rsrch(r'' + str(num), tablero[i][j]):
				ficha = tablero[i][j]
				vector.append(ficha[1])
	return vector