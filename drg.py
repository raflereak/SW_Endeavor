from PyQt5 import QtWidgets
import calendarProcess
import win32api
import pyautogui
app = QtWidgets.QApplication([])
screen_resolution = app.desktop().screenGeometry()
width, height = screen_resolution.width(), screen_resolution.height()
count = 0


while(True):
    pos = win32api.GetCursorPos()
    x,y = pos
    if(x>(width*0.99)):
        count += 1
        print(count," you complete")
        calendarProcess.st()