import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Gabriel$582",
        database="gestao_suporte"
    )


def executar_comando(comando, dados):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(comando, dados)
    conexao.commit()
    cursor.close()
    conexao.close()

def consultar_comando(comando, dados):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(comando, dados)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado
