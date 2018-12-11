import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_file import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)



    def run(self):
       f = open('GAME_SETTINGS.txt', 'w')
       # repson
       if self.radioButton_2.isChecked():
           f.write('1' + '\n')
       elif self.radioButton_3.isChecked():
           f.write('2' + '\n')
       elif self.radioButton_9.isChecked():
           f.write('3' + '\n')
       elif self.radioButton_4.isChecked():
           f.write('4' + '\n')
       elif self.radioButton.isChecked():
           f.write('5' + '\n')
       # rpotiv
       if self.radioButton_6.isChecked():
           f.write('1' + '\n')
       elif self.radioButton_7.isChecked():
           f.write('2' + '\n')
       elif self.radioButton_8.isChecked():
           f.write('3' + '\n')
       # prepyat
       if self.radioButton_10.isChecked():
           f.write('1' + '\n')
       elif self.radioButton_11.isChecked():
           f.write('2' + '\n')
       elif self.radioButton_5.isChecked():
           f.write('3' + '\n')
       # fon
       if self.radioButton_13.isChecked():
           f.write('1' + '\n')
       elif self.radioButton_14.isChecked():
           f.write('2' + '\n')
       elif self.radioButton_12.isChecked():
           f.write('3' + '\n')
       f.close()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

