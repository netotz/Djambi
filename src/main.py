from inicio import inicializarTablero, crearJugadores
from turno import *
from os import system

def start():
	TAB = inicializarTablero()
	JUG = crearJugadores(TAB)

	turno(TAB, JUG)

start()
system("pause")
