import sys

from PyQt5.QtWidgets import QApplication

from gui.tela_nome import TelaNome


app = QApplication(sys.argv)

janela = TelaNome()
janela.show()

sys.exit(app.exec_())