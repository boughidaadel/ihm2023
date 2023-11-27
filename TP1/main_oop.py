#same code as main.py (with OOP paradigm)

from PyQt5.QtWidgets import * # to import Qt Widgets
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test PyQt5")
        self.setGeometry(100, 100, 200, 250)  # Sets the position to (100, 100) and the size to (800, 600)

        # 1st widget(label)
        self.label = QLabel() # element1 Label (to display a text or image)
        self.label.setText("This is a label component!")
        self.label.setFont(QFont("arial", 12)) # set font to a text with QFont
        # label.move(20, 100) # change the position (20, 50) of the widget (for any QWidget)

        # another label widget (contain image)
        self.label_image = QLabel()
        self.label_image.setPixmap(QPixmap("image.png"))


        # 2st widget(textEdit)
        self.text_box = QTextEdit()
        self.text_box.setText("This text will be displayed when click on button")

        # 3th widget(lineEdit)
        self.line_edit = QLineEdit()
        self.line_edit.text()

        # 4th widget(Button)
        self.button = QPushButton("Click here! ")
        self.button.clicked.connect(self.click_me) # connect button to click_me fonction


        layout = QVBoxLayout() # for horizontal display QHBoxLayout() and for grid we use QGridLayout()
        layout.addWidget(self.label) #layout.addWidget(label, 0, 0) for grid
        layout.addWidget(self.label_image)
        layout.addWidget(self.text_box)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def click_me(self):
        print("bla bla")
        msg_box = QMessageBox()
        msg_box.setText(self.text_box.toPlainText())
        msg_box.exec_()
def main():
    app = QApplication([]) # click the apps object + manages apps flow, adjusts to user’s desktop settings, adapt to  changes.
    window = MainWindow() # new top-level window that can hold and organize other widgets

    window.show() # to show the widget (window in this case)
    app.exec_()  #starts the application’s event loop, which waits for and dispatches events or messages in the program



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
