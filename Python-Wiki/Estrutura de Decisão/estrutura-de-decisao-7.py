a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
c = int(input("Digite um número: "))

if(a < b < c):
	print("Menor valor: ", a)

elif b < c:
	print("Menor valor: ", b)

else:
	print("Menor valor: ", c)

