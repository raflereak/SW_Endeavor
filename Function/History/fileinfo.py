import os, datetime
import pandas as pd
import numpy as np
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8') # 아스키 코드에서 유니코드 형식으로 변경
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

def dataGet(_path):
    try:
        csv = pd.read_csv('dataset.csv', encoding='cp949')#csv파일이 있는지 확인하기 위해서 사용
    except:
        f = open("dataset.csv", "a", encoding='cp949')#없으면 생성 및 헤더 자동 작성
        f.write("파일명,작성시간,수정시간,확장자,용량,파일경로" + "\n")
        f.close()

    filename = _path#경로나 같은 폴더의 파일명으로 이용가능

    csv = pd.read_csv("dataset.csv", encoding='cp949')
    # 만든시간을 타임 스탬프로 출력
    ctime = os.path.getctime(filename)#path or filename
    # 수정시간을 타임 스탬프로 출력
    mtime = os.path.getmtime(filename)#path or filename
    # 마지막 엑세스시간을 타임 스탬프로 출력
    atime = os.path.getatime(filename)#path or filename
    # 파일크기
    size = str(os.path.getsize(filename))+"B" #path or filename

    filenames = filename.split('\\')
    names = filenames[-1]#파일 이름+확장자
    exttype = names.split('.')
    name = exttype[0]
    ext = exttype[-1]#확장자
    if (ext == names):
        ext = "folder"
    c = datetime.datetime.fromtimestamp(ctime)
    m = datetime.datetime.fromtimestamp(mtime)
    strc = str(c)
    strm = str(m)
    
    csvdata = csv.to_numpy()
    rows, cols = csvdata.shape
    check = False
    if(check == False):
        for i in range(rows):#이동한 파일이 같은 파일인지 판별하여 csv파일에 기록할지 판별하기 위함
            if(csvdata[i:i+1,0:1] == name):
                if(csvdata[i:i+1,1:2] == strc):
                    if(csvdata[i:i+1,3:4] == ext):
                        if(csvdata[i:i+1,5:6] == filename):
                            csvdata[i:i+1,2:3] = strm
                            csvdata[i:i+1,4:5] = size
                            #df = pd.DataFrame(csvdata)
                            #df.to_csv('dataset.csv', header=False, index=False, encoding='cp949')
                            check = True
                            break
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
    if(check == False):
        f = open("dataset.csv", "a", encoding='cp949')
        f.write("%s,%s,%s,%s,%s,%s" % (name,c,m,ext,size,filename) + "\n")
        f.close()


#이름, 확장자, 생성일자, 수정 날짜, 용량가 동일할 때 기록을 갱신할 것
#수정날짜의 경우 최신 날짜가 있으면 기존 과거 데이터 제거 후 추가하는 조건

