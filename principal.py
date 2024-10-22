from produto_poo import Produto

def menu():
    loja = Produto()
    while True:  # Loop infinito até que o usuário escolha sair
        print("\nMenu:")
        print("1. Cadastrar Produto")
        print("2. Consultar Produtos")
        print("3. Deletar Produto")
        print("4. Atualizar Produto")
        print("5. Consultar Produto Individual")
        print("6. Sair")
            
        opcao = input("Escolha uma opção: ")
            
        if opcao == '1':
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            quantidade_disponivel = int(input("Quantidade disponível: "))
            loja.cadastrarProduto(nome, preco, quantidade_disponivel)
            
        elif opcao == '2':
            loja.consultarProduto()
            
        elif opcao == '3':
            codigo = int(input("Código do produto a ser deletado: "))
            loja.deletarProduto(codigo)
            
        elif opcao == '4':
            loja.atualizarProdutos()
            
        elif opcao == '5':
            codigo = int(input("Código do produto a ser consultado: "))
            loja.consultarProdutosIndividual(codigo)
            
        elif opcao == '6':
            print("Saindo...")
            break  # Agora está dentro de um loop, então funciona corretamente
            
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
menu()
