import csv
from database import conectar

def importar_csv(caminho):

    conn = conectar()
    cursor = conn.cursor()

    with open(caminho, newline='', encoding='utf-8') as arquivo:

        leitor = csv.DictReader(arquivo)

        for linha in leitor:

            data = linha["data"]
            descricao = linha["descricao"]
            valor = float(linha["valor"])

            tipo = "credito" if valor > 0 else "debito"

            cursor.execute("""
            INSERT INTO transacoes
            (data, descricao, tipo, valor, origem)
            VALUES (?, ?, ?, ?, 'csv')
            """, (data, descricao, tipo, abs(valor)))

    conn.commit()
    conn.close()

    print("Extrato importado com sucesso!")