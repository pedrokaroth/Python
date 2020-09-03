area = int(input("Área a ser pintada: "))
latas = round( ( (area / 3) / 18) + 0.5)
print("Latas: " + str(latas))
print("Valor: R$" + str(latas * 80))
