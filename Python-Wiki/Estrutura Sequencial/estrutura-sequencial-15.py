valor = float(input("Valor da hora: "))
horas = int(input("Horas trabalhadas: "))

sb = valor * horas
ir = sb * 0.11
inss = sb * 0.08
sindicato = sb * 0.05

print(" + Salario bruto: " + str(sb))
print(" - Imposto de Renda: " + str(ir)) 
print(" - Inss: " + str(inss))
print(" - Sindicato: " + str(sindicato))
print(" = Salario Liquido: " + str(sb - ir - inss - sindicato))
