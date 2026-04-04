import sqlite3


def conectar(nome_perfil):
    return sqlite3.connect(f"{nome_perfil}.db")


def criar_tabelas(nome_perfil):
    conn = conectar(nome_perfil)
    cursor = conn.cursor()
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS transacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT,
        descricao TEXT,
        tipo TEXT,
        valor REAL,
        origem TEXT
    )
    """
    )
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS salario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        valor REAL,
        dia_pagamento INTEGER
    )
    """
    )
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS salario_lancado (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        mes INTEGER,
        ano INTEGER
    )
    """
    )
    conn.commit()
    conn.close()
