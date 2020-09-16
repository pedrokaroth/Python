produtos = []

produtos.append(int(input("Digite o valor do produto: ")))
produtos.append(int(input("Digite o valor do produto: ")))
produtos.append(int(input("Digite o valor do produto: ")))

print("Melhor valor: " + str(sorted(produtos)[0]))