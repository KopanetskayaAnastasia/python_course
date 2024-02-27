'''вариант 5'''


class Rectangle:
    def __init__(self, ident, p1, p2):
        self.ident = ident
        if len(p1) != 2:
            raise ValueError("Создание объекта невозможно. Введите 2 координаты для p1")
        else:
            self.p1 = p1
        if len(p2) != 2:
            raise ValueError("Создание объекта невозможно. Введите 2 координаты для p2")
        else:
            self.p2 = p2

    def square(self):
        width = abs(self.p1[0] - self.p2[0])
        height = abs(self.p1[1] - self.p2[1])
        return width * height

    def points(self):
        return [self.p1, self.p2, [self.p1[0], self.p2[1]], [self.p2[0], self.p1[1]]]

    def set_p1(self, x, y):
        self.p1[0] += x
        self.p1[1] += y

    def set_p2(self, x, y):
        self.p2[0] += x
        self.p2[1] += y

    def top_l(self):
        x = min(self.p1[0], self.p2[0])
        y = max(self.p1[1], self.p2[1])
        return [x, y]

    def bot_r(self):
        x = max(self.p1[0], self.p2[0])
        y = min(self.p1[1], self.p2[1])
        return [x, y]


class Pentagon:
    def __init__(self, ident, points):
        self.ident = ident
        if len(points) != 5 or any(len(point) != 2 for point in points):
            raise ValueError("Создание обЪекта невозможно. Введите 5 вершин, в каждой 2 координаты")
        else:
            self.points = points

    def set_points(self, x, y):
        for i in self.points:
            i[0] += x
            i[1] += y

    def min_x(self):
        x = self.points[0][0]
        for i in self.points:
            if i[0] < x:
                x = i[0]
        return x

    def max_x(self):
        x = self.points[0][0]
        for i in self.points:
            if i[0] > x:
                x = i[0]
        return x

    def min_y(self):
        y = self.points[0][1]
        for i in self.points:
            if i[1] < y:
                y = i[1]
        return y

    def max_y(self):
        y = self.points[0][1]
        for i in self.points:
            if i[1] > y:
                y = i[1]
        return y


def move(t, x, y):
    if isinstance(t, Rectangle):
        t.set_p2(x, y)
        t.set_p1(x, y)
    if isinstance(t, Pentagon):
        t.points(x, y)


def is_include_r_p(r,p):
    if p.max_y() <= r.top_l()[1] and p.max_x() <= r.bot_r()[0] and p.min_y() >= r.bot_r()[1] and p.min_x() >= r.top_l()[0]:
        print("Прямоугольник включает пятиугольник")
    elif p.max_y() >= r.top_l()[1] and p.max_x() >= r.bot_r()[0] and p.min_y() <= r.bot_r()[1] and p.min_x() <= r.top_l()[0]:
        print("Пятиугольник включает прямоугольник")


def is_include(t1, t2):
    if isinstance(t1, Rectangle) and isinstance(t2, Pentagon):
        is_include_r_p(t1, t2)
    elif isinstance(t2, Rectangle) and isinstance(t1, Pentagon):
        is_include_r_p(t2, t1)
    elif isinstance(t1, Rectangle) and isinstance(t2, Rectangle):
        if t1.top_l()[0] <= t2.top_l()[0] and t1.top_l()[1] >= t2.top_l()[1] and t1.bot_r()[0] >= t2.bot_r()[0] and t1.bot_r()[1] <= t2.bot_r()[1]:
            print("Прямоугольник т1 включает т2")
        elif t1.top_l()[0] >= t2.top_l()[0] and t1.top_l()[1] <= t2.top_l()[1] and t1.bot_r()[0] <= t2.bot_r()[0] and t1.bot_r()[1] >= t2.bot_r()[1]:
            print("Прямоугольник т2 включает т1")
    elif isinstance(t1, Pentagon) and isinstance(t2, Pentagon):
        if t1.min_x() <= t2.min_x() and t1.min_y() <= t2.min_y() and t1.max_x() >= t2.max_x() and t1.max_y() >= t2.max_y():
            print("Пятиугольник т1 включает т2")
        elif t1.min_x() >= t2.min_x() and t1.min_y() >= t2.min_y() and t1.max_x() <= t2.max_x() and t1.max_y() <= t2.max_y():
            print("Пятиугольник т2 включает т1")
    else:
        print("Не включает")

figure = []
s = int(input("Введите количество фигур: "))
for i in range(s):
    code = int(input("Введите код фигуры: 1 - прямоугольник, 2 - пятиугольник: "))
    if code == 1:
        print("Введите 2 точки для прямоугольника: ")
        points = []
        for j in range(2):
            x = int(input())
            y = int(input())
            points.append([x, y])
        figure.append(Rectangle(i, points[0], points[1]))
    if code == 2:
        print("Введите 5 точек для пятиугольника: ")
        points = []
        for j in range(5):
            x = int(input())
            y = int(input())
            points.append([x, y])
        figure.append(Pentagon(i, points))
f1 = int(input("Введите номер фигуры 1: "))
f2 = int(input("Введите номер фигуры 2: "))
is_include(figure[f1], figure[f2])




