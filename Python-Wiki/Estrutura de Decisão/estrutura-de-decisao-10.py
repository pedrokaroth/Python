print("M - Matutino\nV - Vespertino\nN - Noturno")
turno = input("Digite seu turno: ")

if turno.lower() == "m":
	print("Bom dia")

elif turno.lower() == "v":
	print("Boa tarde")

elif turno.lower() == "n":
	print("Boa noite")

else:
	print("Turno inválido")