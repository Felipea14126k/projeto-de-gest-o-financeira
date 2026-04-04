from perfil import perfil_existe, criar_perfil, escolher_perfil
from database import criar_tabelas
from financas import *
from importador_csv import importar_csv


def tela_inicial(perfil):

    print(f"\nOlá, bem-vindo, {perfil['nome']}! 👋")

    while True:

        resposta = input(
            "Você já tem algum conhecimento em gestão financeira? (sim/não): "
        ).lower()

        if resposta == "sim":
            print("Ótimo, vamos seguir para o sistema.")
            break

        elif resposta == "não":
            print(
                "Sem problemas, depois vamos iniciar um pequeno tutorial explicativo."
            )
            break

        else:
            print("Apenas respostas de Sim ou Não.")


def menu(perfil):

    while True:

        print("\n=== CONTROLE FINANCEIRO ===\n")

        print("1 - Importar extrato CSV")
        print("2 - Adicionar transação")
        print("3 - Deletar transação")
        print("4 - Mostrar saldo")
        print("5 - Relatório despesas")
        print("0 - Sair")

        op = input("\nEscolha: ")

        if op == "1":
            caminho = input("Caminho do CSV: ")
            importar_csv(caminho)

        elif op == "2":
            adicionar_transacao(perfil["nome"])

        elif op == "3":
            deletar_transacao(perfil["nome"])

        elif op == "4":
            mostrar_saldo(perfil["nome"])

        elif op == "5":
            relatorio_despesas(perfil["nome"])

        elif op == "0":
            break


if not perfil_existe():
    criar_perfil()

perfil = escolher_perfil()

criar_tabelas(perfil["nome"])

tela_inicial(perfil)

menu(perfil)
