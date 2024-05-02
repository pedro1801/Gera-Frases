from PySide6.QtGui import QIcon
from PySide6.QtCore import QCoreApplication, Qt
from PySide6.QtWidgets import QApplication,QMainWindow, QWidget
from GUI import Ui_MainWindow
import sys

class mainwindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mainwindow,self).__init__()
        self.setupUi(self)
        appincon = QIcon(u"")
        self.setWindowIcon(appincon)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mainwindow()
    window.show()
    app.exec()