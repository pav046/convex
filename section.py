from math import sqrt


class Section:
    vert, gor, k, b, y, x = False, False, 0, 0, 0, 0
    x1, x2, y1, y2 = 0, 0, 0, 0

    @staticmethod
    def init(x1=None, y1=None, x2=None, y2=None, reload=False):
        if reload:
            Section._reload()
        if x1 is None:
            x1 = float(input('Введите координату х1 конца отрезка -> '))
        if y1 is None:
            y1 = float(input('Введите координату y1 конца отрезка -> '))
        if x2 is None:
            x2 = float(input('Введите координату x2 конца отрезка -> '))
        if y2 is None:
            y2 = float(input('Введите координату y2 конца отрезка -> '))

        Section.x1, Section.x2, Section.y1, Section.y2 = x1, x2, y1, y2

        if x1 == x2:
            Section.vert = True
            Section.x = x1
        elif y1 == y2:
            Section.gor = True
            Section.y = y1
        elif x1 == 0.0:
            Section.b = y1
            Section.k = (y2 - Section.b) / x2
        else:
            Section.b = (x1 * y2 - x2 * y1) / (x1 - x2)
            Section.k = (y1 - Section.b) / x1

    @staticmethod
    def dist(self):
        if Section.vert:
            Section._vert(self)
        elif Section.gor:
            Section._gor(self)
        else:
            Section.r(self)

    @staticmethod
    def _vert(self):
        a, b, c = 1, -2 * self.y, self.y ** 2 + (Section.x - self.x) ** 2 - 1
        self.distance = Section.discriminant(a, b, c, Section.y1, Section.y2)

    @staticmethod
    def _gor(self):
        a, b, c = 1, -2 * self.x, self.x ** 2 + (Section.y - self.y) ** 2 - 1
        self.distance = Section.discriminant(a, b, c, Section.x1, Section.x2)

    @staticmethod
    def r(self):
        b, k = Section.b, Section.k
        a, b, c = 1 + k ** 2, 2 * k * b - 2 * self.x - 2 * k * self.y,\
            self.x ** 2 + b ** 2 - 2 * b * self.y + self.y ** 2 - 1
        self.distance = Section.discriminant(a, b, c, Section.x1, Section.x2)

    @staticmethod
    def discriminant(a, b, c, start, end):
        res = False
        if start > end:
            start, end = end, start
        d = b ** 2 - 4 * a * c
        if d > 0:
            sqrtd = sqrt(d)
            res1 = (-b + sqrtd) / (2 * a)
            res2 = (-b - sqrtd) / (2 * a)
            if res1 > res2:
                res1, res2 = res2, res1
            if res1 >= end or abs(end - res1) < 0.0000000001\
                    or res2 <= start or abs(start - res2) < 0.0000000001:
                res = False
            else:
                res = True
        return res

    @staticmethod
    def _reload():
        Section.vert, Section.gor = False, False
