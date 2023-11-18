from PyQt5.QtWidgets import * # to import Qt Widgets
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap

def main():
    app = QApplication([]) # click the apps object + manages apps flow, adjusts to user’s desktop settings, adapt to  changes.
    window = QWidget() # new top-level window that can hold and organize other widgets
    window.setWindowTitle("Test PyQt5")
    window.setGeometry(100, 100, 200, 250) # Sets the position to (100, 100) and the size to (800, 600)

    # 1st widget(label)
    label = QLabel() # element1 Label (to display a text or image)
    label.setText("This is a label component!")
    label.setFont(QFont("arial", 12)) # set font to a text with QFont
    # label.move(20, 100) # change the position (20, 50) of the widget (for any QWidget)

    # another label widget (contain image)
    label_image = QLabel()
    label_image.setPixmap(QPixmap("image.png"))


    # 2st widget(textEdit)
    text_box = QTextEdit()
    text_box.setText("This text will be displayed when click on button")
    # 3th widget(lineEdit)
    line_edit = QLineEdit()
    line_edit.text()

    # 4th widget(Button)
    button = QPushButton("Click here! ")
    button.clicked.connect(lambda: click_me(text_box.toPlainText())) # connect button to click_me fonction


    layout = QVBoxLayout() # for horizontal display QHBoxLayout() and for grid we use QGridLayout()
    layout.addWidget(label) #layout.addWidget(label, 0, 0) for grid
    layout.addWidget(label_image)
    layout.addWidget(text_box)
    layout.addWidget(line_edit)
    layout.addWidget(button)

    window.setLayout(layout)
    #
    window.show() # to show the widget (window in this case)
    app.exec_()  #starts the application’s event loop, which waits for and dispatches events or messages in the program

def click_me(msg):
    msg_box = QMessageBox()
    msg_box.setText(msg)
    msg_box.exec_()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
