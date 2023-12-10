from PyQt5.QtWidgets import *
from PyQt5 import uic

import sqlite3

conn = sqlite3.connect('users.db') # connect with db if exist (and create db if not exist)
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY,
                       fullname TEXT,
                       email TEXT,
                       password TEXT,
                       gender TEXT)
""")

class showWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('show_users.ui', self)
        self.setWindowTitle("List of users")
        #self.tableWidget
        cur.execute("SELECT id, email, fullname, gender FROM user")
        rows = cur.fetchall()
        self.tableWidget.setRowCount(len(rows))
        self.removeButton.clicked.connect(self.remove_users)
        for i, row in enumerate(rows):
            id = row[0]
            email = row[1]
            fullname = row[2]
            gender = row[3]
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(id)))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(fullname))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(email))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(gender))

            # add checkbox
            checkbox = QCheckBox()
            # checkbox.setText("Remove ?")
            checkbox.setChecked(False)
            self.tableWidget.setCellWidget(i, 4, checkbox)

    def remove_users(self):
        list_id = []
        for i in range(self.tableWidget.rowCount()):
            checkbox = self.tableWidget.cellWidget(i, 4)
            if checkbox.isChecked():
                id = int(self.tableWidget.item(i, 0).text())
                list_id.append((id, ))
        print(list_id)
        cur.executemany("DELETE FROM user WHERE id=?", list_id)
        conn.commit()
        print("You have deleted the users ", list_id)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle("Login users")
        self.signupButton.clicked.connect(self.signup)
        self.loginButton.clicked.connect(self.login)
        self.showButton.clicked.connect(self.show_users)

    def show_users(self):
        self.show_window = showWindow()
        self.show_window.show()
    def login(self):
        email = self.emailLineEdit.text()
        password = self.passwordLineEdit.text()
        cur.execute("SELECT * FROM user WHERE email=? AND password=?", (email, password))
        rows = cur.fetchall()
        if len(rows) == 1:
            print("login with success ! ")
        else:
            print("login failed !")
    def signup(self):
        messagebox = QMessageBox()
        messagebox.setWindowTitle("Sign Up")
        if self.passwordLineEdit_2.text() == self.confirmLineEdit.text(): # email exists + len(password) ....
            fullname = self.nameLineEdit.text()
            password = self.passwordLineEdit_2.text()
            email = self.emailLineEdit_2.text()
            if self.maleRadio.isChecked():
                gender = self.maleRadio.text() # Male
            elif self.femaleRadio.isChecked():
                gender = self.femaleRadio.text() # Female
            cur.execute("INSERT INTO user (fullname, email, password, gender) VALUES (?, ?, ?, ?)", (fullname, email, password, gender))
            conn.commit()
            messagebox.setText("User added with success!")
            messagebox.setIcon(QMessageBox.Information)
        else:
            messagebox.setText("Sign Up failed !")
            messagebox.setIcon(QMessageBox.Critical)
        messagebox.exec_()
def main():
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()


