import sqlite3
class Produto: 
    def conexao(self):
        conexao = sqlite3.connect("loja.db") #criando um arquivo que irá guardar nosso banco de dados

        tabela = """
        CREATE TABLE IF NOT EXISTS produto(
            codigo INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(100),
            preco FLOAT,
            quantidade_disponivel VARCHAR(100)
        );
        """

        consulta = conexao.cursor() #o objeto cursor () é responsavel por manipular dados do banco de dados

        consulta.execute(tabela)

        return conexao
    
    def cadastrarProduto(self, nome, preco, quantidade_disponivel):
        conexao = self.conexao() # chamando o método 'conexao' que irá conectar ao banco 

        sql = "INSERT INTO produto VALUES(?,?,?,?)" #evitar possiveis ataques de sql injection

        campos = (None, nome, preco, quantidade_disponivel) #none - será atribuído o valor padrao do AUTOINCREMENT

        consulta = conexao.cursor()
        consulta.execute(sql, campos)

        conexao.commit()
        print(consulta.rowcount, "Produto cadastrado com sucesso!\n")
        conexao.close()

    def consultarProduto(self):
        conexao = self.conexao()

        consulta = conexao.cursor()
        sql = "SELECT * FROM produto"

        consulta.execute(sql)

        resultado = consulta.fetchall() #pegando todos os registros da tabela

        for item in resultado:
            print(f"Código: {item[0]}")
            print(f"Nome: {item[1]}")
            print(f"Preço: {item[2]}")
            print(f"Quantidade: {item[3]}")

        conexao.close()
    
    def deletarProduto(self, codigo):
        conexao = self.conexao()  # Certifique-se de que esse método retorna uma conexão válida
        consulta = conexao.cursor()

        # Executa a consulta para deletar o produto com o código fornecido
        consulta.execute('DELETE FROM produto WHERE codigo = ?', (codigo,))
        conexao.commit()

        if consulta.rowcount > 0:
            print(f"Produto de código {codigo} deletado com sucesso.")
        else:
            print(f"Produto de código {codigo} não encontrado.")

        conexao.close()

    def atualizarProdutos(self):
        conexao = self.conexao()
        consulta = conexao.cursor()

        nome = input("Informe o nome do novo produto: ")
        codigo = int(input("Qual o código do produto: "))

        sql = "UPDATE produto SET nome = ? WHERE codigo = ?"
        campos = (nome, codigo)

        consulta.execute(sql, campos)

        conexao.commit()

        print(consulta.rowcount, "Produto atualizado com sucesso!\n")
        conexao.close()

    def consultarProdutosIndividual(self, codigo):
        conexao = self.conexao()
        consulta = conexao.cursor()

        sql = "SELECT * FROM produto WHERE codigo = ?"

        consulta.execute(sql, (codigo,))  #codigo em uma tupla

        resultado = consulta.fetchall()  #todos os registros da tabela

        if resultado:
            item = resultado[0]  # pegando apenas o primeiro registro
            print(f"Código: {item[0]}")
            print(f"Nome: {item[1]}")
            print(f"Preço: {item[2]}")
            print(f"Quantidade Disponível: {item[3]}")
        else:
            print(f"O produto com código {codigo} não encontrado.")

        conexao.close()