import os
# 파이썬 파일의 실행하는 파일의 위치
def apath():
    python_file_path = os.path.dirname(os.path.abspath(__file__))
    parent_dirtory = os.path.dirname(python_file_path)#상위 폴더의 절대 경로값 얻어오기
    parent_dirtory2 = os.path.dirname(parent_dirtory)#상위의 상위폴더...
    return parent_dirtory2