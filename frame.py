from PyQt5.QtWidgets import QApplication, QWidget
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('风电集群')
    window.show()
    app.exec_()
