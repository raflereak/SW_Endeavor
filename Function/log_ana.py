from typing import Any, Optional
Files = open('')

def Files_analyze(Files: Optional[str]) -> bool:
    """ls
    
    파일 안에 머가 있는지 분석, 추출하는 함수
    """
    # ""안에 있는 워드를 찾기
    searchTarget = ""
    cnt = 0
    for i in Files.readlines():
        if searchTarget in i:
            print("[" + str(cnt) + "]" + i)
        cnt += 1
print(Files_analyze(Files))