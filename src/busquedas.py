def posDePzaEnTab(tablero, ficha):
	for i in range(9):
		for j in range(9):
			if ficha == tablero[i][j]:
				return str(i)+str(j)

def jugTienePza(vector, pieza):
	cantidad = 0
	for p in vector:
		if p == pieza:
			cantidad += 1
	return cantidad

def validMov(arreglo, pos):
	for x in arreglo:
		if pos == x:
			return True
	return False