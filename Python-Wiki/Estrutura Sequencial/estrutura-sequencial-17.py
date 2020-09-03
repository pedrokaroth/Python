area = int(input("Área a ser pintada: "))
litros = area / 6
lataA = round( ( litros / 18 ) + 0.5)
lataB = round( ( litros / 3.6) + 0.5)

print("Latas de 18 litros: " + str(lataA) + " Valor:" + str(lataA * 80))
print("Latas de 3.5 litros: " + str(lataB) + " Valor: " + str(lataB * 25))

areaPintada = 0
tipoA = 0
tipoB = 0
while(areaPintada < (area + area * 0.1)):
	if (areaPintada + 108) < area:
		tipoA += 1
		areaPintada += 108
	else:
		tipoB += 1
		areaPintada += 21


print("Mistura de " + str(tipoA) + " (18 litros) com " + str(tipoB) + " (3.5 litros)" + "Total: " + str((tipoA * 80) + (tipoB * 25)))
