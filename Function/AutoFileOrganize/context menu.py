
import sys
import winreg as reg
#파일 설명
#python_script_in_right_click_menu
#Windows에서 마우스 오른쪽 버튼 클릭(컨텍스트 메뉴)에 python 스크립트를 추가하는 스크립트

#지시
#이 스크립트를 실행하기 전에 레지스트리 정보를 편집할 수 있도록 관리자 모드에서 터미널 또는 IDE를 엽니다.

#winreg 모듈은 Windows 레지스트리
#pip install winregistry 의 내용에 액세스하는 데 필요합니다.
#컨텍스트 메뉴에 표시할 나만의 Python 스크립트를 삽입하도록 스크립트 수정



# Get path of current working directory and python.exe
#cwd = os.getcwd() #원래는 이것으로 하려고 했었으나 잘 안되서 임의로 위치를 지정해놓음
python_exe = sys.executable

# optional hide python terminal in windows
hidden_terminal = '\\'.join(python_exe.split('\\')[:-1])+"\\pythonw.exe"


# Set the path of the context menu (right-click menu)
key_path = r'Directory\\Background\\shell\\AutoFileOrganize\\' # Change 'Organiser' to the name of your project

# Create outer key
key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
reg.SetValue(key, '', reg.REG_SZ, '&Organize File in Folder')  # Change 'Organise folder' to the function of your script

# create inner key
key1 = reg.CreateKey(key, r"command")
reg.SetValue(key1, '', reg.REG_SZ, python_exe + f' "C:\\Users\\CDH\\Desktop\\실행할 파일 위치\\program.py"') # cwd의 위치의 program.py를 실행하도록 한다.
#reg.SetValue(key1, '', reg.REG_SZ, hidden_terminal + f' "{cwd}\\file_organiser.py"')  # use to to hide terminal
