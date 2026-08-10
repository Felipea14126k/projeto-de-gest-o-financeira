from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout
)

from PyQt5.QtCore import Qt
from gui.tela_questionario import TelaQuestionario

NOME_APP = "Gestão Financeira"

COR_FUNDO = "#131F24"
COR_VERDE = "#58CC02"
COR_VERDE_HOVER = "#4CAF00"
COR_TEXTO_SECUNDARIO = "#AFAFAF"


class TelaIntroducao(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(NOME_APP)
        self.resize(1000, 650)

        self.setStyleSheet(f"""
            QWidget{{
                background:{COR_FUNDO};
            }}
        """)

        titulo = QLabel("Antes de começar")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("""
            color:white;
            font-size:36px;
            font-weight:bold;
        """)

        texto = QLabel(
            "Agora vamos te fazer algumas perguntas sobre sua renda "
            "e seus gastos, para personalizar o aplicativo para você."
        )
        texto.setAlignment(Qt.AlignCenter)
        texto.setWordWrap(True)
        texto.setStyleSheet(f"""
            color:{COR_TEXTO_SECUNDARIO};
            font-size:16px;
        """)

        btn_prosseguir = QPushButton("Próxima Etapa")
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
        layout.addSpacing(15)
        layout.addWidget(texto)
        layout.addSpacing(30)
        layout.addWidget(btn_prosseguir)
        layout.addStretch()

        self.setLayout(layout)

    def prosseguir(self):
        pass