import os
import json

CAMINHO_PASTA = "perfil"
CAMINHO_ARQUIVO = os.path.join(CAMINHO_PASTA, "usuario.json")


def usuario_existe():
    return os.path.exists(CAMINHO_ARQUIVO)


def criar_usuario(nome):

    nome = nome.strip()

    if len(nome) < 3:
        return False, "Nome muito curto."

    if len(nome) > 60:
        return False, "Nome muito grande."

    os.makedirs(CAMINHO_PASTA, exist_ok=True)

    dados = {"nome": nome}

    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False)

    return True, "Usuário criado com sucesso."


def carregar_usuario():

    if not usuario_existe():
        return None

    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_usuario(dados):
    os.makedirs(CAMINHO_PASTA, exist_ok=True)

    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False)


def resetar_usuario():
    if usuario_existe():
        os.remove(CAMINHO_ARQUIVO)
        return True
    return False