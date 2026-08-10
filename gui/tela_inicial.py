from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout
)

from PyQt5.QtCore import Qt

from gui.login import Login
from gui.criar_perfil import CriarPerfil

from perfil import listar_perfis


class TelaInicial(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestão Financeira")
        self.resize(1000, 650)

        self.setStyleSheet("""
            QWidget{
                background:qlineargradient(
                    x1:0,y1:0,
                    x2:1,y2:1,
                    stop:0 #1B1F3B,
                    stop:1 #121212
                );
            }
        """)

        titulo = QLabel("💰 Gestão Financeira")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("""
            color:white;
            font-size:42px;
            font-weight:bold;
        """)

        subtitulo = QLabel(
            "Organize suas finanças de maneira simples e inteligente."
        )

        subtitulo.setAlignment(Qt.AlignCenter)

        subtitulo.setStyleSheet("""
            color:#BBBBBB;
            font-size:16px;
        """)

        btn_login = QPushButton("Entrar")
        btn_criar = QPushButton("Criar Perfil")

        estilo_botao = """
         QPushButton{
            background:#00C853;
            color:white;
            border:none;
            border-radius:12px;
            padding:12px;
            font-size:16px;
        }

        QPushButton:hover{
            background:#00E676;
        }
        """
        btn_login.setStyleSheet(estilo_botao)
        btn_criar.setStyleSheet(estilo_botao)

        btn_login.clicked.connect(self.entrar)
        btn_criar.clicked.connect(self.criar_perfil)

        #Buscaer os perfis existentes

        if len(listar_perfis()) == 0:
            btn_login.setEnabled(False)
            btn_login.setText("Nenhum perfil disponível")

        btn_login = QPushButton("Entrar")
        btn_criar = QPushButton("Criar Perfil")

        # Buscar os perfis existentes
        perfis = listar_perfis()

        if len(perfis) == 0:
            btn_login.setEnabled(False)
            btn_login.setText("Nenhum perfil disponível")
        layout = QVBoxLayout()

        layout.addStretch()
        layout.addWidget(titulo)
        layout.addWidget(subtitulo)
        layout.addSpacing(30)
        layout.addWidget(btn_login)
        layout.addWidget(btn_criar)
        layout.addStretch()

        self.setLayout(layout)
    

    def entrar(self):
        self.login = Login()
        self.login.show()
        self.close()

    def criar_perfil(self):
        self.tela_criar = CriarPerfil()
        self.tela_criar.show()
        self.close()
    
    