def foo2(filenames, params):
    print('foo2')
    print(filenames)
    input()

def foo3(filenames, params):
    print('foo3')
    print(filenames)
    input()

if __name__ == '__main__':
            from context_menu import menus

            cm = menus.ContextMenu('오거나이즈', type='FILES')
            cm2 = menus.ContextMenu('버전 체인지')
            cm3 = menus.ContextMenu('Foo Menu 3')

            cm3.add_items([
                menus.ContextCommand('Foo One', command='echo hello > example.txt'),
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
                cm2,
                menus.ContextCommand('버전 만들기', python=foo3)
            ])

            cm.compile()