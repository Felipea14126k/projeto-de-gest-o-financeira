from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox
)

from PyQt5.QtCore import Qt

from perfil import carregar_usuario, salvar_usuario


NOME_APP = "Gestão Financeira"

COR_FUNDO = "#131F24"
COR_CAIXA = "#1E2A2F"
COR_VERDE = "#58CC02"
COR_VERDE_HOVER = "#4CAF00"
COR_TEXTO_SECUNDARIO = "#AFAFAF"


PERGUNTAS_PARTE1 = [
    {"bloco": 1, "chave": "renda_fixa", "texto": "Qual sua renda mensal fixa?"},
    {"bloco": 1, "chave": "renda_extra", "texto": "Você tem alguma renda extra ou variável?"},
    {"bloco": 1, "chave": "dia_pagamento", "texto": "Em que dia do mês você costuma receber?"},

    {"bloco": 2, "chave": "aluguel", "texto": "Você paga aluguel ou financiamento? Quanto?"},
    {"bloco": 2, "chave": "contas_fixas", "texto": "Quanto costuma gastar com contas fixas (água, luz, internet, telefone)?"},
    {"bloco": 2, "chave": "assinaturas", "texto": "Tem alguma assinatura recorrente? (streaming, academia, etc.)"},

    {"bloco": 3, "chave": "categorias_gasto", "texto": "Em quais categorias você mais gasta no dia a dia?"},
    {"bloco": 3, "chave": "transporte", "texto": "Você tem gasto com transporte fixo (combustível, transporte público, app de carro)?"},
    {"bloco": 3, "chave": "delivery_frequencia", "texto": "Com que frequência você costuma pedir delivery ou comer fora? (ex: por semana)"},
    {"bloco": 3, "chave": "delivery_valor_medio", "texto": "Qual o valor médio que você gasta por vez com delivery/restaurante?"},
]

PERGUNTAS_DIVIDA = [
    {"chave": "valor_total", "texto": "Qual o valor total dessa dívida?"},
    {"chave": "parcela_mensal", "texto": "Qual o valor da parcela mensal?"},
    {"chave": "parcelas_restantes", "texto": "Quantas parcelas ainda faltam pagar?"},
    {"chave": "valor_pago", "texto": "Já foi pago algum valor até agora? Se sim, quanto?"},
]

PERGUNTAS_PARTE2 = [
    {"bloco": 5, "chave": "meta_existe", "texto": "Você tem alguma meta financeira? (juntar dinheiro, quitar dívida, comprar algo)"},
    {"bloco": 5, "chave": "meta_valor_prazo", "texto": "Se sim, qual o valor e prazo aproximado dessa meta?"},
]

BLOCOS_OBRIGATORIOS = [1, 2]


