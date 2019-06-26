from re import search as rsrch

def validCoord(casilla):
	if len(casilla) != 2:
		return False
	return rsrch(r'^[0-8]+$',casilla)

def validPza(pieza):
	if len(pieza) != 1:
		return False
	return rsrch(r'^[mMcCdDrRaAnN]+$',pieza)