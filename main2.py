

import mysql.connector
from datetime import datetime

from banco_dados import conectar

# ============================================================
# CATEGORIAS
# ============================================================
def cadastrar_categoria(nome, cor):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "INSERT INTO categorias (nome, cor) VALUES (%s, %s)"
    cursor.execute(sql, (nome, cor))
    conexao.commit()

    print(f"Categoria '{nome}' cadastrada! ID gerado: {cursor.lastrowid}")

    cursor.close()
    conexao.close()


def consultar_categorias():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT id, nome, cor FROM categorias")
    resultados = cursor.fetchall()

    for id_cat, nome, cor in resultados:
        print(f"[{id_cat}] {nome} - {cor}")

    cursor.close()
    conexao.close()
    return resultados


def deletar_categoria(id_categoria):
    conexao = conectar()
    cursor = conexao.cursor()
 
    cursor.execute("DELETE FROM categorias WHERE id = %s", (id_categoria,))
    conexao.commit()
 
    if cursor.rowcount == 0:
        print(f"Nenhuma categoria encontrada com id {id_categoria}.")
    else:
        print(f"Categoria {id_categoria} excluída.")
 
    cursor.close()
    conexao.close()


# ============================================================
# TICKETS
# ============================================================
def gerar_numero_protocolo():
    # Ex: "TCK-20260924153045", baseado na data/hora atual
    return "TCK-" + datetime.now().strftime("%Y%m%d%H%M%S")


def criar_ticket(titulo, descricao, prioridade, setor):
    numero_protocolo = gerar_numero_protocolo()

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO tickets (numero_protocolo, titulo, descricao, status, prioridade, setor)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    valores = (numero_protocolo, titulo, descricao, "ABERTO", prioridade, setor)
    cursor.execute(sql, valores)
    conexao.commit()

    print(f"Ticket criado! Protocolo: {numero_protocolo} (id {cursor.lastrowid})")

    cursor.close()
    conexao.close()
    return numero_protocolo


def listar_tickets():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, numero_protocolo, titulo, status, prioridade, setor, data_criacao
        FROM tickets
        ORDER BY data_criacao DESC
    """)
    resultados = cursor.fetchall()

    for id_t, protocolo, titulo, status, prioridade, setor, data in resultados:
        print(f"[{id_t}] {protocolo} | {titulo} | {status} | {prioridade} | {setor} | {data}")

    cursor.close()
    conexao.close()
    return resultados


def buscar_ticket_por_id(id_ticket):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM tickets WHERE id = %s", (id_ticket,))
    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()
    return resultado


def atualizar_status_ticket(id_ticket, novo_status, descricao_solucao=None):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "UPDATE tickets SET status = %s, descricao_solucao = %s WHERE id = %s"
    cursor.execute(sql, (novo_status, descricao_solucao, id_ticket))
    conexao.commit()

    if cursor.rowcount == 0:
        print(f"Nenhum ticket encontrado com id {id_ticket}.")
    else:
        print(f"Ticket {id_ticket} atualizado para status {novo_status}.")

    cursor.close()
    conexao.close()


def deletar_ticket(id_ticket):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM tickets WHERE id = %s", (id_ticket,))
    conexao.commit()

    if cursor.rowcount == 0:
        print(f"Nenhum ticket encontrado com id {id_ticket}.")
    else:
        print(f"Ticket {id_ticket} excluído.")

    cursor.close()
    conexao.close()


# ============================================================
# MENU
# ============================================================
def menu():
    while True:
        print("\n===== MENU HELPDESK =====")
        print("1 - Cadastrar categoria")
        print("2 - Consultar categorias")
        print("3 - Criar ticket")
        print("4 - Listar tickets")
        print("5 - Buscar ticket por id")
        print("6 - Atualizar status do ticket")
        print("7 - Deletar ticket")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome da categoria: ")
            cor = input("Cor em hexadecimal (ex: #FF0000): ")
            cadastrar_categoria(nome, cor)

        elif opcao == "2":
            consultar_categorias()

        elif opcao == "3":
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            prioridade = input("Prioridade (BAIXA, MEDIA, ALTA): ")
            setor = input("Setor (TI, RH, FINANCEIRO, ADMINISTRATIVO, MANUTENCAO): ")
            criar_ticket(titulo, descricao, prioridade, setor)

        elif opcao == "4":
            listar_tickets()

        elif opcao == "5":
            id_ticket = int(input("ID do ticket: "))
            resultado = buscar_ticket_por_id(id_ticket)
            print(resultado if resultado else "Ticket não encontrado.")

        elif opcao == "6":
            id_ticket = int(input("ID do ticket: "))
            novo_status = input("Novo status (ABERTO, EM_ANALISE, RESOLVIDO, CANCELADO): ")
            solucao = input("Descrição da solução (opcional, Enter para pular): ")
            atualizar_status_ticket(id_ticket, novo_status, solucao if solucao else None)

        elif opcao == "7":
            id_ticket = int(input("ID do ticket a excluir: "))
            deletar_ticket(id_ticket)

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    menu()
