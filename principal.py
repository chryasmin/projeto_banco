from produto_poo import Produto

p1 = Produto()

nome = input("Informe o nome do produto: ")
preco = float(input("Informe o preço do produto: "))
quantidade_disponivel = input("Informe a quantidade disponível: ")

p1.cadastrarProduto(nome, preco, quantidade_disponivel)
