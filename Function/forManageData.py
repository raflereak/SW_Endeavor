
class manageData: # 최초로 불러 올 때 모든 데이터를 받아옵니다. 파일 위치는 아직 정해지지 않았습니다.
    def __init__(self, _target_Path):
        self.targetFile_Path = _target_Path
        forRead = open(self.targetFile_Path, 'r')
        if (forRead.read() == ""):
            forInput_List = ["", "", "False", "", "", 1, ""]
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
        
        # Order by List
        self.tabSize = forInput_List[5]
        self.tab = forInput_List[6]
        self.tabList = self.tab.split(",")
        

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
        saveData.write("# Order by List\n")
        saveData.write("tabSize=" + str(self.tabSize) + "\n")
        saveData.write("tab=" + str(self.tab))
        

'''
텍스트 파일 포맷
##################################
# Organize
organize_Path = test
targetFolder_Path = tt
shortCut = False

# Version
file = asd
file_Path = dddd

# Order by List
tabSize = 2
tab1 = 1
tab2 = 3
###################################
'''