from logging.config import dictConfig
import logging

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
            'formatter': 'default',
            'encoding' : 'utf-8',
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['file']
    }
})

def myfunc():
    logging.debug("함수가 시작되었습니다.")

def organizeLog(turple): # beforePath, afterPath, howMany, fileList
    logging.debug("[파일 정렬 기능]을 사용하여 " + turple[0] + "에서 " + turple[1] + "(으)로 " + str(turple[2]) + "개의 파일이 " + str(turple[3]) + "종류별로 정리 되었습니다.")

def verLog(turple): # filePath, fileName, file version
    logging.debug("[버전 생성 기능]을 사용하여 " + turple[0] + "의 [" + turple[1] + "]이(가) [버전 " + str(turple[2]) + "] 파일이 생성되었습니다.")

def verChangeLog(turple): # filePath, fileName, targetVer
    logging.debug("[버전 바꾸기 기능]을  사용하여 " + turple[0] + "의 [" + turple[1] + "]이(가) [버전 " + str(turple[2]) + "] (으)로 변경되었습니다.")

def copyAndPaste_File_noneName_Log(turple): # pathPackage, pathTarget
    logging.debug("[패키지 파일 옮기기 기능]을 사용하여 " + turple[0] + "의 파일을 [" + turple[1] +  "] (으)로 옮겼습니다.")

def copyAndPaste_File_Log(turple): # pathPackage, what, name, path_target
    logging.debug("[패키지 파일 옮기기 기능]을 사용하여 " + turple[0] + "의 파일을 [" + turple[1] + "] (이)라는 이름으로 " + turple[2] + "]에 옮겼습니다.")
