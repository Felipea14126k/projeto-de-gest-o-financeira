from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QComboBox,
    QMessageBox
)

from PyQt5.QtCore import Qt

from perfil import listar_perfis, carregar_perfil


class Login(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Entrar")
        self.resize(600, 400)

        self.setStyleSheet("""
            QWidget{
                background:#1B1F3B;
            }

            QLabel{
                color:white;
                font-size:16px;
            }

            QComboBox{
                padding:10px;
                font-size:15px;
                border-radius:8px;
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

        titulo = QLabel("Entrar")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("""
            color:white;
            font-size:30px;
            font-weight:bold;
        """)

        self.combo = QComboBox()

        perfis = listar_perfis()

        if perfis:
            self.combo.addItems(perfis)
        else:
            self.combo.addItem("Nenhum perfil encontrado")

        btn_entrar = QPushButton("Entrar")
        btn_entrar.clicked.connect(self.entrar)

        layout = QVBoxLayout()

        layout.addStretch()
        layout.addWidget(titulo)
        layout.addWidget(self.combo)
        layout.addWidget(btn_entrar)
        layout.addStretch()

        self.setLayout(layout)
        
        
        

    def entrar(self):
        nome = self.combo.currentText()

        if nome == "Nenhum perfil encontrado":
          QMessageBox.warning(
            self,
            "Erro",
            "Crie um perfil primeiro."
        )
          return

        perfil = carregar_perfil(nome)

        QMessageBox.information(
        self,
        "Sucesso",
        f"Bem-vindo, {perfil['nome']}!"
    )

