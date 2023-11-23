import sys

from PyQt5.QtCore import QSize, QSettings
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QDialog, QLabel, QLineEdit

Stylesheet = """
QLineEdit {
    max-width: 100px;  
}
QLable {
    max-width: 100px; 
}
QPushButton {
    min-height: 20px;
    max-width: 60px;  
}
QWidget {
    max-width: 300px;  
    max-height: 300px; 
    alignment: center;

}
"""


class Page12(QWidget):

    def __init__(self):
        super().__init__()
        self.setStyleSheet(Stylesheet)
        self.initUi()

    def initUi(self):
        self.page12 = QWidget()
        layout = QGridLayout(self.page12)
        self.agc_status_lable = QLabel('AGC投切状态')
        self.plan_power_lable = QLabel('有功计划值（kW）')
        self.dispatch_status_lable = QLabel('调度通信状态')
        self.allocate_method_lable = QLabel('分配方式')
        self.agc_status = QLineEdit('切入')
        self.plan_power = QLineEdit('2300')
        self.dispatch_status = QLineEdit('通信正常')
        self.allocate_method = QLineEdit('平均')
        self.confirm_button = QPushButton('确认')

        layout.addWidget(self.agc_status_lable, 0, 0)
        layout.addWidget(self.plan_power_lable, 1, 0)
        layout.addWidget(self.dispatch_status_lable, 2, 0)
        layout.addWidget(self.allocate_method_lable, 3, 0)
        layout.addWidget(self.agc_status, 0, 1)
        layout.addWidget(self.plan_power, 1, 1)
        layout.addWidget(self.dispatch_status, 2, 1)
        layout.addWidget(self.allocate_method, 3, 1)
        layout.addWidget(self.confirm_button, 4, 1)
        self.setLayout(layout)
        self.setWindowTitle('AGC控制')

    def sizeHint(self):
        return QSize(300, 400)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open('MacOS.qss') as file:
        stylesheet = file.read()
    app.setStyleSheet(stylesheet)
    page = Page12()
    page.resize(page.sizeHint())
    page.show()
    sys.exit(app.exec_())