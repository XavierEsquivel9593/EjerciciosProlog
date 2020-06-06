"""		INTEGRANTES
ERICK XAVIER ESQUIVEL MACIAS 16590461 
GÓMEZ OLVERA JACOB MISAEL 16590474"""

"""https://www.computrabajo.com.mx/ofertas-de-trabajo/oferta-de-trabajo-de-desarrollador-batch-exp-sistemas-abiertos-en-queretaro-601BC72F6CEBB0F761373E686DCF3405
	En una empresa solicitan Lic./Ing. en Sistemas, Computación o afín.
	con los siguientes requisitos:

	• Oracle BBDD
	• SQL y PL/SQL
	• Linux
	• Unix
	• Shell (Linux - Unix)
	• C++, Proc*C y Tuxedo V12 o anteriores
	• Visual Basic 6.0
	• Java (Frameworks) , Web Services y Micro Servicios APIs
	
	Realizar un programa que realice preguntas al usuario
	y que apartir de sus respuestas evalue si es cadidato o no
	
	(usen conjuntos)"""


Requisitos = {
	"Oracle","SQL/PL","Linux","Unix","Shell","C++",
	"Proc*C","TuxedoV12", "VB6", "Java","WebServices","MicroServicios"
} 

def pedirRequisitos():
	input("Responda con y ne caso de contar con experiencia, de lo contrario prosiga.")
	Req1 = input("1.- Experiencia con Oracle? ").upper()
	Req2 = input("2.- Experiencia con SQL y PL/SQL? ").upper()
	Req3 = input("3.- Experiencia con Linux? ").upper()
	Req4 = input("4.- Experiencia con Unix? ").upper()
	Req5 = input("5.- Experiencia con Shell? ").upper()
	Req6 = input("6.- Experiencia con C++? ").upper()
	Req7 = input("7.- Experiencia con Proc*C? ").upper()
	Req8 = input("8.- Experiencia con TuxedoV12? ").upper()
	Req9 = input("9.- Experiencia con VB6? ").upper()
	Req10 = input("10.- Experiencia con Java? ").upper()
	Req11 = input("11.- Experiencia con WebServices? ").upper()
	Req12 = input("13.- Experiencia en MicroServicios? ").upper()

	ExpReq = set()
	if Req1 == "Y":
		ExpReq.add("Oracle")
	if Req2 == "Y":
		ExpReq.add("SQL/PL")
	if Req3 == "Y":
		ExpReq.add("Linux")
	if Req4 == "Y":
		ExpReq.add("Unix")
	if Req5 == "Y":
		ExpReq.add("Shell")
	if Req6 == "Y":
		ExpReq.add("C++")
	if Req7 == "Y":
		ExpReq.add("Proc*C")
	if Req8 == "Y":
		ExpReq.add("TuxedoV12")
	if Req9 == "Y":
		ExpReq.add("VB6")
	if Req10 == "Y":
		ExpReq.add("Java")
	if Req11 == "Y":
		ExpReq.add("WebServices")
	if Req12 == "Y":
		ExpReq.add("MicroServicios")
	noExp = Requisitos - ExpReq
	conReq = Requisitos & ExpReq

	print("\nUsted cuenta con los siguientes requisitos: ",ExpReq)
	print("Usted no cuenta con los siguientes requisitos: ",noExp)

	tReq = len(Requisitos)
	Exp = len(conReq)
	reqMin = tReq - 2 #debe coumplir con al menos 11 de los 13
	if Exp >= reqMin:
		return "\nEres candidato para la vacante, Felicidades."
	else:
		return "Nosotros le llamamos"

print(pedirRequisitos())