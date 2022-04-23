from PyQt5 import *
import os #파일명, 폴더명 정보를 읽어오기 위한 모듈
import shutil #파일 이동을 위한 모듈

import winshell
import win32com.client

import sys
import io

from yaml import scan
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8') # 아스키 코드에서 유니코드 형식으로 변경
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

def shortCut():
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

#파일명을 읽어와서 파일명의 분류 부분을 중복없이 리스트화
def fileList(path_before : str)->list :
    file_list = os.listdir(path_before) #폴더의 파일명을 리스트화
    category = [] #분류 데이터 저장을 위해 빈 리스트 생성
    for file in file_list:
        temp_list = file.split(".") #파일명중 "."로 분리하여 리스트화
        category.append(temp_list[-1]) #리스트의 -1 인덱싱 데이터를 category에 추가

    temp_set = set(category) #중복을 제거하기 위해 set 사용
    result = list(temp_set) #중복 제거 후 다시 리스트화
    #print(result)
    return result #결과 리턴


#죄 분류 리스트를 받아와서 정해진 위치에 폴더 생성
def makeFolder(path_after : str, file_list : list):    
    #폴더가 이미 생성되어있다면 오류가 발생하므로 예외처리 진행
    for file in file_list:
        try:
            os.makedirs(path_after+"/"+file)
        except:
            pass

#파일을 폴더 분류에 맞게 이동
def moveFile(path_before, path_after):
    folderlist = os.listdir(path_after)
    filelist = os.listdir(path_before)
    dict = {}

    #파일명에 대한 폴더명을 딕셔너리로 저장
    for file in filelist:
        temp_list = file.split(".")
        dict[file]=temp_list[-1]
     
    #print(dict)
    
    #딕셔너리 정보 활용하여 파일 이동
    cnt = 0
    for key, value in dict.items():
        shutil.move(path_before+"/"+key, path_after+"/"+value)
        cnt +=1
    return cnt
    
def process(_path, _targetPath):
    path_before = r""+_path
    file_list = fileList(path_before)

    #옮길 경로 폴더
    path_after = r""+_targetPath #옮길 위치 직접 지정
    makeFolder(path_after, file_list)
    cnt = moveFile(path_before, path_after)
    return _path, _targetPath, cnt, file_list

def mainProgram():#숏컷과 분류를 선택하는 함수
    choice = input("분류할 방식을 선택하시오(0 or 1) ")
    if (choice == 0):
        process()
    elif(choice == 1):
        shortCut()

mainProgram()
