from PyQt5 import QtWidgets , QtCore , QtGui
import sys
import os
application = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()

def create_file():
    le.clear()

def save_file():
    fil , _= QtWidgets.QFileDialog.getSaveFileName(window, "save file", os.path.join(os.path.expanduser('~'), "untitled.txt") , "*.txt")
    if fil:
        with open(fil,'w' ,encoding="utf-8") as folder:
            folder.write(le.toPlainText())
def open_file():
    fil2 , _= QtWidgets.QFileDialog.getOpenFileName(window, "open file" ,os.path.join(os.path.expanduser('~')), "*.txt")
    if fil2:
        with open(fil2, 'r', encoding="utf-8") as folder2:
            r = folder2.read()
            le.setPlainText(r)
def input_text():
    fo , ok = QtWidgets.QFontDialog.getFont()
    if ok:
        le.setCurrentFont(fo)
def input_color():
    color= QtWidgets.QColorDialog.getColor()
    if color.isValid():
        le.setTextColor(color)
def undo():
    le.undo()
window.setWindowTitle("Text Editor")
window.resize(900,700)
def redo():
    le.redo()

le = QtWidgets.QTextEdit(window)
le.setStyleSheet("font-size:25px;")
le.setGeometry(0,10,1000,1000)


main = window.menuBar()
m1 = main.addMenu("File")
m2 = main.addMenu("Edit")
m3 = main.addMenu("View")

a1 = QtWidgets.QAction("New",window)
a2 = QtWidgets.QAction("Open",window)
a3 = QtWidgets.QAction("Save",window)

a1.setShortcut("Ctrl+N")
a2.setShortcut('Ctrl+O')
a3.setShortcut("Ctrl+S")

a1.triggered.connect(create_file)
a2.triggered.connect(open_file)
a3.triggered.connect(save_file)

b1 = QtWidgets.QAction("Change font setting",window)
b2 = QtWidgets.QAction("Change font color", window)
b3 = QtWidgets.QAction("Undo", window)
b4 = QtWidgets.QAction("Redo", window)

# b1.setSeparator(True,window)
# b2.setSeparator(True,window)
# b3.setSeparator(True,window)

b1.setShortcut("Ctrl+F")
b2.setShortcut("Ctrl+C")
b3.setShortcut("Ctrl+U")
b4.setShortcut("Ctrl+R")

b1.triggered.connect(input_text)
b2.triggered.connect(input_color)
b3.triggered.connect(undo)
b4.triggered.connect(redo)

m1.addAction(a1)
m1.addAction(a2)
m1.addAction(a3)

m2.addAction(b1)
m2.addAction(b2)
m2.addAction(b3)
m2.addAction(b4)

window.show()
application.exec_()