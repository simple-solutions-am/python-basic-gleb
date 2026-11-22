commands = [("add", "Макс", "+7 900 123-45-67"), ("add", "Глеб", "+7 911 765-43-21"), ("find", "Глеб"), ("find", "Илья"), ("del", "Макс"), ("del", "Денис"), ("add", "Саша", "+7 922 111-22-33"), ("list",)]
book = {}
for i in commands:
    if i[0] == "add":
        print(f"Сохранил:{i[1]}")
        book[i[1]] = i[2]
    elif i[0] == "find":
        if book.get(i[1]) is None:
            print(f"{i[1]}: такого контакта нет")
        else:
            print(f"{i[1]}:{book.get(i[1])}")
    elif i[0] == "del":
        if book.get(i[1]) is None:
            print(f"{i[1]}: такого контакта нет")
        else:
            del book[i[1]]
            print(f"Удалил: {i[1]}")
    elif i[0] == "list":
        for i, x in book.items():
            print(f"{i}: {x}")
