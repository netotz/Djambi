from actualizar import *
from impresiones import limpiar, mostrarGanador
from movimientos import moverPzaEnTab, posiblesDestinos, reporMata
from busquedas import jugTienePza, validMov, posDePzaEnTab

def turno(tablero, jugs):
	N = 0

	hay_presi = False
	siguiente = 0
	anterior = -1

	dblturn = False
	first = True
	turnos = 0

	quitar = False
	pza = ''
	orig = 0

	while True:
		aux = N
		if anterior == 3:
			aux = 0

		if hay_presi:
			if anterior != presidente:
				siguiente = aux
				N = presidente
			else:
				if dblturn:
					if not first:
						if turnos < 1:
							N = presidente
							turnos += 1
						else:
							turnos = 0
					first = False
				if siguiente == presidente:
					siguiente += 1
				else:
					N = siguiente
		else:
			dblturn = False
			first = True
			if siguiente == anterior:
				siguiente += 1
			N = siguiente

		if N > 3:
			N = 0
		if siguiente > 3:
			siguiente = 0

		if not jugs[N].jefe or jugs[N].cerrado:
			if N == siguiente:
				siguiente += 1
			N += 1
			continue

		if N == anterior and (not jugs[N].presi or not dblturn):
			N += 1
			continue

		jug = jugs[N].num
		limpiar(tablero,jug,jugs)

		while True:
			x = 0
			y = 0
			if not quitar:
				pza = pedirPieza()
				orig = 0
			pza = pza.upper()

			ficha = str(jug) + pza

			tiene = jugTienePza(jugs[N].piezas, pza)
			if not tiene:
				print("\t\tUsted no tiene la pieza ",pza,".\n\t\tSolo letras de su color de jugador.\n", sep='')
				continue
			elif tiene > 1 and not quitar:
				orig = especificar(1)
				x = int(orig[0])
				y = int(orig[1])
				if len(tablero[x][y]) == 2:
					if tablero[x][y][0] != str(jug):
						print("\t\tNo puede mover piezas de otro jugador.\n")
						continue
				else:
					print("\t\tEn la casilla",orig,"no se encuentra ninguna pieza",pza,"\b.\n")
					continue

			vector = posiblesDestinos(tablero, ficha, orig)
			if not vector:
				print("\t\tSu pieza",pza,"no tiene ningún movimiento válido.\n")
				quitar = False
				continue
			else:
				pos = pedirCasilla(1,ficha[1])
				if not validMov(vector,pos):
					print("\t\tLa casilla ",pos," no es un destino válido para la pieza ",pza,".\n", sep='')
					continue
				else:
					break

		obj = tablero[ int(pos[0]) ][ int(pos[1]) ]
		letraObj = ''

		if pza == 'R':
			tablero = moverPzaEnTab(tablero, ficha, '', pos, orig)
			limpiar(tablero,jug,jugs)

			arreglo = reporMata(tablero,pos,jug)
			if arreglo:
				if len(arreglo) == 1:
					dest = arreglo[0]
				elif len(arreglo) > 1:
					while True:
						dest = especificar(0)
						if not validMov(arreglo,dest):
							print("\t\tEn la casilla",dest,"no se encuentra ninguna víctima válida.\n")
							continue
						else:
							break

				i = int(dest[0])
				j = int(dest[1])
				obj = tablero[i][j]
				letraObj = obj[1]
				tablero[i][j] = '0'

		else:
			if obj == '':
				tablero = moverPzaEnTab(tablero, ficha, '', pos, orig)

			elif obj == '0':
				tablero = moverPzaEnTab(tablero, ficha, '', pos, orig)
				limpiar(tablero,jug,jugs)

				while True:
					dest = pedirCasilla(0,letraObj)
					if dest == '44':
						print("\t\tLas fichas muertas no se pueden colocar en la casilla central (44).\n")
						continue
					elif tablero[int(dest[0])][int(dest[1])] == '':
						break
					else:
						print("\t\tLa ficha muerta debe ser colocada en una casilla vacía.\n")
						continue

				tablero = moverPzaEnTab(tablero, '0', ficha, dest, pos)

			else:
				letraObj = obj[1]
				if pza == 'D':
					tablero = moverPzaEnTab(tablero, ficha, '', pos, orig)
					limpiar(tablero,jug,jugs)

					while True:
						dest = pedirCasilla(1,letraObj)
						if tablero[int(dest[0])][int(dest[1])] == '':
							if dest == '44':
								if letraObj == 'C':
									break
								else:
									print("\t\tSolo las piezas C pueden colocarse en la casilla central (44).\n")
									continue
							else:
								break
						else:
							print("\t\tLa pieza enemiga",letraObj,"debe ser colocada en una casilla vacía.\n")
							continue

					tablero = moverPzaEnTab(tablero, obj, ficha, dest, pos)
					
				elif pza == 'A':
					tablero = moverPzaEnTab(tablero, ficha, '0', pos, orig)

				else:
					tablero = moverPzaEnTab(tablero, ficha, '', pos, orig)
					limpiar(tablero,jug,jugs)

					while True:
						dest = pedirCasilla(0,letraObj)
						if dest == '44':
							print("\t\tLas fichas muertas no se pueden colocar en la casilla central (44).\n")
							continue
						elif tablero[int(dest[0])][int(dest[1])] == '':
							break
						else:
							print("\t\tLa ficha muerta debe ser colocada en una casilla vacía.\n")
							continue

					tablero = moverPzaEnTab(tablero, '0', ficha, dest, pos)

		if letraObj == 'C' and pza != 'D':
			tablero = pasarPiezas(tablero, str(jug), obj[0])

		jugs = propiedades(jugs, tablero)

		vivos = 0
		for jug in jugs:
			if jug.jefe:
				if not jug.necro and posDePzaEnTab(tablero,str(jug.num) + 'C') != '44' and encerrado(tablero,jug.num):
					jug.cerrado = True
				else:
					vivos += 1
					ganador = jug.num
					jug.cerrado = False

		if vivos == 1:
			limpiar(tablero,ganador,jugs)
			mostrarGanador(ganador)
			break
		elif vivos == 2:
			dblturn = True

		central = tablero[4][4]
		if central == '' or central == '0':
			hay_presi = False
			presidente = -1
		elif central[1] == 'C':
			for jug in jugs:
				if int(central[0]) == jug.num:
					hay_presi = True
					jug.presi = True
					presidente = jug.num -1
					break
				else:
					jug.presi = False
		else:
			quitar = True
			N = central[0]
			pza = central[1]
			orig = '44'
			continue
		pza = ''
		orig = 0
		quitar = False

		if hay_presi:
			for jug in jugs:
				if jug.jefe and jug.cerrado:
					pos = posDePzaEnTab(tablero,str(jug.num)+'C')
					tablero[int(pos[0])][int(pos[1])] = '0'
					tablero = pasarPiezas(tablero, str(presidente + 1), str(jug.num) )

		jugs = propiedades(jugs, tablero)

		anterior = N
		N += 1

	return