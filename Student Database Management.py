from PyQt5 import QtGui , QtCore , QtWidgets
from PyQt5.QtSql import QSqlTableModel , QSqlDatabase , QSqlQueryModel , QSqlQuery
from PyQt5.QtWidgets import QTableView , QVBoxLayout ,  QFormLayout , QMessageBox , QFileDialog
import sys


class test_window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Student Record System')
        self.setGeometry(700,600,1200,700)
        self.move(40,70)
        self.table = QTableView()




        self.sql = QSqlDatabase.addDatabase('QSQLITE')
        self.sql.setDatabaseName('student_record.db')
        self.que = QSqlQuery()
        
        if not self.sql.open():
            print("خطا في فتح الجدول")
            return
        self.que.exec_("CREATE TABLE IF NOT EXISTS student_record(ID INTEGER PRIMARY KEY AUTOINCREMENT,Name TEXT, Age INTEGER, Subject TEXT, Grades REAL)")
    

        self.model = QSqlTableModel(self)
        self.table.setModel(self.model)
        self.model.setTable("student_record")

        self.model.select()
        self.table.setColumnWidth(0,285)
        self.table.setColumnWidth(1,285)
        self.table.setColumnWidth(2,285)
        self.table.setColumnWidth(3,285)

        self.table.setStyleSheet("background-color:#d7f2ee")

        self.name = QtWidgets.QLineEdit(self)
        self.age = QtWidgets.QLineEdit(self)
        self.subject = QtWidgets.QLineEdit(self)
        self.grades = QtWidgets.QLineEdit(self)

        self.add_button = QtWidgets.QPushButton("Add record",self)
        self.add_button.clicked.connect(self.add_student)

        self.delete_button = QtWidgets.QPushButton("Delete record",self)
        self.delete_button.clicked.connect(self.delete_data) 

        self.update_button = QtWidgets.QPushButton("Update record",self)
        self.update_button.clicked.connect(self.update_data)


        
       
        self.form_layout()

    def add_student(self):    
            name1 = self.name.text()
            age1 = self.age.text()
            subject1 = self.subject.text()
            grades1 = self.grades.text()

            if not all([name1, age1, subject1, grades1]):
                    QMessageBox.warning(self, "Input Error", "Please fill in all fields.")
                    return

            self.que.prepare("INSERT INTO student_record (Name,Age,Subject,Grades) VALUES(?,?,?,?)")
            self.que.addBindValue(name1)
            self.que.addBindValue(age1)
            self.que.addBindValue(subject1)
            self.que.addBindValue(grades1)

            if not self.que.exec_():
                 QMessageBox.warning(self,"Error","Faild to add record")
            else:
                self.model.select()
                QMessageBox.information(self,"Success","Data added successfully")


    def form_layout(self):
          
            self.form = QFormLayout()
            self.form.addWidget(self.table)
            self.form.addRow("Name",self.name)
            self.form.addRow("Age",self.age)
            self.form.addRow("Subject",self.subject)
            self.form.addRow("Grades",self.grades)
            self.form.addRow(self.add_button)
            self.form.addRow(self.delete_button)
            self.form.addRow(self.update_button)

            self.qbox = QVBoxLayout()
            self.qbox.addLayout(self.form)
            self.setLayout(self.qbox)

    def delete_data(self):
                  self.row = self.table.currentIndex().row()
                  if self.row < 0:
                        self.model.removeRow(self.row)
                  if self.model.submitAll():
                         reply = QMessageBox.warning(self,"Delete record",'Are you sure !', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                  if reply == QMessageBox.Yes:
                     self.model.removeRow(self.row)
                     if self.model.submitAll():
                        self.model.select()
                        QMessageBox.information(self, "Deleted", "Record deleted successfully.")
                        
                     else:
                        QMessageBox.critical(self, "Error", "Failed to delete record.")
                        self.model.revertAll()
                  else:
                    self.model.revertAll()

    def update_data(self):
                   self.table.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
                   QMessageBox.information(self, "Update", "You can now edit cells directly by double-clicking.")
                   self.model.select()



ap = QtWidgets.QApplication(sys.argv)
window = test_window()
window.show()
ap.exec_()