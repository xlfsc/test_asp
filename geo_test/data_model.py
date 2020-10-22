from pyDatalog import pyDatalog


class Express

class Point(pyDatalog.Mixin):
    def __int__(self, name):
        super(Point, self).__init__()
        self.name = name

    def __repr__(self):
        return self.name


class Segment(pyDatalog.Mixin):
    def __init__(self, point_A: Point, point_B: Point, length=None):
        super(Segment, self).__init__()

        self.name = '{}{}'.format(point_A.name, point_B.name)
        self.point_A = point_A
        self.point_B = point_B
        self.length = length

    def __repr__(self):
        return self.name

        # def __eq__(self, other):
        #     return self.point_A == other.point_A and self.point_B == other.point_B

class Angle(pyDatalog.Mixin):
    def __init__(self, point_A: Point, point_B: Point, point_C: Point):
        super(Angle, self).__init__()

        self.name = '∠{}{}{}'.format(point_A.name, point_B.name, point_C.name)
        self.point_A = point_A
        self.point_B = point_B
        self.point_C = point_C

    def __repr__(self):
        return self.name

class PointOnSegment(pyDatalog.Mixin):
    def __init__(self, point: Point, segment: Segment):
        super(PointOnSegment, self).__init__()

        self.point = point
        self.segment = segment


class Triangle(pyDatalog.Mixin):
    def __init__(self, point_A: Point, point_B: Point, point_C: Point):
        super(Triangle, self).__init__()

        self.name = '△{}{}{}'.format(point_A.name, point_B.name, point_C.name)

        self.point_A = point_A
        self.point_B = point_B
        self.point_C = point_C

        self.segment_AB = Segment(point_A, point_B)
        self.segment_AC = Segment(point_A, point_C)
        self.segment_BC = Segment(point_B, point_C)

        self.angle_ABC = Angle(point_A, point_B, point_C)
        self.angle_ACB = Angle(point_A, point_C, point_B)
        self.angle_BAC = Angle(point_B, point_A, point_C)


class IsoscelesTriangle(Triangle):
    def __init__(self, point_A: Point, point_B: Point, point_C: Point, top_point: Point):
        super().__init__(point_A, point_B, point_C)
        self.top_point = top_point

    @pyDatalog.program
    def _():
        IsoscelesTriangle(X)