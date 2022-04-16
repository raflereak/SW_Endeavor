# Version Manage

# Version Manage 기능 실행하면 현재 파일과 같은 이름의 디렉토리 생성
# 그 디렉토리 안에 파일과 같은 이름의 파일 1 생성
# 최대 5개까지 생성 가능하고 5개 초과 시에 파일 1은 삭제
# 파일 2가 파일 1, 파일 3이 파일 2 등이 되면서 총 파일 개수는 5개로 유지

import os # 디렉토리 생성, 파일 및 디렉토리 경로를 위한 모듈
import shutil # 파일 복사를 위한 모듈 

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8') # 아스키 코드에서 유니코드 형식으로 변경
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


# 디렉토리 생성
def makeDir(self, fileName):
    try:
        if not os.path.exists(fileName): # 현재 파일 이름으로 된 디렉토리가 없으면
            os.makedirs(fileName) # 현재 파일 이름으로 된 디렉토리 생성
            
    except OSError: # 현재 파일 이름으로 된 디렉토리가 존재하는 경우 에러 발생하므로 예외 처리
        pass


# 파일 생성
def makeFile(self, fileName):
    file_path = os.path.realpath(__file__) # 파일의 절대 경로

    dirPath = os.getcwd() # 현재 작업하고 있는 디렉토리 경로 받아오기
    dirList = os.listdir(dirPath) # 현재 경로에 있는 디렉토리 속 디렉토리와 파일 리스트를 dirList 변수에 저장
    dirName = ""

    # 파일 이름과 같은 디렉토리 찾기
    for dir in dirList:
        if dir == fileName:
            if os.path.isdir(dir): pass
            else: dirName = dir
    
    copy_path = dirPath + "\\" + dirName

    shutil.copy(file_path, copy_path) # 원래주소, 복사할 주소
    #shutil.copy2(file_path, copy_path)
    #copy2를 사용하면 파일을 작성한 날짜도 복사, copy는 파일을 작성한 날짜가 복사한 날짜로 변경


# 파일 개수 유지하기
def setFileNum(self):
    dirPath = os.getcwd() # 현재 작업하고 있는 디렉토리 경로 받아오기
    dirList = os.listdir(dirPath) # 현재 경로에 있는 디렉토리 속 디렉토리와 파일 리스트를 dirList 변수에 저장

    # dirList 에 있는 디렉토리 제거
    for file in dirList:
        if os.path.isfile(file): pass
        else: del dirList[file]

    fileCount = len(dirList) # 현재 디렉토리 안에 있는 파일의 개수

    # 파일 개수가 5개가 넘어가는 경우
    if fileCount > 5:
        del dirList[0] # 첫번째 파일 삭제



        