from re import search as rsrch, escape as resc
from busquedas import posDePzaEnTab
from inicio import crearMatriz

def moverPzaEnTab(tablero, ficha, ant, pos, origen):
	if origen == 0:
		origen = posDePzaEnTab(tablero,ficha)
	x = int(origen[0])
	y = int(origen[1])
	tablero[x][y] = ant

	x = int(pos[0])
	y = int(pos[1])
	tablero[x][y] = ficha

	return tablero

def reporMata(tablero, pos, jug):
	x = int(pos[0])
	y = int(pos[1])

	vector = list()
	vector.append( reporOps(tablero,x-1,y,jug) )
	vector.append( reporOps(tablero,x,y+1,jug) )
	vector.append( reporOps(tablero,x+1,y,jug) )
	vector.append( reporOps(tablero,x,y-1,jug) )

	count = 0
	for i in vector:
		if i == '-':
			count += 1
	for i in range(count):
		vector.remove('-')			

	return vector

def reporOps(tablero,A,B,jug):
	if A > 8 or B > 8 or A < 0 or B < 0:
		return '-'

	if tablero[A][B] != '' and tablero[A][B] != '0':
		if tablero[A][B][0] != str(jug):
			return str(A)+str(B)
	return '-'

def colocarPza(tablero):
	vector = list()
	for i in range(9):
		for j in range(9):
			if tablero[i][j] == '':
				if i == 4 and j == 4:
					continue
				else:
					vector.append(str(i) + str(j))
	return vector

def posiblesDestinos(tablero, ficha, origen):
	if ficha[1] == "N":
		P = 0
	elif ficha[1] == "R":
		P = 1
	elif ficha[1] == "C":
		P = 2
	elif ficha[1] == "M":
		P = 3
	else:
		P = 4

	if origen == 0:
		origen = posDePzaEnTab(tablero,ficha)
	x = int(origen[0])
	y = int(origen[1])

	if tablero[x][y] == ficha:
		return ( horizontal(tablero,ficha[0],P, x, y+1, 9, 1) + horizontal(tablero,ficha[0],P, x, y-1, -1, -1) +
		vertical(tablero,ficha[0],P, x+1, y, 9, 1) + vertical(tablero,ficha[0],P, x-1, y, -1, -1) +
		diagonal(tablero,ficha[0],P, x+1, y+1, 9, 1, 9, 1) + diagonal(tablero,ficha[0],P, x-1, y-1, -1, -1, -1, -1) +
		diagonal(tablero,ficha[0],P, x-1, y+1, -1, -1, 9, 1) + diagonal(tablero,ficha[0],P, x+1, y-1, 9, 1, -1, -1) )
	else:
		return []

def horizontal(tablero, jug, pieza, x, y, tope, sig):
	vector = list()
	contador = 0
	for j in range(y,tope,sig):
		if pieza == 3 and contador == 2:
			break

		if rsrch(r'[1-4]', tablero[x][j]):
			if rsrch(r'' + jug, tablero[x][j]) or pieza == 1 or pieza == 0:
				break
			else:
				if x == 4 and j == 4 and pieza == 3:
					break
				pos = str(x)+str(j)
				vector.append(pos)
				break
		elif rsrch(r'[0]',tablero[x][j]):
			if pieza == 0:
				pos = str(x)+str(j)
				vector.append(pos)
				break
			else:
				break
		else:
			if x == 4 and j == 4:
				if pieza == 2:
					pos = str(x)+str(j)
					vector.append(pos)
				else:
					continue
			else:
				pos = str(x)+str(j)
				vector.append(pos)

		contador += 1
	return vector

def vertical(tablero, jug, pieza, x, y, tope, sig):
	vector = list()
	contador = 0
	for i in range(x,tope,sig):
		if pieza == 3 and contador == 2:
			break

		if rsrch(r'[1-4]', tablero[i][y]):
			if rsrch(r'' + jug, tablero[i][y]) or pieza == 1 or pieza == 0:
				break
			else:
				if i == 4 and y == 4 and pieza == 3:
					break
				pos = str(i)+str(y)
				vector.append(pos)
				break
		elif rsrch(r'[0]',tablero[i][y]):
			if pieza == 0:
				pos = str(i)+str(y)
				vector.append(pos)
				break
			else:
				break
		else:
			if i == 4 and y == 4:
				if pieza == 2:
					pos = str(i)+str(y)
					vector.append(pos)					
				else:
					continue
			else:
				pos = str(i)+str(y)
				vector.append(pos)

		contador += 1
	return vector

def diagonal(tablero, jug, pieza, x, y, tope, sig, tope_, sig_):
	vector = list()
	contador = 0
	for i,j in zip( range(x,tope,sig) , range(y,tope_,sig_) ):
		if pieza == 3 and contador == 2:
			break

		if rsrch(r'[1-4]', tablero[i][j]):
			if rsrch(r'' + jug, tablero[i][j]) or pieza == 1 or pieza == 0:
				break
			else:
				if i == 4 and j == 4 and pieza == 3:
					break
				pos = str(i)+str(j)
				vector.append(pos)
				break
		elif rsrch(r'[0]',tablero[i][j]):
			if pieza == 0:
				pos = str(i)+str(j)
				vector.append(pos)
				break
			else:
				break
		else:
			if i == 4 and j == 4:
				if pieza == 2:
					pos = str(i)+str(j)
					vector.append(pos)					
				else:
					continue
			else:
				pos = str(i)+str(j)
				vector.append(pos)

		contador += 1
	return vector