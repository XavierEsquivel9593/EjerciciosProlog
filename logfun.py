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
	input("RESPONDA CON Y PARA AFIRMAR QUE TIENE EXPERIENCIA")
	input("CASO CONTRARIO PROSIGA")
	Req1 = input("Experiencia con Oracle? ").upper()
	Req2 = input("Experiencia con SQL y PL/SQL? ").upper()
	Req3 = input("Experiencia con Linux? ").upper()
	Req4 = input("Experiencia con Unix? ").upper()
	Req5 = input("Experiencia con Shell? ").upper()
	Req6 = input("Experiencia con C++? ").upper()
	Req7 = input("Experiencia con Proc*C? ").upper()
	Req8 = input("Experiencia con TuxedoV12? ").upper()
	Req9 = input("Experiencia con VB6? ").upper()
	Req10 = input("Experiencia con Java? ").upper()
	Req11 = input("Experiencia con WebServices? ").upper()
	Req12 = input("Experiencia en MicroServicios? ").upper()

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
	#set.intersection()
	conReq = Requisitos & ExpReq

	print("\nUsted Cuenta Con estos requisitos ---> ",ExpReq)
	print("Usted NO Cuenta Con estos requisitos---> ",noExp)

	tReq = len(Requisitos)
	Exp = len(conReq)
	reqMin = tReq - 2 #SE PIDE QUE AL MENOS CUMPLA CON 10 DE 12 REQUISITOS PARA SER CANDIDATO
	if Exp >= reqMin:
		return "\nMuy Bien!! Eres Candidato Para La Vacante"
	else:
		return "Nosotros Te Llamamos xD"

print(pedirRequisitos())
	#print(Requisitos())
"""		INTEGRANTES
ERICK XAVIER ESQUIVEL MACIAS 16590461 
GÓMEZ OLVERA JACOB MISAEL 16590474"""