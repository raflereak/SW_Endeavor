import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("main.ui")[0]

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        # 연결한 Ui를 준비한다.
        self.setupUi(self)
        # 화면을 보여준다.
        self.show()
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()