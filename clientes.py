
from banco_dados import conectar

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
