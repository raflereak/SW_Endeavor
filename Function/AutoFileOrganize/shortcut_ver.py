import os
import winshell
import win32com.client

def shortcut(path):
    desktop = winshell.desktop()
    #desktop = r"path to where you wanna put your .lnk file"

    path = os.path.join(desktop, 'test file.lnk') #데스크탑에 만들 바로가기의 이름. 뒤에 .lnk 혹은 .url로 지정
    #파일명 지정시 주의사항 : 바로가기를 생성할 위치에 같은 이름이 있을 경우 덮어쓰기를 해버림

    target = r"C:\Users\CDH\Desktop\3학년 수강\SW프로젝트기초\gui\test.txt" #주소+이름+확장자까지 작성하여 바로가기를 만들 파일을 지정
    icon = target #사용할 아이콘을 위 경로의 파일과 같은 아이콘으로 지정. 따로 지정하고 싶을 경우 위와같이 주소를 지정해주면 됨

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.IconLocation = icon
    shortcut.save()