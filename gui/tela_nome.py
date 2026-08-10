from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QMessageBox
)

from PyQt5.QtCore import Qt

from perfil import criar_usuario
from gui.tela_introducao import TelaIntroducao


NOME_APP = "Gestão Financeira"

COR_FUNDO = "#131F24"
COR_CAIXA = "#1E2A2F"
COR_VERDE = "#58CC02"
COR_VERDE_HOVER = "#4CAF00"
COR_TEXTO_SECUNDARIO = "#AFAFAF"


class TelaNome(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(NOME_APP)
        self.resize(1000, 650)

        self.setStyleSheet(f"""
            QWidget{{
                background:{COR_FUNDO};
            }}
        """)

        titulo = QLabel(NOME_APP)
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("""
            color:white;
            font-size:42px;
            font-weight:bold;
        """)

        boas_vindas = QLabel("Seja bem-vindo ao gerenciador financeiro")
        boas_vindas.setAlignment(Qt.AlignCenter)
        boas_vindas.setStyleSheet(f"""
            color:{COR_TEXTO_SECUNDARIO};
            font-size:16px;
        """)

        self.campo_nome = QLineEdit()
        self.campo_nome.setPlaceholderText("Coloque seu nome")
        self.campo_nome.setStyleSheet(f"""
            background:{COR_CAIXA};
            color:white;
            padding:10px;
            border-radius:8px;
            font-size:15px;
            border:1px solid #2C3A40;
        """)

        btn_prosseguir = QPushButton("Prosseguir")
        btn_prosseguir.setStyleSheet(f"""
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
        """)
        btn_prosseguir.clicked.connect(self.prosseguir)

        layout = QVBoxLayout()

        layout.addStretch()
        layout.addWidget(titulo)
        layout.addWidget(boas_vindas)
        layout.addSpacing(30)
        layout.addWidget(self.campo_nome)
        layout.addWidget(btn_prosseguir)
        layout.addStretch()

        self.setLayout(layout)

    def prosseguir(self):
        nome = self.campo_nome.text().strip()

        sucesso, mensagem = criar_usuario(nome)

        if not sucesso:
            QMessageBox.warning(self, "Erro", mensagem)
            return

        self.introducao = TelaIntroducao()
        self.introducao.show()
        self.close()