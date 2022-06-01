import os, datetime
import pandas as pd
import csv
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8') # 아스키 코드에서 유니코드 형식으로 변경
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

def dataGet(_path):
    try:
        csvfile = pd.read_csv('dataset.csv', encoding='cp949')#csv파일이 있는지 확인하기 위해서 사용
    except:
        f = open("dataset.csv", "w", encoding='cp949')#없으면 생성 및 헤더 자동 작성
        f.write("파일명,작성시간,수정시간,확장자,용량,파일경로" + "\n")
        f.close()

    filename = _path#경로나 같은 폴더의 파일명으로 이용가능

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
    a = datetime.datetime.fromtimestamp(atime)
    strc = str(c) #pandas와 비교하기 위하여 str타입으로 변환
    strm = str(m)
    stra = str(a)

    f = open("dataset.csv", 'r', encoding='cp949')
    rdr = csv.reader(f)
    lines = []
    check = False
    
    for line in rdr:
        if (line[0] == name):
            if (line[1] == strc):
                if(line[3] == ext):
                    if(line[5] == filename):
                        line[2] = stra
                        line[4] = size
                        check = True
                    lines.append(line)
                else:
                    lines.append(line)
            else:
                lines.append(line)
        else:
            lines.append(line)
    f = open('dataset.csv', 'w', newline='')
    wr = csv.writer(f)
    wr.writerows(lines)
    f.close()

    if(check == False):
        # f = open("dataset.csv", "w", newline='', encoding='cp949')
        # wr = csv.writer(f)
        # wr.writerows(lines)
        # f.close()
        f = open("dataset.csv", "a", encoding='cp949')
        f.write("%s,%s,%s,%s,%s,%s" % (name,c,a,ext,size,filename) + "\n")
        f.close()


#이름, 확장자, 생성일자, 수정 날짜, 용량가 동일할 때 기록을 갱신할 것
#수정날짜의 경우 최신 날짜가 있으면 기존 과거 데이터 제거 후 추가하는 조건

