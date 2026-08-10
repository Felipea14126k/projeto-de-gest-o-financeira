import sqlite3

NOME_BANCO = "dados.db"


def conectar():
    return sqlite3.connect(NOME_BANCO)


def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT,
        descricao TEXT,
        tipo TEXT,
        valor REAL,
        origem TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS salario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        valor REAL,
        dia_pagamento INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS salario_lancado (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        mes INTEGER,
        ano INTEGER
    )
    """)

    conn.commit()
    conn.close()