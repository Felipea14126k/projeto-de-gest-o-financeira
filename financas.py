from database import conectar


def adicionar_transacao(nome_perfil):

    data = input("Data (DD-MM-YYY): ")
    descricao = input("Descrição: ")
    tipo = input("Tipo (credito/debito): ")
    valor = float(input("Valor (0.00): "))

    conn = conectar(nome_perfil)
    cursor = conn.cursor()

    cursor.execute(
        """
    INSERT INTO transacoes
    (data, descricao, tipo, valor, origem)
    VALUES (?, ?, ?, ?, 'manual')
    """,
        (data, descricao, tipo, valor),
    )

    conn.commit()
    conn.close()

    print("Transação adicionada.")


def deletar_transacao(nome_perfil):

    id = input("ID da transação: ")

    conn = conectar(nome_perfil)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM transacoes WHERE id=?", (id,))

    conn.commit()
    conn.close()

    print("Transação removida.")


def mostrar_saldo(nome_perfil):

    conn = conectar(nome_perfil)
    cursor = conn.cursor()

    cursor.execute(
        """
    SELECT
    SUM(CASE WHEN tipo='credito' THEN valor ELSE 0 END) -
    SUM(CASE WHEN tipo='debito' THEN valor ELSE 0 END)
    FROM transacoes
    """
    )

    saldo = cursor.fetchone()[0]

    if saldo is None:
        saldo = 0

    print(f"Saldo atual: R$ {saldo:.2f}")

    conn.close()


def relatorio_despesas(nome_perfil):

    conn = conectar(nome_perfil)
    cursor = conn.cursor()

    cursor.execute(
        """
    SELECT substr(data,1,7) mes,
    SUM(valor)
    FROM transacoes
    WHERE tipo='debito'
    GROUP BY mes
    """
    )

    resultados = cursor.fetchall()

    print("\nDespesas por mês\n")

    for mes, total in resultados:
        print(mes, "R$", total)

    conn.close()
