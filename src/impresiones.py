from re import search as rsrch
from os import system as sys
from colorama import *
init()

def imprimirTablero(tablero, jugadores):
	print("\t\t\t\t\tCada casilla es identificada con un número de dos cifras.")
	
	print("     ", end='')
	for x in range(9):
		print(x," ", end='')
	print("\tLa primera cifra es el número de la fila, y la segunda el de la columna.")

	print("   ┌", end='')
	for x in range(9):
		print("───", end='')
	print("\t\tNinguna pieza puede saltar otras piezas.")

	for i in range(9):
		print("",i,"│ ", end='')
		print(Style.BRIGHT, end='')
		for j in range(9):
			if rsrch(r"[1]",tablero[i][j]):
				if jugadores[0].cerrado:
					print(Fore.WHITE, end='')	
				else:
					print(Fore.RED, end='')
			elif rsrch(r"[2]",tablero[i][j]):
				if jugadores[1].cerrado:
					print(Fore.WHITE, end='')
				else:
					print(Fore.CYAN, end='')
			elif rsrch(r"[3]",tablero[i][j]):
				if jugadores[2].cerrado:
					print(Fore.WHITE, end='')
				else:
					print(Fore.YELLOW, end='')
			elif rsrch(r"[4]",tablero[i][j]):
				if jugadores[3].cerrado:
					print(Fore.WHITE, end='')
				else:
					print(Fore.GREEN, end='')	
			else:
				print(Fore.WHITE, end='')
				if tablero[i][j] == '0':
					print("†  ", end='')
				elif (i == 4 and j == 4) and tablero[4][4] == '':
					print("¤  ", end='')
				elif tablero[i][j] == '':
					print("■  ", end='')
				continue
			print(tablero[i][j][1]," ", end='')
		if i == 0:
			print(Style.RESET_ALL, end='')
			print("\tTodas las piezas pueden moverse en cualquier dirección y las casillas que sean,")
		if i == 1:
			print(Style.RESET_ALL, end='')
			print("\texcepto los Militantes, que solo pueden avanzar 2 casillas como máximo.")
		elif i == 2:
			print(Style.RESET_ALL, end='')
			print("\tSolo el Capitán puede ocupar la casilla central, la 44.")
		elif i == 3:
			print(Style.RESET_ALL, end='')
			print("\tEl Diplomático solo pueden mover piezas vivas.")
		elif i == 4:
			print(Style.RESET_ALL, end='')
			print("\tEl Necromóvil solo pueden mover fichas muertas.")
		elif i == 5:
			print(Style.RESET_ALL, end='')
			print("\tEl Asesino mata intercambiando lugares con la pieza víctima,")
		elif i == 6:
			print(Style.RESET_ALL, end='')
			print("\tlos Militantes y el Capitán colocan la ficha muerta donde el jugador guste.")
		elif i == 7:
			print(Style.RESET_ALL, end='')
			print("\tSi hay un error al escoger una pieza, el movimiento puede ser cancelado,")
		elif i == 8:
			print(Style.RESET_ALL, end='')
			print("\tingresando cualquier casilla que no sea válida para esa pieza.")
	print("\t\t\t\t\tCuando un Capitán llega a la casilla central se convierte en Presidente,")
	print("\t\t\t\t\tlo que le otorga un turno extra después de cada jugador.")
	print("\t\t\t\t\tSi un Capitán queda encerrado entre fichas muertas sin posibilidad de moverse,")
	print("\t\t\t\t\ty el necromóvil de su color ha muerto, el jugador ya no jugará,")
	print("\t\t\t\t\ta menos que sea liberado por otro equipo; o si hay un Presidente,")
	print("\t\t\t\t\tentonces las piezas pasan a ser del Presidente y el jugador pierde.")
	print("\t\t\t\t\tEl ganador es el último Capitán vivo o el último que pueda jugar.")
	return

def imprimirJug(jug):
	print(Style.BRIGHT, end='')
	if jug == 1:
		print(Fore.RED, end='')
	elif jug == 2:
		print(Fore.CYAN, end='')
	elif jug == 3:
		print(Fore.YELLOW, end='')
	elif jug == 4:
		print(Fore.GREEN, end='')
	print("JUGADOR",jug, end='')
	print(Style.RESET_ALL, end='')

	return

def limpiar(tablero, jug, jugadores):
	sys("cls")
	imprimirTablero(tablero,jugadores)
	print("\n\t", end='')
	imprimirJug(jug)
	print('')

	return

def mostrarGanador(jug):
	print(Style.BRIGHT, end='')
	print("\n\tEl ", end='')
	imprimirJug(jug)
	print(Style.BRIGHT, end='')
	print(" ha ganado. ¡Felicidades, campeón!\n")
	print(Style.RESET_ALL, end='')
	return