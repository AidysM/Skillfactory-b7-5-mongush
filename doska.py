class Doska:
    # field = [['o'] * 6 for _ in range(6)]

    def __init__(self, bs, ms1, ms2, ss1, ss2, ss3, ss4):
        self.bs = bs
        self.ms1 = ms1
        self.ms2 = ms2
        self.ss1 = ss1
        self.ss2 = ss2
        self.ss3 = ss3
        self.ss4 = ss4

    def get_bs(self):
        return self.bs

    def set_bs(self, Bs):
        return self.bs

    def get_ms1(self):
        return self.ms1

    def set_ms1(self, ms1):
        return self.ms1

    def get_ms2(self):
        return self.ms2

    def set_ms2(self, ms2):
        return self.ms2


class Ship:
    def __init__(self, x, y, x1='', y1='', x2='', y2=''):
        self.x = x
        self.x1 = x1
        self.x2 = x2
        self.y = y
        self.y1 = y1
        self.y2 = y2

    def get_x(self):
        return self.x

    def get_x1(self):
        return self.x1

    def get_x2(self):
        return self.x2

    def get_y(self):
        return self.y

    def get_y1(self):
        return self.y1

    def get_y2(self):
        return self.y2

    def set_x(self, x):
        return self.x

    def set_x1(self, x1):
        return self.x1

    def set_x2(self, x2):
        return self.x2

    def set_y(self, y):
        return self.y

    def set_y1(self, y1):
        return self.y1

    def set_y2(self, y2):
        return self.y2

# class BigShip(Ship):
#     def __init__(self, x1, y1, x2, y2, x3, y3):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#         self.x3 = x3
#         self.y3 = y3
