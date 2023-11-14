
try:
    from PyQt5.QtCore import Qt, QSize, QTimer
    from PyQt5.QtWidgets import QDialog, QVBoxLayout, QWidget, \
    QGraphicsDropShadowEffect, QPushButton, QGridLayout, QSpacerItem, \
    QSizePolicy, QApplication, QLabel, QLineEdit, QCheckBox, QHBoxLayout
except ImportError:
    from PySide2.QtCore import Qt, QSize, QTimer
    from PySide2.QtWidgets import QDialog, QVBoxLayout, QWidget, \
        QGraphicsDropShadowEffect, QPushButton, QGridLayout, QSpacerItem, \
        QSizePolicy, QApplication

Stylesheet = """
#Custom_Dialog {
    background-color: rgba(255, 255, 255, 180);
}

#Custom_Widget {
    background-image: url(R-C.png);
    background-size: contain;
    background-position: left;
    border-radius: 10px;
}

#closeButton {
    min-width: 26px;
    min-height: 26px;
    font-family: "Webdings";
    qproperty-text: "r";
    border-radius: 10px;
}
#closeButton:hover {
    color: white;
    background: red;
}
"""


class Dialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(Dialog, self).__init__(*args, **kwargs)
        self.setWindowTitle('登录')
        self.setObjectName('Custom_Dialog')
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAutoFillBackground(True)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet(Stylesheet)
        self.initUi()
        # 添加阴影
        # effect = QGraphicsDropShadowEffect(self)
        # effect.setBlurRadius(20)
        # effect.setOffset(0, 0)
        # effect.setColor(Qt.gray)
        # self.setGraphicsEffect(effect)

    def initUi(self):
        # 重点： 这个widget作为背景和圆角
        self.username_label = QLabel('用户')
        self.password_label = QLabel('密码')
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.remember_me = QCheckBox('记住我')
        self.login_button = QPushButton('登录')
        self.forgot_password_button = QPushButton('忘记密码?')
        self.widget = QWidget(self)
        self.widget.setObjectName('Custom_Widget')
        layout = QVBoxLayout(self)
        layout.addWidget(self.widget)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password)
        layout.addWidget(self.remember_me)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.login_button)
        button_layout.addWidget(self.forgot_password_button)
        layout.addLayout(button_layout)
        self.setLayout(layout)
        # 在widget中添加ui
        layout = QGridLayout(self.widget)
        layout.addItem(QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum), 0, 0)
        layout.addWidget(QPushButton(
            'r', self, clicked=self.accept, objectName='closeButton'), 0, 1)
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum,
                                   QSizePolicy.Expanding), 1, 0)

    def sizeHint(self):
        return QSize(300, 400)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    with open('login.qss') as file:
        stylesheet = file.read()
    app.setStyleSheet(stylesheet)
    w = Dialog()
    w.resize(w.sizeHint())
    w.exec_()
    QTimer.singleShot(200, app.quit)
    sys.exit(app.exec_())
