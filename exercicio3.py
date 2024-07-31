def dados():
  codigo = input("Insira o código do produto: ")
  nome = input("Insira o nome do produto: ")
  quantidade = int(input("Insira a quantidade do produto: "))
  preco = float(input("Insira o preço do produto: "))

  print(f"Código: {codigo}" "\n" f"Nome: {nome}" "\n" f"Quantidade: {quantidade}" "\n" f"Preço: R$ {preco}" "\n")
  print(f"Valor total da compra: R$ {(quantidade * preco)}")

dados()