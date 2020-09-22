notaA = float(input("Digite a 1ª Nota"))
notaB = float(input("Digite a 2ª Nota"))

media = (notaA + notaB) / 2

if (10 <= media >= 9):
	conceito = "A"

elif (media >= 7.5):
	conceito = "B"

elif (media >= 6):
	conceito = "C"

elif (media >= 4):
	conceito = "D"

elif (media >= 0):
	conceito = "E"


if conceito in ["A", "B" , "C"]:
	print("Aprovado, conceito: " + str(conceito))

else:
	print("Reprovado, conceito: " + str(conceito))
