peso = float(input("Peso de peixes: "))

if peso > 50:
	print("Multa: " + str((peso - 50) * 4 ) )

else: 
	print("Não existem taxas para esse peso.")
	