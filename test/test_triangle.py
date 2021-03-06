from pyDatalog import pyDatalog


class Point(pyDatalog.Mixin):
    def __int__(self, name):
        super(Point, self).__init__()
        self.name = name

    def __repr__(self):
        return self.name


class Segment(pyDatalog.Mixin):
    def __init__(self, point_A, point_B, length=None):
        super(Segment, self).__init__()

        self.name = '{}{}'.format(point_A, point_B)
        self.point_A = point_A
        self.point_B = point_B
        self.length = length

    def __repr__(self):
        return self.name

    # def __eq__(self, other):
    #     return self.point_A == other.point_A and self.point_B == other.point_B

    @pyDatalog.program()
    def _():
        Segment.length_equ(X, Z) <= (Segment.length[X] == Y) & (Segment.length[Z] == Y) & (Y != None) & (X != Z)
        Segment.obj_eq(X, Y) <= Segment(X) & Segment(Y) & (
        ((Segment.point_A[X] == Segment.point_A[Y]) & (Segment.point_B[X] == Segment.point_B[Y]))
        or (Segment.point_A[X] == Segment.point_B[Y] & Segment.point_B[X] == Segment.point_A[Y]))


class ObjectEqual(pyDatalog.Mixin):
    def __int__(self):
        super(ObjectEqual, self).__init__()

    @pyDatalog.program()
    def _():
        ObjectEqual.obj_eq(X, Y) <= Segment(X) & Segment(Y) & (Segment.point_A[X] == Segment.point_A[Y]) & (
        Segment.point_B[X] == Segment.point_B[Y])


class Triangle(pyDatalog.Mixin):
    def __init__(self, point_A, point_B, point_C):
        super(Triangle, self).__init__()
        self.name = '△{}{}{}'.format(point_A, point_B, point_C)
        self.segment_AB = Segment(point_A, point_B)
        self.segment_AC = Segment(point_A, point_C)
        self.segment_BC = Segment(point_B, point_C)

    def __repr__(self):
        return self.name

    @pyDatalog.program()
    def _():
        Triangle.IsoscelesTriangle(X) <= (Triangle.segment_AB[X] == Y) & (
            Triangle.segment_BC[X] == Z) & (Segment.length_equ(Y, Z) or Segment.length_equ(Z, Y)) & (Y != Z)

        Triangle.IsoscelesTriangle(X) <= (Triangle.segment_AB[X] == Y) & (
            Triangle.segment_AC[X] == Z) & (Segment.length_equ(Y, Z) or Segment.length_equ(Z, Y)) & (Y != Z)

        Triangle.IsoscelesTriangle(X) <= (Triangle.segment_BC[X] == Y) & (
            Triangle.segment_AC[X] == Z) & (Segment.length_equ(Y, Z) or Segment.length_equ(Z, Y)) & (Y != Z)


triangle_ABC = Triangle('A', 'B', 'C')
segment_AB = Segment('A', 'B', 1)
segment_AC = Segment('A', 'C', 1)

X = pyDatalog.Variable()

Segment.length[X] == 1
print(X)

Triangle.IsoscelesTriangle[X]
print(X)

OtherRule.length_equ(segment_AC, X)
print(X)

Triangle.segment_AB[triangle_ABC] == X
print(X)
