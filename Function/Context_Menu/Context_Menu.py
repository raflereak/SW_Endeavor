import glob
import os

def foo2(filenames, params):
    print('foo2')
    print(filenames)
    input()

def FilePath(filename, params):
    testFile1 = open(os.path.join(os.path.dirname(filename[0]), "test.txt"),'w') # w: write 쓴다path.join(file, filename)
    testFile1.write(filename[0])
    # filepath = os.path.join(file, filename)
    
    print('불러온 경로 : ',filename)
    print(filename[0])
    testFile1.close()
    input()
    
if __name__ == '__main__':
            from context_menu import menus

            cm = menus.ContextMenu('오거나이즈', type='DIRECTORY_BACKGROUND')
            cm2 = menus.ContextMenu('버전 체인지')
            

        
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
                cm2,
                menus.ContextCommand('버전 만들기', python=foo2)
            ])
            cm.add_items([
                cm2,
                menus.ContextCommand('이동 할 경로 설정', python=FilePath)
            ])
            cm.add_items([
                cm2,
                menus.ContextCommand('이동 받을 경로 설정', python=FilePath)
            ])

            cm.compile()