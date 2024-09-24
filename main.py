# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import mysql.connector


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Conectar ao banco de dados MySQL
    conn = mysql.connector.connect(
        host='localhost',  # ou o IP do servidor MySQL
        user='root',  # usuário do MySQL
        password='7931852456',  # senha do MySQL
        database='igreja_db',  # nome do banco de dados
        charset='utf8mb4',  # Define o conjunto de caracteres
        collation='utf8mb4_unicode_ci'  # Define a collation
    )

    cursor = conn.cursor()

    # Criar a tabela se ainda não existir
    cursor.execute('SELECT * FROM caixa')
    # See PyCharm help at https://www.jetbrains.com/help/pycharm/

    # Buscar todos os resultados da consulta
    resultados = cursor.fetchall()
    resultados_somados = 0
    gastos_somados = 0
    entrada_somada = 0
    saldo_inicial = resultados[0][6]
    for linha in resultados:
        id_caixa = linha[0]
        entrada = linha[1]
        saida = linha[2]
        resultado = linha[3]
        mes_referente = linha[4]
        ano_referente = linha[5]
        saldo_atual = linha[6]
        saldo_anterior = linha[7]
        resultados_somados += resultado
        gastos_somados += saida
        entrada_somada += entrada
    print("===Informação analítica anual do caixa da igreja===\n")
    print("Total em caixa: R$ {}".format(resultados_somados + saldo_inicial))
    print("A média do resultado mensal do ultimo ano foi: R$ {}".format(resultados_somados / len(resultados)))
    print("O resultado de gastos do ultimo ano foi: R$ {}".format(gastos_somados))
    print("A média de gastos mensais do ultimo ano foi: R$ {}".format(gastos_somados / len(resultados)))
    print("O resultado de entradas do ultimo ano foi: R$ {}".format(entrada_somada))
    print("A média de entradas mensais do ultimo ano foi: R$ {}".format(entrada_somada / len(resultados)))

    # Fechar o cursor e a conexão
    cursor.close()
    conn.close()
