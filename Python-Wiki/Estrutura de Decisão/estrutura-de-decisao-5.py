notaA = float(input("Digite a 1º nota: "))
notaB = float(input("Digite a 2º nota: "))

media = (notaA + notaB) / 2

if media == 10:
	print("Aprovado com distinção")

elif media >= 7:
	print("Aprovado")

else:
	print("Reprovado")
	