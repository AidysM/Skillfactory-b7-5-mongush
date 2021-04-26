from doska import Doska, Ship

print("Морской бой")

field = [['o'] * 6 for _ in range(6)]


def show_doska():
    print("  | 1 | 2 | 3 | 4 | 5 | 6 |")
    for i in range(len(field)):
        print(str(i) + ' | ' + ' | '.join(field[i]) + ' |')


show_doska()

# Gamer = Doska()

print("На доске должно быть 1 большой (3 точки), 2 средних (2 точки) и 4 маленьких (1 точка) кораблей.")


def sh_input(f):
    K = []
    while True:
        place = input("Введите координаты корабля (точки в 1 линию):").split()
        if not (len(place) != 6 or len(place) != 4 or len(place) != 2):
            print("Введите координаты по парам")
            continue
        n = len(place)
        for i in range(n):
            if not place[i].isdigit():
                print("Введите числа")
                continue
        if n == 2:
            x1, y1 = map(int, place)
            if not (0 < x1 <= 6 and 0 < y1 <= 6):
                print("Вышли из диапазона")
                continue
            if f[x1][y1] != 'o':
                print("Координаты заняты")
                continue
            K = x1, y1
        elif n == 4:
            x1, y1, x2, y2 = map(int, place)
            if not (0 < x1 <= 6 and 0 < x2 <= 6 and 0 < y1 <= 6 and 0 < y2 <= 6):
                print("Вышли из диапазона")
                continue
            if f[x1][y1] != 'o' and f[x2][y2] != 'o':
                print("Координаты заняты")
                continue
            K = x1, y1, x2, y2
        else:
            x1, y1, x2, y2, x3, y3 = map(int, place)
            if not (0 < x1 <= 6 and 0 < x2 <= 6 and 0 < x3 <= 6 and
                    0 < y1 <= 6 and 0 < y2 <= 6 and 0 < y3 <= 6):
                print("Вышли из диапазона")
                continue
            if f[x1][y1] != 'o' and f[x2][y2] != 'o' and f[x3][y3] != 'o':
                print("Координаты заняты")
                continue
            K = x1, y1, x2, y2, x3, y3
        break
    return K


print()
big_ship = sh_input(field)
# med_ship_1 =
# medium_ship_1 =
