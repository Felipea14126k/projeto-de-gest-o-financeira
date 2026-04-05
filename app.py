from perfil import perfil_existe, criar_perfil, escolher_perfil, salvar_perfil, listar_perfis
from database import criar_tabelas
from financas import *
from importador_csv import importar_csv


def tela_inicial(perfil):

    if "conhecimento_financeiro" in perfil:
        print(f"\nConhecimento financeiro salvo: {perfil['conhecimento_financeiro']}")
        resposta = input("Pressione Enter para continuar ou digite alterar: ").lower()

        if resposta != "alterar":
            return

    print(f"\nOlá, bem-vindo, {perfil['nome']}! 👋")

    while True:

        resposta = input(
            "Você já tem algum conhecimento em gestão financeira? (sim/não): "
        ).lower()

        if resposta == "sim" or resposta == "não":

            perfil["conhecimento_financeiro"] = resposta
            salvar_perfil(perfil)

            print("Informação salva com sucesso ✅")

            if resposta == "sim":
                print("Ótimo, vamos seguir para o sistema.")

            else:
                 tutorial_financeiro()

            break

        else:
            print("Apenas respostas de sim ou não.")
            


def menu(perfil):

    while True:

        print("\n=== PAGINA INICIAL ===\n")

        print("1 - Importar extrato CSV")
        print("2 - Adicionar transação")
        print("3 - Deletar transação")
        print("4 - Mostrar saldo")
        print("5 - Relatório despesas")

        print("8 - Trocar perfil")
        print("9 - Menu inicial")

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

        elif op == "8":

            perfis = listar_perfis()
            if len(perfis) > 1:
                    return

            else:
                print("É necessário ter mais de um perfil para trocar.")

        elif op == "9":
            return


        elif op == "0":
            print("Saindo do programa...")
            exit()


def tutorial_financeiro():
    print("\n=== MINI TUTORIAL FINANCEIRO ===\n")
    print("• Crédito = dinheiro que entra")
    print("• Débito = dinheiro que sai")
    print("• Saldo = total disponível")
    print("• Relatório ajuda a entender seus gastos")













if not perfil_existe():
    criar_perfil()

    perfil = escolher_perfil()

    criar_tabelas(perfil["nome"])

    tela_inicial(perfil)

    menu(perfil)