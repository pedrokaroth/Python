salario = float(input("Digite o valor da Hora: "))
horas = int(input("Horas trabalhadas: "))
salarioBruto = salario * horas


if salarioBruto <= 900:
	ir = 0
	descontoIr = 0

elif salarioBruto <= 1500:
	ir = 5
	descontoIr = salarioBruto * (ir / 100)

elif salarioBruto <= 2500:
	ir = 10
	descontoIr = salarioBruto * (ir / 100)

else:
	ir = 20
	descontoIr= salarioBruto * (ir / 100)

descontoInss = salarioBruto * (10 / 100)
descontoTotal = descontoIr + descontoInss

print("Salario bruto: " + str(salarioBruto))
print("( - ) IR (" + str(ir) + "%):" + str(descontoIr))
print("( - ) INSS (10%): " + str(descontoInss))
print("FGTS: " + str(salarioBruto * 0.11))
print("Descontos: " + str(descontoTotal))
print("Salario liquido: " + str(salarioBruto - descontoTotal))


