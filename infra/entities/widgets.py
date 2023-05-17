from PySide6.QtWidgets import QGridLayout
from PySide6.QtGui import QPixmap, QPainter

class GridLayoutGremio(QGridLayout):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.background_image = QPixmap(r"C:\Users\Anderson\Documents\MeusProjetos\DesktoqCadastroClientesSQL\imagens/Gremio.png")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.background_image)
        super().paintEvent(event)