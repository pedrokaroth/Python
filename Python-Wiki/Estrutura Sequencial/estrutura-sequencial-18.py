tamanho = int(input("Tamanho do arquivo em MB: "))
velocidade = int(input("Velocidade da internet MBps: "))
print("Tempo estimado: " + str(tamanho/(velocidade/8)) + " segundos")
