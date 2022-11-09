if __name__ == '__main__':
    from storage import Storage
else:
    from .storage import Storage

def main():
    storage = Storage()
    menu = {
        1:('Add smth', storage.add),
        2:('Show zoo', storage.showZoo),
        3:("Edit", storage.edit),
        4:("kill", storage.kill),
        5:("killall", storage.killAll),
    }

    while 1:
        for k, v in menu.items():
            print(k, "-", v[0])
        print()
        try:
            point = int(input())
        except ValueError:
            print('Interrupted')
            continue
        if 0 < point <= len(menu):
            menu[point][1]()
        else:
            print('Invalid number')

if __name__ == '__main__':
	main()


