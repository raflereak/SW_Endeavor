import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QCalendarWidget
from PyQt5.QtCore import QDate
import keyboard

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())

        vbox = QVBoxLayout()
        vbox.addWidget(cal)
        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setWindowTitle('QCalendarWidget')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def showDate(self, date):
        self.lbl.setText(date.toString())



def Start():
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = MyApp()
        sys.exit(app.exec_())

def premise(): 
    while(True):
        if(keyboard.read_key() == "space"):#스페이스바를 눌렀을때 캘린더 출력
            Start()
premise()