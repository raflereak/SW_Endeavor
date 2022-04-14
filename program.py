#folder_move
import os #파일명, 폴더명 정보를 읽어오기 위한 모듈
import shutil #파일 이동을 위한 모듈

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#파일명을 읽어와서 파일명의 분류 부분을 중복없이 리스트화
def fileList(path_before : str)->list :
    file_list = os.listdir(path_before) #폴더의 파일명을 리스트화
    category = [] #분류 데이터 저장을 위해 빈 리스트 생성
    for file in file_list:
        temp_list = file.split(".") #파일명중 "."로 분리하여 리스트화
        category.append(temp_list[-1]) #리스트의 -1 인덱싱 데이터를 category에 추가

    temp_set = set(category) #중복을 제거하기 위해 set 사용
    result = list(temp_set) #중복 제거 후 다시 리스트화
    print(result)
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
     
    print(dict)
    
    #딕셔너리 정보 활용하여 파일 이동
    for key, value in dict.items():
        shutil.move(path_before+"/"+key, path_after+"/"+value)
    
    


if __name__ == "__main__" :
    #분류할 파일이 있는 위치 폴더
    path_before = r"C:\Users\CDH\Desktop\3학년 수강\SW프로젝트기초\테스트 폴더"
    file_list = fileList(path_before)

    #옮길 경로 폴더
    path_after = r"C:\Users\CDH\Desktop\3학년 수강\SW프로젝트기초\infomation"
    makeFolder(path_after, file_list)
    moveFile(path_before, path_after)