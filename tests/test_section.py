from convex import Void, Segment, Polygon
from r2point import R2Point
from section import Section


class TestPointVoid:

    def setup_method(self):
        Section.init(0, 0, 1, 0)
        self.f = Void()

    # У нульугольника нет вершин, лежащих на расстоянии 1 от отрезка
    def test_null(self):
        assert self.f.N == 0

    # Точка на расстоянии 1 не считается
    def test_point1(self):
        assert self.f.add(R2Point(2, 0)).N == 0

    # Точка, лежащая на расстоянии больше 1, не считается
    def test_point3(self):
        assert self.f.add(R2Point(5, 5)).N == 0

    # Точка, лежащая на расстоянии меньше 1, считается
    def test_point2(self):
        assert self.f.add(R2Point(0.5, 0.5)).N == 1


class TestSegment:

    def setup_method(self):
        Section.init(0, 0, 0, 1, reload=True)
        self.f = Segment(R2Point(2, 0.5), R2Point(-0.9, 0.5), n=0)

    def test_segment(self):
        assert self.f.N == 1

    # Изменяя отрезок, количество вершин,
    # удовлетворяющих условию, может уменьшиться
    def test_segment2(self):
        assert self.f.add(R2Point(-2, 0.5)).N == 0


class TestPolygon:

    def setup_method(self):
        Section.init(0, 0, 1, 1, reload=True)
        self.f = Polygon(R2Point(1, 1), R2Point(1, 0), R2Point(0, 1), n=0)

    def test_polygon1(self):
        assert self.f.N == 3

    # Изменяя многоугольник, количество вершин,
    # удовлетворяющих условию, может увеличиться
    def test_polygon2(self):
        assert self.f.add(R2Point(0, 0)).N == 4

    # Изменяя многоугольник, количество вершин,
    # удовлетворяющих условию, может уменьшиться
    def test_polygon3(self):
        assert self.f.add(R2Point(-1, 2)).add(R2Point(2, -1)).N == 1
