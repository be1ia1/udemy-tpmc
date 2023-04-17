from PyQt6.QtWidgets import QApplication, QLabel, \
                            QWidget, QGridLayout, \
                            QLineEdit, QPushButton, \
                            QMainWindow, QTableWidget, \
                            QTableWidgetItem, QDialog, \
                            QVBoxLayout, QComboBox
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt
import sys
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Managment System')
        self.resize(500,400)
        file_menu_item = self.menuBar().addMenu('&File')
        add_student_action = QAction('Add Student', self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)
        help_menu_item = self.menuBar().addMenu('&Help')
        about_action = QAction('About',self)       
        help_menu_item.addAction(about_action)
        edit_menu_item = self.menuBar().addMenu('&Edit')
        search_action = QAction('Search', self)
        search_action.triggered.connect(self.search)
        edit_menu_item.addAction(search_action)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['Id', 'Name', 'Course', 'Mobile'])
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

    def load_data(self):
        connection = sqlite3.connect('database.db')
        result = connection.execute('SELECT * FROM students')
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()

    def search(self):
        search_dialog = SearchDialog()
        search_dialog.exec()

class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Insert Student Data..')
        self.setFixedHeight(300)
        self.setFixedWidth(300)
        layout = QVBoxLayout()
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText('Name')
        self.course_name = QComboBox()
        courses = ['Biology', 'Math', 'Astronomy', 'Physics']
        self.course_name.addItems(courses)
        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText('Mobile')
        button = QPushButton('Submit')
        button.clicked.connect(self.add_student)
        layout.addWidget(self.student_name)
        layout.addWidget(self.course_name)
        layout.addWidget(self.mobile)
        layout.addWidget(button)

        self.setLayout(layout)

    def add_student(self):
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile.text()
        connecion = sqlite3.connect('database.db')
        cursor = connecion.cursor()
        cursor.execute('INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)',
        (name, course, mobile))
        connecion.commit()
        cursor.close()
        connecion.close()
        student_app.load_data()

class SearchDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Search Student..')
        self.setFixedHeight(300)
        self.setFixedWidth(300)
        layout = QVBoxLayout()
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText('')
        button = QPushButton('Submit')
        button.clicked.connect(self.search_student)
        layout.addWidget(self.student_name)
        layout.addWidget(button)

        self.setLayout(layout)
    
    def search_student(self):
        name = self.student_name.text()
        # connection = sqlite3.connect('database.db')
        # cursor = connection.cursor()
        # result = cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
        # rows = list(result)
        # cursor.close()
        # connection.close()
        items = student_app.table.findItems(name, Qt.MatchFlag.MatchFixedString)
        for item in items:
            student_app.table.item(item.row(), 1).setSelected(True)

app = QApplication(sys.argv)
student_app = MainWindow()
student_app.show()
student_app.load_data()
sys.exit(app.exec())