class TelaQuestionario(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(NOME_APP)
        self.resize(1000, 650)

        self.setStyleSheet(f"""
            QWidget{{
                background:{COR_FUNDO};
            }}
        """)

        self.respostas = {}
        self.dividas = []
        self.divida_atual = {}

        self.fase = "parte1"
        self.indice = 0
        self.indice_divida = 0

        self.historico = []

        self.titulo = QLabel("")
        self.titulo.setAlignment(Qt.AlignCenter)
        self.titulo.setWordWrap(True)
        self.titulo.setStyleSheet("""
            color:white;
            font-size:26px;
            font-weight:bold;
        """)

        self.campo_resposta = QLineEdit()
        self.campo_resposta.setStyleSheet(f"""
            background:{COR_CAIXA};
            color:white;
            padding:10px;
            border-radius:8px;
            font-size:15px;
            border:1px solid #2C3A40;
        """)

        estilo_botao = f"""
            QPushButton{{
                background:{COR_VERDE};
                color:white;
                border:none;
                border-radius:12px;
                padding:12px;
                font-size:16px;
                font-weight:bold;
            }}

            QPushButton:hover{{
                background:{COR_VERDE_HOVER};
            }}
        """

        self.btn_sim = QPushButton("Sim")
        self.btn_nao = QPushButton("Não")
        self.btn_sim.setStyleSheet(estilo_botao)
        self.btn_nao.setStyleSheet(estilo_botao)
        self.btn_sim.clicked.connect(lambda: self.avancar(resposta_sim_nao="sim"))
        self.btn_nao.clicked.connect(lambda: self.avancar(resposta_sim_nao="não"))

        self.btn_voltar = QPushButton("Voltar")
        self.btn_avancar = QPushButton("Avançar")
        self.btn_voltar.setStyleSheet(estilo_botao)
        self.btn_avancar.setStyleSheet(estilo_botao)
        self.btn_voltar.clicked.connect(self.voltar)
        self.btn_avancar.clicked.connect(lambda: self.avancar())

        botoes_sim_nao = QHBoxLayout()
        botoes_sim_nao.addWidget(self.btn_sim)
        botoes_sim_nao.addWidget(self.btn_nao)

        botoes_texto = QHBoxLayout()
        botoes_texto.addWidget(self.btn_voltar)
        botoes_texto.addWidget(self.btn_avancar)

        layout = QVBoxLayout()
        layout.addStretch()
        layout.addWidget(self.titulo)
        layout.addSpacing(20)
        layout.addWidget(self.campo_resposta)
        layout.addLayout(botoes_sim_nao)
        layout.addSpacing(30)
        layout.addLayout(botoes_texto)
        layout.addStretch()

        self.setLayout(layout)

        self.mostrar_pergunta_atual()

    def pergunta_atual(self):
        if self.fase == "parte1":
            return PERGUNTAS_PARTE1[self.indice]
        if self.fase == "parte2":
            return PERGUNTAS_PARTE2[self.indice]
        if self.fase == "divida_perguntas":
            return PERGUNTAS_DIVIDA[self.indice_divida]
        return None

    def eh_pergunta_sim_nao(self):
        return self.fase in ("divida_gate", "divida_mais")

    def mostrar_pergunta_atual(self):
        if self.fase == "divida_gate":
            texto = "Você tem alguma dívida atualmente?"
        elif self.fase == "divida_mais":
            texto = "Deseja adicionar outra dívida?"
        else:
            texto = self.pergunta_atual()["texto"]

        self.titulo.setText(texto)

        if self.eh_pergunta_sim_nao():
            self.campo_resposta.hide()
            self.btn_sim.show()
            self.btn_nao.show()
            self.btn_avancar.hide()
        else:
            self.campo_resposta.show()
            self.campo_resposta.clear()
            self.btn_sim.hide()
            self.btn_nao.hide()
            self.btn_avancar.show()

        self.btn_voltar.setEnabled(len(self.historico) > 0)

    def salvar_estado_no_historico(self):
        self.historico.append({
            "fase": self.fase,
            "indice": self.indice,
            "indice_divida": self.indice_divida,
            "divida_atual": dict(self.divida_atual),
            "dividas": list(self.dividas),
        })

    def avancar(self, resposta_sim_nao=None):

        if self.fase == "parte1":
            pergunta = PERGUNTAS_PARTE1[self.indice]
            resposta = self.campo_resposta.text().strip()

            if pergunta["bloco"] in BLOCOS_OBRIGATORIOS and resposta == "":
                QMessageBox.warning(self, "Campo obrigatório", "Essa pergunta precisa ser respondida para continuar.")
                return

            self.salvar_estado_no_historico()
            self.respostas[pergunta["chave"]] = resposta

            if self.indice == len(PERGUNTAS_PARTE1) - 1:
                self.fase = "divida_gate"
            else:
                self.indice += 1

        elif self.fase == "divida_gate":
            self.salvar_estado_no_historico()

            if resposta_sim_nao == "sim":
                self.fase = "divida_perguntas"
                self.indice_divida = 0
                self.divida_atual = {}
            else:
                self.fase = "parte2"
                self.indice = 0

        elif self.fase == "divida_perguntas":
            pergunta = PERGUNTAS_DIVIDA[self.indice_divida]
            resposta = self.campo_resposta.text().strip()

            self.salvar_estado_no_historico()
            self.divida_atual[pergunta["chave"]] = resposta

            if self.indice_divida == len(PERGUNTAS_DIVIDA) - 1:
                self.dividas.append(self.divida_atual)
                self.divida_atual = {}
                self.fase = "divida_mais"
            else:
                self.indice_divida += 1

        elif self.fase == "divida_mais":
            self.salvar_estado_no_historico()

            if resposta_sim_nao == "sim":
                self.fase = "divida_perguntas"
                self.indice_divida = 0
                self.divida_atual = {}
            else:
                self.fase = "parte2"
                self.indice = 0

        elif self.fase == "parte2":
            pergunta = PERGUNTAS_PARTE2[self.indice]
            resposta = self.campo_resposta.text().strip()

            self.salvar_estado_no_historico()
            self.respostas[pergunta["chave"]] = resposta

            if self.indice == len(PERGUNTAS_PARTE2) - 1:
                self.finalizar()
                return
            else:
                self.indice += 1

        self.mostrar_pergunta_atual()

    def voltar(self):
        if not self.historico:
            return

        estado_anterior = self.historico.pop()

        self.fase = estado_anterior["fase"]
        self.indice = estado_anterior["indice"]
        self.indice_divida = estado_anterior["indice_divida"]
        self.divida_atual = estado_anterior["divida_atual"]
        self.dividas = estado_anterior["dividas"]

        self.mostrar_pergunta_atual()

        if not self.eh_pergunta_sim_nao():
            chave = self.pergunta_atual()["chave"]
            if self.fase == "divida_perguntas":
                valor = self.divida_atual.get(chave, "")
            else:
                valor = self.respostas.get(chave, "")
            self.campo_resposta.setText(valor)

    def finalizar(self):
        usuario = carregar_usuario()
        usuario["financeiro"] = self.respostas
        usuario["dividas"] = self.dividas
        salvar_usuario(usuario)

        QMessageBox.information(
            self,
            "Concluído",
            "Questionário finalizado! Suas informações foram salvas."
        )