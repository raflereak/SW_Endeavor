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
    logging.debug(turple[0] + "에서 " + turple[1] + "(으)로 " + str(turple[2]) + "개 의 파일이 " + str(turple[3]) + "종류별로 정리 되었습니다.")
