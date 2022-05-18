import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8') # 아스키 코드에서 유니코드 형식으로 변경
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class QPushButton(QPushButton):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat("application/x-qabstractitemmodeldatalist"):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.setText(e.source().currentItem().text())


class QLineEdit(QLineEdit):
    def __init__(self):
        super(QLineEdit, self).__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat("application/x-qabstractitemmodeldatalist"):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.setText(e.source().currentItem().text())


class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        label_example = QLabel("Select your favorite color")
        label_favorite = QLabel("Drag-and-drop above items to below")

        folder_icon = QIcon("C:\\Users\\CDH\\Desktop\\오버레이 테스트 파일\\Folder_Icon.png")
        
        #아래는 폴더-파일순 선택창
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        filee , check = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()",
                                               "", "All Files (*);;Python Files (*.py);;Text Files (*.txt)")
        #
        tmp = file.split("/")
        folderName = tmp[-1]
        print(folderName)

        tmpp = filee.split("/")
        fileName = tmpp[-1]
        print(fileName)

        

        list_item = QListWidgetItem(folder_icon, folderName)
        lis_item = QListWidgetItem(folder_icon, fileName)

        self.list_example = QListWidget()
        self.list_example.addItem(list_item)
        self.list_example.addItem(lis_item)

        self.list_favorite = QListWidget()

        self.list_example.setDragEnabled(True)
        self.list_favorite.setAcceptDrops(True)

        lineedit = QLineEdit()
        button_name_change = QPushButton("Color")

        button_remove = QPushButton("Remove")
        button_apply = QPushButton("Apply")

        button_remove.clicked.connect(self.remove_selected_item)

        button_layout = QHBoxLayout()
        button_layout.addWidget(button_remove)
        button_layout.addWidget(button_apply)

        layout.addWidget(label_example)
        layout.addWidget(self.list_example)
        layout.addWidget(label_favorite)
        layout.addWidget(self.list_favorite)
        layout.addWidget(lineedit)
        layout.addWidget(button_name_change)
        layout.addLayout(button_layout)
        self.setLayout(layout)
        self.show()

        qust = False# 삭제를 할지 질문할 것인지 선택하는 칸을 따로 만드는 게 좋을 것 같음 현재는 질문없이 바로삭제
    def remove_selected_item(self, qust):
        if (qust == True):
            reply = QMessageBox.question(self, "Question", "Are you sure to remove selected item?", QMessageBox.Yes | QMessageBox.No,
                                            QMessageBox.No)
            if reply == QMessageBox.Yes:
                for item in self.list_favorite.selectedItems():
                    row = self.list_favorite.row(item)
                    self.list_favorite.takeItem(row)
        else:
            for item in self.list_favorite.selectedItems():
                    row = self.list_favorite.row(item)
                    self.list_favorite.takeItem(row)
            


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())

