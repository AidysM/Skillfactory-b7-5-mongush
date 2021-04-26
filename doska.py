from random import randint


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"({self.x}, {self.y})"


class Ship:
    def __init__(self, bow, l, o):
        self.bow = bow
        self.l = l  # длина корабля
        self.o = o  # ориентация
        self.lives = l

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.l):
            cur_x = self.bow.x
            cur_y = self.bow.y
            if self.o == 0:
                cur_x += i
            elif self.o == 1:
                cur_y += i
            ship_dots.append(Dot(cur_x, cur_y))
        return ship_dots

    def shooten(self, shot):
        return shot in self.dots



    # def get_x2(self):
    #     return self.x2
    #
    # def get_y(self):
    #     return self.y
    #
    # def get_y1(self):
    #     return self.y1
    #
    # def get_y2(self):
    #     return self.y2
    #
    # def set_x(self, x):
    #     return self.x
    #
    # def set_x1(self, x1):
    #     return self.x1
    #
    # def set_x2(self, x2):
    #     return self.x2
    #
    # def set_y(self, y):
    #     return self.y
    #
    # def set_y1(self, y1):
    #     return self.y1
    #
    # def set_y2(self, y2):
    #     return self.y2

# class BigShip(Ship):
#     def __init__(self, x1, y1, x2, y2, x3, y3):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#         self.x3 = x3
#         self.y3 = y3
