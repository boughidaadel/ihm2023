from PyQt5.QtWidgets import *
from PyQt5 import uic

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle("Display message after login")

        self.loginButton.clicked.connect(self.login)
        self.showButton.clicked.connect(self.show_message)

    def login(self):
        if self.usernameTextEdit.text() == 'adel' and self.passwordTextEdit.text() == '123321':
            self.messageTextEdit.setEnabled(True)
            self.showButton.setEnabled(True)
        else:
            message_failed = QMessageBox()
            message_failed.setText('Username or password incorect ! ')
            message_failed.exec_()

    def show_message(self):
        show_msg_box = QMessageBox()
        show_msg_box.setText(self.messageTextEdit.toPlainText())
        show_msg_box.exec_()
def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()



if __name__ == '__main__':
    main()