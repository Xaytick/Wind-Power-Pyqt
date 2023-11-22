import sys

from PyQt5.QtCore import QSize, Qt, pyqtSignal
from PyQt5.QtWidgets import (QApplication, QMainWindow, QListWidget,
                             QStackedWidget, QWidget, QGridLayout, QSpacerItem, QSizePolicy, QPushButton, QToolBar,
                             QTreeWidget, QHBoxLayout, QTextEdit)
from windpower.page11 import Page11


Stylesheet = """
#sideBar {
    background: rgb(240, 255, 255);
    font-family: "Microsoft YaHei";
    font-size: 16px;
    font-weight: bold;
}
#sideBar::item {
    height: 100px;
    width: 100px;
    display: flex;
    justify-content: center; 
}
QToolBar {
    spacing: 10px;  
    background-image: url(hhu.png);

    background-position: right center;
    background-repeat: no;
}

QToolButton {
    min-width: 26px;
    min-height: 26px;
    border-radius: 10px;
    margin: 20px 20px 2px 166px; /*上右下左*/
}
QToolButton:hover {background: rgb(240, 255, 255);}
QToolButton:pressed {background: rgb(100, 255, 255);}
#Main_Window{
    background: white
}
"""


class MainWindow(QMainWindow):

    login_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('风电集群')
        self.setObjectName('Main_Window')
        self.setWindowFlags(self.windowFlags())
        self.setAutoFillBackground(True)
        self.setStyleSheet(Stylesheet)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        self.initUi()

    def initUi(self):
        self.pages = QStackedWidget(self)
        self.toolbar = QToolBar()
        self.toolbar.addAction('Page 1', lambda: self.pages.setCurrentIndex(0))
        self.toolbar.addAction('Page 2', lambda: self.pages.setCurrentIndex(1))
        self.addToolBar(self.toolbar)
        self.add_page1()
        self.add_page2()

        self.setCentralWidget(self.pages)

    def display(self, index):
        self.stack1.setCurrentIndex(index)

    def add_page1(self):
        self.p1 = QWidget()
        layout = QGridLayout(self.p1)
        side = QListWidget()

        side.setObjectName('sideBar')
        self.stack1 = QStackedWidget()
        layout.addWidget(self.stack1, 0, 1)
        layout.addWidget(side, 0, 0)
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 6)
        side.currentRowChanged.connect(self.display)

        self.p11 = Page11()
        self.stack1.addWidget(self.p11)
        side.addItem('实时监控')

        self.p12 = QWidget()
        self.stack1.addWidget(self.p12)
        side.addItem('AGC控制')

        self.pages.addWidget(self.p1)

    def add_page2(self):
        self.p2 = QWidget()
        self.pages.addWidget(self.p2)

    def sizeHint(self):
        return QSize(1080, 720)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open('MacOS.qss') as file:
        stylesheet = file.read()
    app.setStyleSheet(stylesheet)
    w = MainWindow()
    w.resize(w.sizeHint())
    w.show()
    sys.exit(app.exec_())