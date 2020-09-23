ladoA = float(input("Lado A: "))
ladoB = float(input("Lado B: "))
ladoC = float(input("Lado C: "))

if(ladoA == ladoB == ladoC):
	print("Equilétero")

elif(ladoA == ladoB or ladoA == ladoC or ladoB == ladoC):
	print("Isóceles")

elif(ladoA != ladoB != ladoC):
	print("Escaleno")