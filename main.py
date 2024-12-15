import sys
from random import randint
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsEllipseItem
from PyQt6.QtGui import QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.pushButton = None
        self.graphicsView = None
        uic.loadUi('UI.ui', self)
        self.scene = QGraphicsScene(self)
        self.graphicsView.setScene(self.scene)
        self.pushButton.clicked.connect(self.draw_circle)

    def draw_circle(self) -> None:
        diameter = randint(20, 100)
        x = randint(0, int(self.graphicsView.width()) - diameter)
        y = randint(0, int(self.graphicsView.height()) - diameter)
        ellipse = QGraphicsEllipseItem(x, y, diameter, diameter)
        ellipse.setBrush(QColor(255, 255, 0))
        self.scene.addItem(ellipse)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())