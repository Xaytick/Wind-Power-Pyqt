import sys

from PyQt5.QtCore import QSize, Qt, pyqtSignal
from PyQt5.QtWidgets import (QApplication, QMainWindow, QListWidget,
                             QStackedWidget, QWidget, QGridLayout, QSpacerItem, QSizePolicy, QPushButton)
from windpower.page1 import Page1


Stylesheet = """
#leftList{
   background: rgb(240, 255, 255);
}
#leftList {
  font-family: "Microsoft YaHei";
  font-size: 16px;
  font-weight: bold;
}
#leftList::item {
    height: 100px;
    width: 100px;
    display: flex;
    justify-content: center; 
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
        self.left_list = QListWidget()
        self.left_list.currentRowChanged.connect(self.display)
        self.left_list.setObjectName("leftList")
        self.stack = QStackedWidget()
        # 主部件widget
        main_widget = QWidget()
        layout = QGridLayout(main_widget)
        # 使用网格布局添加左右栏
        layout.addWidget(self.left_list, 0, 0)
        layout.addWidget(self.stack, 0, 1)
        # 设置列宽度比例
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 6)
        self.setCentralWidget(main_widget)
        # 测试页面
        self.page1 = Page1()
        self.page2 = QWidget()
        self.stack.addWidget(self.page1)
        self.stack.addWidget(self.page2)
        self.left_list.addItem("Page1")
        self.left_list.addItem("Page2")


    def display(self, index):
        self.stack.setCurrentIndex(index)

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