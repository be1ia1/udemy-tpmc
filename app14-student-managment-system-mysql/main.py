from PyQt6.QtWidgets import QApplication, QLabel, \
                            QGridLayout, QMessageBox,\
                            QLineEdit, QPushButton, \
                            QMainWindow, QTableWidget, \
                            QTableWidgetItem, QDialog, \
                            QVBoxLayout, QComboBox, \
                            QToolBar, QStatusBar
                            
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt
import sys
import mysql.connector

class DatabaseConnection:
    def __init__(self, host='localhost', 
                       user='root', 
                       password='pythoncourse', 
                       database='school'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        connection = mysql.connector.connect(host=self.host, 
                                             user=self.user, 
                                             password=self.password,
                                             database=self.database)
        return connection

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Managment System')
        self.setMinimumSize(500, 400)
        file_menu_item = self.menuBar().addMenu('&File')
        add_student_action = QAction(QIcon('icons/add.png'),'Add Student', self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)
        help_menu_item = self.menuBar().addMenu('&Help')
        about_action = QAction('About', self)
        help_menu_item.addAction(about_action)
        about_action.triggered.connect(self.about)
        edit_menu_item = self.menuBar().addMenu('&Edit')
        search_action = QAction(QIcon('icons/search.png'), 'Search', self)
        search_action.triggered.connect(self.search)
        edit_menu_item.addAction(search_action)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['Id', 'Name', 'Course', 'Mobile'])
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)
        
        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        toolbar.addAction(add_student_action)
        toolbar.addAction(search_action)

        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)
        self.table.cellClicked.connect(self.cell_clicked)

    def cell_clicked(self):
        edit_button = QPushButton('Edit Record')
        edit_button.clicked.connect(self.edit)

        delete_button = QPushButton('Delete Record')
        delete_button.clicked.connect(self.delete)
        
        children = self.findChildren(QPushButton)
        if children:
            for child in children:
                self.statusbar.removeWidget(child)

        self.statusbar.addWidget(edit_button)
        self.statusbar.addWidget(delete_button)

    def edit(self):
        dialog = EditDialog()
        dialog.exec()

    def delete(self):
        dialog = DeleteDialog()
        dialog.exec()

    def about(self):
        dialog = AboutDialog()
        dialog.exec()

    def load_data(self):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM students')
        result = cursor.fetchall()
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

class AboutDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('About')
        content = """
This app was created during the course 'The Python Mega Course'.
Feel free to modify and reuse this app.
"""
        self.setText(content)

class EditDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Update Student Data..')
        self.setFixedHeight(300)
        self.setFixedWidth(300)
        layout = QVBoxLayout()
        index = student_app.table.currentRow()
        student_name = student_app.table.item(index, 1).text()
        self.student_name = QLineEdit(student_name)
        self.student_name.setPlaceholderText('Name')
        self.student_id = student_app.table.item(index, 0).text()
        course_name = student_app.table.item(index, 2).text()
        self.course_name = QComboBox()
        courses = ['Biology', 'Math', 'Astronomy', 'Physics']
        self.course_name.addItems(courses)
        self.course_name.setCurrentText(course_name)
        mobile_number = student_app.table.item(index, 3).text()
        self.mobile = QLineEdit(mobile_number)
        self.mobile.setPlaceholderText('Mobile')
        button = QPushButton('Submit')
        button.clicked.connect(self.update_student)
        layout.addWidget(self.student_name)
        layout.addWidget(self.course_name)
        layout.addWidget(self.mobile)
        layout.addWidget(button)

        self.setLayout(layout)

    def update_student(self):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute('UPDATE students SET name = %s, course = %s, mobile = %s WHERE id = %s',
                      (self.student_name.text(),
                       self.course_name.itemText(self.course_name.currentIndex()),
                       self.mobile.text(),
                       self.student_id))
        connection.commit()
        cursor.close()
        connection.close()
        student_app.load_data()

class DeleteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Delete Student Data..')

        layout = QGridLayout()

        confirmation = QLabel('Are you sure you want to delete?')
        yes = QPushButton('Yes')
        no = QPushButton('No')

        layout.addWidget(confirmation, 0, 0, 1, 2)
        layout.addWidget(yes, 1, 0)
        layout.addWidget(no, 1, 1)

        self.setLayout(layout)

        yes.clicked.connect(self.delete_student)

        no.clicked.connect(self.close)



    def delete_student(self):
        index = student_app.table.currentRow()
        student_id = student_app.table.item(index, 0).text()
        
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute('DELETE from students WHERE id = %s', (student_id, ))
        connection.commit()
        cursor.close()
        connection.close()
        student_app.load_data()
        self.close()
        confimation_widget = QMessageBox()
        confimation_widget.setWindowTitle('Success')
        confimation_widget.setText('The record was deleted successfully!')
        confimation_widget.exec()

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
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO students (name, course, mobile) VALUES (%s, %s, %s)',
        (name, course, mobile))
        connection.commit()
        cursor.close()
        connection.close()
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
        # connection = DatabaseConnection().connect()
        # cursor = connection.cursor()
        # cursor.execute("SELECT * FROM students WHERE name = %s", (name,))
        # result = cursor.fetchall()
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