salario = float(input("Digite seu salário: "))

if salario < 280:
	aumento = salario * 0.2
	salarioFinal = salario + aumento
	taxa = "2%"

elif  salario < 750:
	aumento = salario * 0.15
	salarioFinal = salario + aumento
	taxa = "1,5%"

elif salario < 1500:
	aumento = salario * 0.1
	salarioFinal = salario + aumento
	taxa = "1%"

else:
	aumento = salario * 0.05
	salarioFinal = salario + aumento
	taxa = "0,5%"


print("Salario inicial: " + str(salario))
print("Salario Aumento: " + str(aumento))
print("Salario Final: " + str(salarioFinal))
print("Taxa aplicada: " + str(taxa))
