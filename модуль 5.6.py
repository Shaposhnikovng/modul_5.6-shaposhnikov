def greet():
    print()
    print("-------------------")
    print("  Приветствую Вас  ")
    print("     в игре        ")
    print("  Крестики-нолики  ")
    print("-------------------")
    print()
    print("Формат ввода: X и Y")
    print(" X - номер строки  ")
    print(" Y - номер столбца ")
    print()

def show():
    print()
    print("    | 0 | 1 | 2 | ")
    print("    ------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("    ------------- ")
    print()

def ask():
    while True:
        cords = input("   Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y
#x, y = map(int, input("        Ваш ход: ").split()) - первый вариант
# while x < 0 or x > 0 or y < 0 or y > 2: - первый вариант
# x, y = map(int, input("        Ваш ход: ").split()) - первый вариант
# return x, y - первый вариант
# x, y = map(int, input("        Ваш ход: ").split()) #- третий вариант
# if 0 > x or x > 2 or 0 > y or y > 2: #- третий вариант
#  print(" Координаты вне диапазона ") #- третий вариант
# continue #- третий вариант

# if field[x][y] != " ": #- третий вариант
#   print(" Клетка занята! ") #- третий вариант
#  continue #- третий вариант
# return x, y #- третий вариант
# f 0 <= x <= 2 and 0 <= y <= 2: #- второй вариант
# if field[x][y] == " ": #- второй вариант
#    return x, y # - второй вариант
# else: # - второй вариант
#    print(" Клетка заянта! ") # - второй вариант
# else: # - второй вариант
#   print(" Координаты вне диапазона ") # - второй вариант
def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("  Выиграл Крестик !!! ")
            return True
        if symbols == ["0", "0", "0"]:
            print(" Выиграл Нолик !!! ")
            return True
    return False

greet()
field = [[" "] * 3 for i in range(3)]
num = 0
while True:
    num += 1

    show()

    if num % 2 == 1:
        print(" Ходит крестик ")
    else:
        print(" Ходит нолик")

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = '0'

    if check_win():
        break

    if num == 9:
        break
        print(" Ничья! ")

#  for i in range(3):
#      symbols = []
#      for i in range(3):
#         symbols.append(field[i][j])
#      if symbols == ["X", "X", "X"]:
#         return True

#  for i in range(3):
#      symbols = []
#     for i in range(3):
#         symbols.append(field[j][i])
#     if symbols == ["X", "X", "X"]:
#         return True

#  symbols = []
#  for j in range(3):
#       symbols.append(field[i][i])
#  if symbols == ["X", "X", "X"]:
#         return True

#  symbols = []
#  for j in range(3):
#      symbols.append(field[i][2-i])
#  if symbols == ["X", "X", "X"]:
#      return True


# field = [ # - вариант один
#   [" ", "X", " "], # - вариант один
#  [" ", "X", " "], # - вариант один
# [" ", "X", " "] # - вариант один
# ]  # - вариант один
