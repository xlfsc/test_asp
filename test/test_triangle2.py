from pyDatalog import pyDatalog


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
        Segment.length_equ(X, Z) <= (Segment.length[X] == Y) & (Segment.length[Z] == Y) & (Y != None)


class EqualRule(pyDatalog.Mixin):
    def __int__(self):
        pass

    @pyDatalog.program()
    def _():
        EqualRule.obj_eq(X,Y) <= Segment(X) & Segment(Y) & (Segment.point_A[X] == Segment.point_A[Y]) &  (Segment.point_B[X] == Segment.point_B[Y])

class Equaltion():
    def __init__(self, equation_content):
        self.equaltion_content=equation_content

    def _():
        Equation(Y) <= Equation(X) & Y==symbol_simpify(Equation.equation_content[X])

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
        IsoscelesTriangle(X) <= (Segment.obj_eq(Triangle.segment_AB[X], Y) &
            Segment.obj_eq(Triangle.segment_AC[X], Y) & Segment.length_equ(Y, Z) &
            not(EqualRule.obj_eq(Z, Y)))
        Triangle.IsoscelesTriangle(X) <= (EqualRule.obj_eq(Triangle.segment_AB[X], Y) &
            EqualRule.obj_eq(Triangle.segment_BC[X], Y) & Segment.length_equ(Y, Z) &
            not(EqualRule.obj_eq(Z, Y)))
        Triangle.IsoscelesTriangle(X) <= (EqualRule.obj_eq(Triangle.segment_AC[X], Y) &
            EqualRule.obj_eq(Triangle.segment_BC[X], Y) & Segment.length_equ(Y, Z) &
            not(EqualRule.obj_eq(Z, Y)))


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
