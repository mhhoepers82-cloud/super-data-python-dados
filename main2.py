from mysql.connector import connect


def conectar():
    conexao = connect(
        host="localhost",
        port=3306,
        user="root",
        password="admin",
        database="helpdask"

    )

    print("Conexão aberta com sucesso")
    return conexao

def consultar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, cor FROM helpdask")
    registros = cursor.fetchall()
    cursor.close()
    conexao.close()

    #fetchall = consulta todos!!

    print("Categorias:")
    for produto in registros:
    #print("Id:, produto[0],"\nNome:", produto[1], "\nDescrição:", produto[2], "\n\n")
        print(produto[0], "=>", produto[1], "=>", produto[2])