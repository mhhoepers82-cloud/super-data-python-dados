from mysql.connector import connect


def conectar():
    conexao = connect(
        host="localhost",
        port=3306,
        user="root",
        password="admin",
        database="loja_db"

    )

    print("Conexão aberta com sucesso")
    return conexao


def consultar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, descricao FROM produtos")
    registros = cursor.fetchall()
    cursor.close()
    conexao.close()

    #fetchall = consulta todos!!

    print("Produtos:")
    for produto in registros:
    #print("Id:, produto[0],"\nNome:", produto[1], "\nDescrição:", produto[2], "\n\n")
        print(produto[0], "=>", produto[1], "=>", produto[2])


def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    descricao = input("Digite a Descriçao: ")

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO produtos (nome, descricao) VALUES (%s, %s)",
        (nome, descricao)
    )
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Produto cadastrado com sucesso")

def apagar_produto():
    id_produto = int(input("Digite o id do produto para apagar: "))

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = %s", (id_produto,))
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Produto apagado com sucesso")

def editar_produto():
    id_produto = (int(input("Digite o id do produto para editar: ")))
    novo_nome = input("Digite o nome do produto: ")
    nova_descrição = input("Digite a descrição: ")

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE produtos SET nome = %s, descricao = %s WHERE id  = %s",
        (novo_nome, nova_descrição, id_produto)
   )

    conexao.commit()
    cursor.close()
    conexao.close()
    print("Produto alterado com sucesso!!")


##======================================================

def consultar_cliente():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, cnpj, endereco, email, limite FROM cliente")
    registros = cursor.fetchall()
    cursor.close()
    conexao.close()

    print("Clientes:")
    for cliente in registros:
        #print("Id:, produto[0],"\nNome:", produto[1], "\nDescrição:", produto[2], "\n\n")
        print(cliente[0], "=>", cliente[1], "=>", cliente[2], "=>", cliente[3],"=>", cliente[4],"=>", cliente[5])

def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    cnpj = input("Digite o CNPJ do cliente: ")
    endereco = input("Digite o endereço: ")
    email = input("Digite o e-mail do cliente: ")
    limite = float(input("Digite o limite de crédito do cliente: "))

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO cliente (nome, cnpj, endereco, email, limite ) VALUES (%s, %s, %s, %s, %s)",
        (nome, cnpj, endereco, email, limite)
    )
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Cliente cadastrado com sucesso")

def apagar_cliente():
    id_cliente = int(input("Digite o id do cliente para apagar: "))

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM cliente WHERE id = %s", (id_cliente,))
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Cliente apagado com sucesso")

def editar_cliente():
    id_cliente = int(input("Digite o id do cliente para editar: "))
    novo_nome = input("Digite o nome do cliente: ")
    novo_cnpj = input("Digite o novo cnpj: ")
    novo_endereco = input("Digite o novo endereço do cliente: ")
    novo_email = input("Digite o novo email do cliente: ")
    novo_limite = float(input("Digite o novo limite do cliente: "))

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE cliente SET nome = %s, cnpj = %s, endereco = %s, email = %s, limite = %s WHERE id = %s",
        (novo_nome, novo_cnpj, novo_endereco, novo_email, novo_limite, id_cliente)
    )

    conexao.commit()
    cursor.close()
    conexao.close()
    print("Cliente alterado com sucesso!!")

def limpar_terminal():
    import os
    os.system("cls")

if __name__ == "__main__":
    menu = """MENU:
1  -Consultar produtos
2  -Cadastrar produtos
3  -Apagar produtos
4  -Editar produtos
5  -Consultar cliente
6  -Cadastrar cliente
7  -Apagar cliente
8  -Editar cliente
99 -Sair

Digitar o menu desejado:"""
    menu_escolhido = int(input(menu))

    while menu_escolhido != 99:
        limpar_terminal()
        if menu_escolhido == 1:
            consultar_produtos()
        elif menu_escolhido == 2:
            cadastrar_produto()
        elif menu_escolhido == 3:
            apagar_produto()
        elif menu_escolhido == 4:
            editar_produto()
        elif menu_escolhido == 5:
            consultar_cliente()
        elif menu_escolhido == 6:
            cadastrar_cliente()
        elif menu_escolhido == 7:
            apagar_cliente()
        elif menu_escolhido == 8:
            editar_cliente()   
        else:
            print("Opção inválida!!") 
    
        menu_escolhido = int(input(menu))