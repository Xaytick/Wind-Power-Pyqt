import sys

from PyQt5.QtCore import QSize, Qt, pyqtSignal
from PyQt5.QtWidgets import (QApplication, QMainWindow, QListWidget,
                             QStackedWidget, QWidget, QGridLayout, QSpacerItem, QSizePolicy, QPushButton, QToolBar,
                             QTreeWidget)
from windpower.page1 import Page1


Stylesheet = """
#topBar {
    height: 30px;
    width: 80px;
    background-color: rgb(240, 255, 255);
    spacing: 10px; /* 项目间距 */
    padding: 5px; /* 内边距 */
}
#topBar::item {
    height: 100px;
    width: 100px;
    display: flex;
    justify-content: center; 
}
#leftList {
    background: rgb(240, 255, 255);
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
        self.top_bar = QListWidget()
        self.left_stacked = QStackedWidget()
        self.left1 = QListWidget()
        self.left2 = QTreeWidget()
        self.top_bar.itemClicked.connect(self.change_left_bar)
        self.top_bar.setObjectName('topBar')

        self.left_stacked.addWidget(self.left1)
        self.left_stacked.addWidget(self.left2)

        self.left_list = QListWidget()
        self.left_list.currentRowChanged.connect(self.display)
        self.left_list.setObjectName('leftList')
        self.stack = QStackedWidget()

        main_widget = QWidget()
        # 添加上边栏
        layout = QGridLayout(main_widget)
        layout.addWidget(self.top_bar, 0, 0, 1, 2)
        # 添加左边栏
        layout.addWidget(self.left_list, 1, 0)
        layout.addWidget(self.stack, 1, 1)
        # 设置列宽度比例 !!!
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 6)

        self.setCentralWidget(main_widget)
        # 测试页面
        self.page1 = Page1()
        self.page2 = QWidget()
        self.stack.addWidget(self.page1)
        self.stack.addWidget(self.page2)
        self.left_list.addItem('实时监控')
        self.left_list.addItem('AGC控制')


    def display(self, index):
        self.stack.setCurrentIndex(index)

    def change_left_bar(self, index):
        self.left_stacked.setCurrentIndex(index)

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