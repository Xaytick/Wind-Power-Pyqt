import sys

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QDialog

Stylesheet = """
QPushButton{
    background: rgb(240, 255, 255);
    background-image: url(风车发电.png);
    background-size: 25% 25%;
    background-repeat: no-repeat;
    background-position: left; 
    padding-left: 20px; 
    padding-top: 110px; 
    text-align: left;
}
"""


class Page11(QWidget):

    def __init__(self):
        super().__init__()
        self.setStyleSheet(Stylesheet)
        self.initUi()

    def initUi(self):
        grid = QGridLayout()
        for i in range(16):
            btn = QPushButton(f"机器{i + 1}")
            btn.setMinimumSize(80, 160)
            btn.clicked.connect(self.showDetails)
            grid.addWidget(btn, i // 4, i % 4)
        self.setLayout(grid)
        self.setWindowTitle('机组实时监控')

    def showDetails(self):
        btn = self.sender()
        index = int(btn.text()[-1])
        dialog = DetailDialog(index)
        dialog.exec_()

    def sizeHint(self):
        return QSize(600, 400)


class DetailDialog(QDialog):

    def __init__(self, index):
        super().__init__()
        self.setWindowTitle(f"机器{index}状态")
        # 显示详细信息


if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open('MacOS.qss') as file:
        stylesheet = file.read()
    app.setStyleSheet(stylesheet)
    page = Page11()
    page.resize(page.sizeHint())
    page.show()
    sys.exit(app.exec_())