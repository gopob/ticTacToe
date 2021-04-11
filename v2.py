def greeting():
    print("-"*25)
    print("Добро пожаловать в игру крестики-нолики")
    print("-"*25)
    print("Для ввода поля нужно соблюдать формат ввода")
    print("Формат ввода: x y где,")
    print("x - номер строки")
    print("y - номер столбца")
    print("-"*25, end='\n'*3)


def show_fields():
    global fields
    print(f"  0 1 2")
    for i in range(3):
        row_text = " ".join(fields[i])
        print(f"{i} {row_text}")
    print('\n')


def ask():
    while True:
        cords = input("Ваш ход: ").split()

        if len(cords) != 2:
            print("Введите 2 координаты")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите числа")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты находятся вне диапазона")
            continue

        if fields[x][y] != " ":
            print("Клетка занята")
            continue
        return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))

    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(fields[c[0]][c[1]])

        if symbols == ["X", "X", "X"]:
            print("Выиграл X")
            return True

        if symbols == ["0", "0", "0"]:
            print("Выиграл 0")
            return True
    return False


greeting()
fields = [[" "] * 3 for i in range(3)]
counter = 0

while True:
    counter += 1
    show_fields()
    if counter % 2 == 1:
        print("Ходит крестик!")
    else:
        print("Ходит нолик!")

    x, y = ask()

    if counter % 2 == 1:
        fields[x][y] = "X"
    else:
        fields[x][y] = "0"

    if check_win():
        break

    if counter == 9:
        print(" Ничья!")
        break
