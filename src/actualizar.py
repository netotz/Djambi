from inicio import crearMatriz
from re import search as rsrch, escape as resc
from validaciones import *
from jugador import *
from busquedas import posDePzaEnTab

def propiedades(jugadores, tablero):
	for jug in jugadores:
		jug.piezas = guardarPiezas(jug.num, tablero)

	for jug in jugadores:
		jug.jefe = False
		jug.necro = False
		for p in jug.piezas:
			if p == 'C':
				jug.jefe = True
			elif p == 'N':
				jug.necro = True

			if jug.jefe and jug.necro:
				break

	return jugadores

def encerrado(tablero, jug):
	pos = posDePzaEnTab(tablero, str(jug) + 'C')
	x = int(pos[0])
	y = int(pos[1])

	for i in range(x-1,x+2):
		for j in range(y-1,y+2):
			print(i,j)
			if (i == x and j == y) or i < 0 or i > 8 or j < 0 or j > 8:
				continue
			if tablero[i][j] != '0':
				return False
	return True

def pasarPiezas(tablero, jug_nuevo, jug_muerto):
	for i in range(9):
		for j in range(9):
			ficha = tablero[i][j]
			if ficha != '' and ficha != '0':
				pieza = ficha[1]
				if ficha[0] == jug_muerto:
					tablero[i][j] = jug_nuevo + pieza
	return tablero

def pedirPieza():
	pza = input("\tIngresar letra de pieza a mover: ")
	if validPza(pza):
		return pza
	else:
		print("\t\tEntrada no válida.\n\t\tSolo letras presentes en el tablero.\n")
		return pedirPieza()
	
def especificar(tipo):
	print("\tEspecifique la casilla donde se encuentra la pieza que quiere ", end='')
	if tipo == 0:
		print("matar: ", end='')
	else:
		print("mover: ", end='')
	coord = input()

	if validCoord(coord):
		return coord
	else:
		print("\t\tEntrada no válida.\n\t\tSolo coordenadas numéricas de 00 a 88.\n")
		return especificar(tipo)

def pedirCasilla(tipo, letra):
	print("\tColocar ", end='')
	if tipo == 0:
		print("la ficha muerta ", end='')
	else:
		print("la pieza",letra,"", end='')

	pos = input("en la casilla: ")
	if validCoord(pos):
		return str(pos)
	else:
		print("\t\tEntrada no válida.\n\t\tSolo coordenadas numéricas de 00 a 88.\n")
		return pedirCasilla(tipo, letra)