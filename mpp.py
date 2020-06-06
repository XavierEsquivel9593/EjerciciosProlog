"""
        INTEGRANTES
ERICK XAVIER ESQUIVEL MACIAS 16590461
GÓMEZ OLVERA JACOB MISAEL 16590474
                                  """

"""
# Programación  Lógica
# Modus ponendo ponens

"el modo que, al afirmar, afirma"
P → Q. P ∴ Q

Se puede encadenar usando algunas variables
P → Q. 
Q → S. 
S → T. P ∴ T

Ejercicio 
Defina una funcion que resuelva con verdadero o falso segun corresponda

Laura esta en Queretaro
Alena esta en Paris
Claudia esta en San Francisco
Queretaro esta en Mexico
Paris esta en Francia
San Francisco esta en EUA
Mexico esta en America
Francia esta en Europa
EUA esta en America

def esta(E1,E2):
	pass
print(esta("Alena","Europa"))
# true
print(esta("Laura","America"))
# true
print(esta("Laura","Europa"))
# false
"""

Base = [
	["Laura", "Queretaro"],
	["EUA", "America"],
	["Queretaro", "Mexico"],
	["Francia", "Europa"],
	["San Francisco", "EUA"],
	["Claudia", "San Francisco"],
	["Mexico", "America"],
	["Alena", "Paris"],
	["Paris", "Francia"]
]

def esta(E1,E2,B=False):
	Enc = [Base[x][1] for x in range(0,len(Base)) if E1 == Base[x][0]]
	if len(Enc) > 0:
		if Enc[0] == E2:
			print(Enc[0] == E2)
		else:
			return esta(Enc[0], E2)
	else:
		print(B)

esta("Alena", "Europa")

