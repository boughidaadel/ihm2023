from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont, QPixmap
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My first Main Window')
        self.setGeometry(100, 100, 300, 400)

        self.menu_bar = self.menuBar()
        # add menus

        file_menu = self.menu_bar.addMenu('File')
        edit_menu = self.menu_bar.addMenu('Edit')
        about_menu = self.menu_bar.addMenu('About')

        # File menu: new, open, save
        new_action = QAction('New', self)
        new_action.setIcon(QIcon('new_icon.svg'))
        new_action.setShortcut('Ctrl+N')
        new_action.triggered.connect(self.new)

        open_action = QAction('Open', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.open)

        save_action = QAction('Save', self)
        save_action.setIcon(QIcon('save_icon.png'))
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save)


        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)

        self.label = QLabel('This is a label widget')
        self.label.setFont(QFont('arial', 14))


        self.label_image = QLabel()

        self.combobox = QComboBox()
        # self.combobox.addItem('Option 1')  # index 0
        # self.combobox.addItem('Option 2')  # index 1
        # self.combobox.addItem('Option 3')  # index 2
        list_items = []
        for i in range(100):
            list_items.append('Option '+str(i))

        #list_items = ['Option '+str(i) for i in range(100)]
        self.combobox.addItems(list_items)
        self.combobox.setCurrentIndex(2)
        self.combobox.currentTextChanged.connect(self.item_changed)


        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.label_image)
        layout.addWidget(self.combobox)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def item_changed(self):
        currenttext = self.combobox.currentText()
        print('You have selected '+currenttext)

    def new(self):
        self.label.setText('you clicked on a new action')

    def open(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open an image', 'C://users/Administrator/Desktop')
        self.label_image.setPixmap(QPixmap(filename))

        self.label.setText('you clicked on a open action')

    def save(self):
        msgbox = QMessageBox()
        msgbox.setText('Are you sure to save the file or no ? ')
        msgbox.setWindowTitle('Save file')
        msgbox.setIcon(QMessageBox.Question) # Information, Critical, Warning, Question
        msgbox.setStandardButtons(QMessageBox.Save|QMessageBox.No|QMessageBox.Cancel)
        msgbox.setDefaultButton(QMessageBox.No)
        msgbox.buttonClicked.connect(self.msgbox_save)
        msgbox.exec_()


    def msgbox_save(self, btn):
        if btn.text() == 'Save':
            self.label.setText('you saved a file with success !')
def main():
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
if __name__ == '__main__':
    main()