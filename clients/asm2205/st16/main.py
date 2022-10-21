if __name__ == '__main__':
    from group import Group
else:
    from .group import Group


def main():
    group = Group()

    menu = [
        ["Add", group.add],
        ["Add Head Student", group.add_headStudent],
        ["Show", group.ShowGroup],
        ["Edit", group.edit],
        ["Delete", group.delete],
        ["Delete All", group.deleteAll],
        # ["Load", group.load],
    ]

    while True:
        for i, menuItem in enumerate(menu, 1):
            print(f"{i}. {menuItem[0]}")
        try:
            m = int(input())
            menu[m-1][1]()
        except Exception as ex:
            print(ex, "Error.\n")


if __name__ == '__main__':
    main()


