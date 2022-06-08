
class manageData: # 최초로 불러 올 때 모든 데이터를 받아옵니다. 파일 위치는 아직 정해지지 않았습니다.
    def __init__(self, _target_Path):
        self.targetFile_Path = _target_Path
        forRead = open(self.targetFile_Path, 'r')
        if (forRead.read() == ""):
            forInput_List = ["", "", "False", "", "", "", 1, ""]
        elif (forRead.read() == None):
            forRead = open(self.targetFile_Path, 'w', encoding="utf-8")
            forInput_List = ["", "", "False", "", "", "", 1, ""]
        else :
            forRead = open(self.targetFile_Path, 'r')
            temp = forRead.readlines()
            forInput_List = []
            for i in temp:
                if("=" in i):
                    forInput_List.append(i.split("=")[1].split("\n")[0])
            
        
        # for Orgazie
        self.organize_Path = forInput_List[0]
        self.targetFolder_Path = forInput_List[1]
        self.shortCut = forInput_List[2]
        
        # Version
        self.file = forInput_List[3]
        self.file_Path = forInput_List[4]

        # Package
        self.package_Path = forInput_List[5]
        
        # Order by List
        self.tabSize = forInput_List[6]
        self.tabList = forInput_List[7].split(",")

        # Profile
        self.name = forInput_List[8]
        self.birthday = forInput_List[9]
        self.job = forInput_List[10]
        self.field = forInput_List[11]

        # Setting
        self.calendarShortcutPosition = forInput_List[12]
        self.checkOrganize = self.strBool(forInput_List[13])
        self.checkCalendar = self.strBool(forInput_List[14])
        self.checkSendData = self.strBool(forInput_List[15])
        self.checkOrderByOldest = self.strBool(forInput_List[16])
        self.checkVersion = self.strBool(forInput_List[17])
        self.checkPackage = self.strBool(forInput_List[18])

        self.AllData = forInput_List

    def get_data(self):
        return self.AllData

    def set_data(self, forInput_List):
        # for Orgazie
        self.organize_Path = forInput_List[0]
        self.targetFolder_Path = forInput_List[1]
        self.shortCut = forInput_List[2]
        
        # Version
        self.file = forInput_List[3]
        self.file_Path = forInput_List[4]

        # Package
        self.package_Path = forInput_List[5]
        
        # Order by List
        self.tabSize = forInput_List[6]
        self.tabList = forInput_List[7]

        # Profile
        self.name = forInput_List[8]
        self.birthday = forInput_List[9]
        self.job = forInput_List[10]
        self.field = forInput_List[11]

        # Setting
        self.calendarShortcutPosition = forInput_List[12]
        self.checkOrganize = self.strBool(forInput_List[13])
        self.checkCalendar = self.strBool(forInput_List[14])
        self.checkSendData = self.strBool(forInput_List[15])
        self.checkOrderByOldest = self.strBool(forInput_List[16])
        self.checkVersion = self.strBool(forInput_List[17])
        self.checkPackage = self.strBool(forInput_List[18])

        self.AllData = forInput_List
        
    def strBool(self, _input):
        if(_input == "False"):
            return False
        else:
            return True

    def save_Data(self): # 프로그램이 끝나기 전이나 함수가 실행 된 이후 저장하는 식으로 진행됩니다.
        saveData = open(self.targetFile_Path, 'w')
        saveData.write("# Organize\n")
        saveData.write("organize_Path=" + self.organize_Path + "\n")
        saveData.write("targetFolder_Path=" + self.targetFolder_Path + "\n")
        saveData.write("shortCut=" + self.shortCut + "\n")

        saveData.write("\n")

        saveData.write("# Version\n")
        saveData.write("file=" + self.file + "\n")
        saveData.write("file_Path=" + self.file_Path + "\n")

        saveData.write("\n")

        saveData.write("# Package\n")
        saveData.write("base_Path=" + self.package_Path + "\n")

        saveData.write("\n")

        saveData.write("# Order by List\n")
        saveData.write("tabSize=" + str(self.tabSize) + "\n")
        temp = ""
        for i in self.tabList:
            temp += i + ","
        saveData.write("tabList=" + temp)

        saveData.write("\n")

        saveData.write("# Profile\n")
        saveData.write("name=" + self.name + "\n")
        saveData.write("birthday=" + self.birthday + "\n")
        saveData.write("job=" + self.job + "\n")
        saveData.write("field=" + self.field + "\n")

        saveData.write("\n")

        saveData.write("# Setting\n")
        saveData.write("calendarShortcutPosition=" + self.calendarShortcutPosition + "\n")

        saveData.write("checkOrganize=" + str(self.checkOrganize) + "\n")
        saveData.write("checkCalendar=" + str(self.checkCalendar) + "\n")
        saveData.write("checkSendData=" + str(self.checkSendData) + "\n")
        saveData.write("checkOrderByOldest=" + str(self.checkOrderByOldest) + "\n")
        saveData.write("checkVersion=" + str(self.checkVersion) + "\n")
        saveData.write("checkPackage=" + str(self.checkPackage) + "\n")


        
        

'''
텍스트 파일 포맷
##################################
# Organize
organize_Path=
targetFolder_Path=
shortCut=False

# Version
file=
file_Path=

# Package
base_path=

# Order by List
tabSize=0
tabList=

# Profile
name=
birthday=
job=
field=

# Setting
calendarShortcutPosition=
checkOrganize=
checkCalendar=
checkSendData=
checkOrderByOldest=
checkVersion=
checkPackage=
###################################
'''