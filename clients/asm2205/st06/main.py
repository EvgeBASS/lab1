if __name__ == '__main__':
    from Staff import Staff
else:
    from .Staff import Staff


def main():
    staff = Staff()

    menu = [
        ["Add", staff.add],
        ["Add trainer master", staff.addMaster],
        ["Show", staff.showStaff],
        ["Edit", staff.edit],
        ["Delete", staff.delete],
        ["Clear", staff.clear],
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


