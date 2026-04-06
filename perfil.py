import os
import json

CAMINHO_PASTA = "perfis"



def listar_perfis():

    arquivos = os.listdir(CAMINHO_PASTA)

    return [
        arquivo.replace(".json", "")
        for arquivo in arquivos
        if arquivo.endswith(".json")
    ]


def excluir_perfil():

    perfis = listar_perfis()

    if not perfis:
        print("Nenhum perfil encontrado.")
        return

    print("\nPerfis disponíveis para excluir:")

    for i, nome in enumerate(perfis, start=1):
        print(f"{i} - {nome}")

    escolha = input("Qual perfil deseja excluir? ")

    if not escolha.isdigit():
        print("Digite apenas número.")
        return

    escolha = int(escolha)

    if escolha < 1 or escolha > len(perfis):
        print("Perfil inválido.")
        return

    nome = perfis[escolha - 1]

    confirmacao = input(
        f"Tem certeza que deseja excluir {nome}? "
        "Irá perder todos seus dados e progresso de gestão. (sim/não): "
    ).lower()

    if confirmacao == "sim":
        os.remove(f"{CAMINHO_PASTA}/{nome}.json")
        print("Perfil excluído com sucesso.")
    else:
        print("Exclusão cancelada.")


def escolher_perfil():

    while True:

        print("\n=== MENU INICIAL ===")
        print("1 - Entrar em perfil")
        print("2 - Criar novo perfil")
        print("3 - Excluir perfil")

        opcao = input("Escolha: ")

        if opcao == "1":

            perfis = listar_perfis()

            if not perfis:
                print("Nenhum perfil encontrado.")
                continue

            print("\nVoltar ao menu")

            for i, nome in enumerate(perfis, start=1):
                print(f"{i} - {nome}")

            escolha = input("Escolha um perfil: ")

            if not escolha.isdigit():
                print("Digite apenas número.")
                continue

            escolha = int(escolha)

            if escolha < 1 or escolha > len(perfis):
                print("Perfil inválido.")
                continue

            nome = perfis[escolha - 1]
            return carregar_perfil(nome)

        elif opcao == "2":
            criar_perfil()

        elif opcao == "3":
            excluir_perfil()

        else:
            print("Opção inválida.")

def salvar_perfil(perfil):
    caminho = f"{CAMINHO_PASTA}/{perfil['nome']}.json"

    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(perfil, arquivo, ensure_ascii=False)

##def criar_perfil():
##  nome = input("Olá, qual seu nome de usuário? ")
##
##  os.makedirs("perfis", exist_ok=True)

##with open(CAMINHO_PERFIL, "w", encoding="utf-8") as arquivo:
##  json.dump({"nome": nome}, arquivo, ensure_ascii=False)
