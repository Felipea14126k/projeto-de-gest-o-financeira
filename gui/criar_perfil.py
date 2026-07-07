from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QLineEdit,
    QMessageBox
)
from PyQt5.QtCore import Qt

from perfil import criar_perfil


class CriarPerfil(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Criar Perfil")
        self.resize(600, 400)

        self.setStyleSheet("""
            QWidget{
                background:#1B1F3B;
            }

            QLabel{
                color:white;
                font-size:16px;
            }

            QLineEdit{
                padding:10px;
                border-radius:8px;
                font-size:15px;
            }

            QPushButton{
                background:#00C853;
                color:white;
                border:none;
                border-radius:10px;
                padding:10px;
                font-size:15px;
            }

            QPushButton:hover{
                background:#00E676;
            }
        """)

        titulo = QLabel("Criar Perfil")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("""
            color:white;
            font-size:30px;
            font-weight:bold;
        """)

        self.nome = QLineEdit()
        self.nome.setPlaceholderText("Digite seu nome")

        btn_criar = QPushButton("Criar Perfil")
        btn_criar.clicked.connect(self.criar)

        layout = QVBoxLayout()
        layout.addStretch()
        layout.addWidget(titulo)
        layout.addWidget(self.nome)
        layout.addWidget(btn_criar)
        layout.addStretch()

        self.setLayout(layout)

    def criar(self):
        nome = self.nome.text().strip()

        sucesso, mensagem = criar_perfil(nome)

        if sucesso:
            QMessageBox.information(self, "Sucesso", mensagem)
            self.close()
        else:
            QMessageBox.warning(self, "Erro", mensagem)
            return