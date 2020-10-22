from pyDatalog import pyDatalog

from pyDatalog import pyEngine

pyEngine.Logging = True
pyEngine.Auto_print = True


# pyEngine.Slow_motion = True


class Express(pyDatalog.Mixin):
    def __init__(self, expression):
        super(Express, self).__init__()
        self.expression = expression

    def __repr__(self):
        return self.expression


class Equality(pyDatalog.Mixin):
    def __init__(self, express_A: Express, express_B: Express):
        super(Equality, self).__init__()
        self.expression = '{}={}'.format(express_A.expression, express_B.expression)
        self.express_A = express_A
        self.express_B = express_B

    def __repr__(self):
        return self.expression


class Point(pyDatalog.Mixin):
    def __init__(self, name):
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

    def get_name(self):
        return self.name

    def get_point_A(self):
        print("get_point_A: " + self.point_A.name)
        return self.point_A

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
        self.name_tmp = None

    def get_sum_of_inner_angle(self):
        return Equality(
            express_A=Express('{}+{}+{}'.format(self.angle_ABC.name, self.angle_ACB.name, self.angle_BAC.name)),
            express_B=Express('π'))


class RightTriangle(Triangle):
    def __init__(self, point_A: Point, point_B: Point, point_C: Point, top_point: Point):
        super(RightTriangle, self).__init__(point_A, point_B, point_C)
        self.top_point = top_point

    def get_hypotenuses(self):
        if self.top_point == self.point_A:
            return [self.segment_AB, self.segment_AC]
        elif self.top_point == self.point_B:
            return [self.segment_AB, self.segment_BC]
        else:
            return [self.segment_AC, self.segment_BC]

    def get_bottom_angles(self):
        if self.top_point == self.point_A:
            return [self.angle_ABC, self.angle_ACB]
        elif self.top_point == self.point_B:
            return [self.angle_BAC, self.angle_ACB]
        else:
            return [self.angle_BAC, self.angle_ABC]


class IsoscelesTriangle(Triangle):
    def __init__(self, point_A: Point, point_B: Point, point_C: Point, top_point: Point):
        super(IsoscelesTriangle, self).__init__(point_A, point_B, point_C)
        self.top_point = top_point

    def get_hypotenuses(self):
        if self.top_point == self.point_A:
            return [self.segment_AB, self.segment_AC]
        elif self.top_point == self.point_B:
            return [self.segment_AB, self.segment_BC]
        else:
            return [self.segment_AC, self.segment_BC]

    def get_bottom_angles(self):
        if self.top_point == self.point_A:
            return [self.angle_ABC, self.angle_ACB]
        elif self.top_point == self.point_B:
            return [self.angle_BAC, self.angle_ACB]
        else:
            return [self.angle_BAC, self.angle_ABC]


class Plane(pyDatalog.Mixin):
    def __init__(self, name):
        super(Plane, self).__init__()
        self.name = name

    def __repr__(self):
        return self.name

#
# point_A = Point('A')
# point_B = Point('B')
# point_C = Point('C')
#
# segment_AB = Segment(point_A, point_B)
#
# triangle = Triangle(point_A, point_B, point_C)
# triangle_ABC = IsoscelesTriangle(point_A, point_B, point_C, point_A)
# # pyDatalog.assert_fact('Triangle', triangle)
# X = pyDatalog.Variable()
# Z = pyDatalog.Variable()
#
# print("ask")
# Triangle.triangle_name(triangle, X)
# print(X)
#
# # Triangle.triangle_name(segment_AB, X)
# # IsoscelesTriangle.hypotenuse(triangle_ABC, X)
# # print(X)
#
# # Segment.point_A[X] == point_A
# # print(X)
#
# Y = pyDatalog.Variable()
# Segment.end_point(segment_AB, Y)
# # Segment.end_point(triangle.segment_AB, X)
#
# print(Y)
