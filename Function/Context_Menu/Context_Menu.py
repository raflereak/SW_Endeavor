import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import abspath

from AutoFileOrganize import program

def readtxt():
    testFile1 = open(os.path.join(abspath.apath(), "option.txt"),'r', encoding='utf-8')
    while(True):
        lines = testFile1.readlines()
        if (not lines):
            break
        sp = lines # lines는 데이터가 while에서 빠져나가는 순간 사라지지만 sp는 데이터가 남음
    return sp

def foo2(filenames, params):
    print('foo2')
    print(filenames)
    input()

def beforeFilePath(filename, params):
    testFile1 = open(os.path.join(abspath.apath(), "option.txt"),'r', encoding='utf-8')
    sp = readtxt()
    testFile1.close()

    sp[1] = "organize_Path="+filename[0]+"\n" #수정할 내용

    testFile2 = open(os.path.join(abspath.apath(), "option.txt"),'w', encoding='utf-8')
    for i in sp:
        testFile2.write(i)
    testFile2.close()
    
    print('before : ',filename)
    print(filename[0])
    print(abspath.apath())#옵션 위치
    input()

def afterFilePath(filename, params):
    testFile1 = open(os.path.join(abspath.apath(), "option.txt"),'r', encoding='utf-8')
    sp = readtxt()
    testFile1.close()

    sp[2] = "targetFolder_Path="+filename[0]+"\n"

    testFile2 = open(os.path.join(abspath.apath(), "option.txt"),'w', encoding='utf-8')
    for i in sp:
        testFile2.write(i)
    testFile2.close()

    print('after : ',filename)
    print(filename[0])
    print(abspath.apath())#옵션 위치
    input()

def filemove(filenames, params):
    testFile1 = open(os.path.join(abspath.apath(), "option.txt"),'r', encoding='utf-8')
    sp = readtxt()
    testFile1.close()
    before = sp[1][14:] #이동할 경로
    after = sp[2][18:] #이동될 경로
    print(before)
    print(after)
    program.process(before, after)
    print("filemove")
    input()

def shortcut(filenames, params):
    before = beforeFilePath()
    after = filenames[0]
    program.process(before, after)
    print("shortcut")
    input()


if __name__ == '__main__':
    from context_menu import menus

    cm = menus.ContextMenu('오거나이즈', type='DIRECTORY_BACKGROUND')
    cm2 = menus.ContextMenu('버전 체인지')
    cm3 = menus.ContextMenu('이동 받을 경로 설정')


    cm3.add_items([
        menus.ContextCommand('filemove', python=filemove)
    ])
    cm3.add_items([
        menus.ContextCommand('shortcut', python=shortcut)
    ])

    cm2.add_items([
        menus.ContextCommand('버전1', python=foo2)
    ])
    cm2.add_items([
        menus.ContextCommand('버전2', python=foo2)
    ])
    cm2.add_items([
        menus.ContextCommand('버전3', python=foo2)
    ])
    cm2.add_items([
        menus.ContextCommand('버전4', python=foo2)
    ])
    cm2.add_items([
        menus.ContextCommand('버전5', python=foo2)
    ])

    
    cm.add_items([
        cm2, cm3,
        menus.ContextCommand('버전 만들기', python=foo2)
    ])
    cm.add_items([
        cm2,
        menus.ContextCommand('이동 할 경로 설정', python=beforeFilePath),
        cm3
    ])
    
    
    cm.compile()