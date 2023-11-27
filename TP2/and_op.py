from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5 import uic

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('and_op.ui', self)
        self.submitButton.clicked.connect(self.submit)

    def submit(self):
        op1 = int(self.operand1Combobox.currentText())
        op2 = int(self.operand2Combobox.currentText())
        res = op1 and op2
        self.resultLabel.setText('Result: '+str(op1)+' AND '+str(op2)+' = '+str(res))

def main():
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()