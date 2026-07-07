import sys

from PyQt5.QtWidgets import QApplication

from gui.tela_inicial import TelaInicial


app = QApplication(sys.argv)

janela = TelaInicial()
janela.show()

sys.exit(app.exec_())