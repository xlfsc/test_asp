from pyDatalog import pyDatalog

from pyDatalog import pyEngine

pyEngine.Logging = True
pyEngine.Auto_print = True


# pyEngine.Slow_motion = True

class AbstractData(pyDatalog.Mixin):
    def __init__(self):
        super(AbstractData, self).__init__()

    @pyDatalog.program()
    def _():
        (AbstractData.IsoscelesTriangle(S, X, K)) <= (S == S) & (Y == (lambda X: X.get_segment_AB())) & (Z == (lambda X: X.segment_AC)) & (
            Segment.obj_equ[Y] == M) & (G == (lambda X: X.get_segment_AB())) & (Segment.obj_equ[Z] == N) & (Segment.length_equ(M, N)) & (K == (
            lambda X: IsoscelesTriangle(X.point_A, X.point_B, X.point_C, X.point_A))) & (H == (lambda X: X.get_segment_AB()))

        # (Triangle.test_prolog[X] == Y) <= (Y == (lambda X: X.test()))
        # (Triangle.test_prolog[X] == Y) <=  (Triangle.test_prolog[X] == Y) & (Y == 'test')
        (Triangle.test_prolog[X] == Y) <= (Y == 'test')


class Express(AbstractData):
    def __init__(self, expression):
        super(Express, self).__init__()
        self.expression = expression

    def __repr__(self):
        return self.expression


class Equality(AbstractData):
    def __init__(self, express_A: Express, express_B: Express):
        super(Equality, self).__init__()
        self.expression = '{}={}'.format(express_A.expression, express_B.expression)
        self.express_A = express_A
        self.express_B = express_B

    def __repr__(self):
        return self.expression


class Point(AbstractData):
    def __init__(self, name):
        super(Point, self).__init__()
        self.name = name

    def __repr__(self):
        return self.name


class Segment(AbstractData):
    def __init__(self, point_A: Point, point_B: Point, length=None):
        super(Segment, self).__init__()

        self.name = '{}{}'.format(point_A.name, point_B.name)
        self.point_A = point_A
        self.point_B = point_B
        self.length = length

    def get_name(self):
        return self.name + ('' if self.length is None else "_" + str(self.length))

    def get_point_A(self):
        print("get_point_A: " + self.point_A.name)
        return self.point_A

    def test(self):
        print("test rule start!")
        return 'test'

    def __repr__(self):
        return self.name

        # def __eq__(self, other):
        #     return self.point_A == other.point_A and self.point_B == other.point_B

    @pyDatalog.program()
    def _():
        Segment.length_equ(X, Z) <= (Segment.length[X] == Y) & (Segment.length[Z] == Y) & (Y != None) & (K == (lambda X: X.test()))
        (Segment.obj_equ[X] == Y) <= (Z == (lambda X: X.get_point_A())) & (
            (Segment.point_A[X] == Segment.point_A[Y]) & (Segment.point_B[X] == Segment.point_B[Y])) or (
            (Segment.point_A[X] == Segment.point_B[Y]) & (Segment.point_B[X] == Segment.point_A[Y]))


class Angle(AbstractData):
    def __init__(self, point_A: Point, point_B: Point, point_C: Point):
        super(Angle, self).__init__()

        self.name = '∠{}{}{}'.format(point_A.name, point_B.name, point_C.name)
        self.point_A = point_A
        self.point_B = point_B
        self.point_C = point_C

    def __repr__(self):
        return self.name


class PointOnSegment(AbstractData):
    def __init__(self, point: Point, segment: Segment):
        super(PointOnSegment, self).__init__()

        self.point = point
        self.segment = segment


class Triangle(AbstractData):
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

    def get_segment_AB(self):
        print("get_segment_AB")
        return self.segment_AB

    def test(self):
        print("test: " + self.name)
        return True

    def __repr__(self):
        return self.name

    def get_sum_of_inner_angle(self):
        print("get_sum_of_inner_angle")
        return Equality(
            express_A=Express('{}+{}+{}'.format(self.angle_ABC.name, self.angle_ACB.name, self.angle_BAC.name)),
            express_B=Express('π'))

    def f(self):
        return IsoscelesTriangle(self.point_A, self.point_B, self.point_C, self.point_A)

    @pyDatalog.program()
    def _():
        # Q: Segment(A, B)与Segment(A, B, 1)等价判定
        # (Triangle.IsoscelesTriangle(X, K)) <= (Y == (lambda X: X.segment_AB)) & (Z == (lambda X: X.segment_AC)) & (
        #     Segment.obj_equ[Y] == M) & (Segment.obj_equ[Z] == N) & (Segment.length_equ(M, N)) & (K == (
        #     lambda X: IsoscelesTriangle(X.point_A, X.point_B, X.point_C, X.point_A)))
        Triangle.sum_of_inner_angle(X, Y) <= (Y == X.get_sum_of_inner_angle())
        # worked!
        pass
        # Triangle.IsoscelesTriangle(X, K) <= (
        #     K == (lambda X: IsoscelesTriangle(X.point_A, X.point_B, X.point_C, X.point_A)))


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
        print("get_hypotenuses!")
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

    def __repr__(self):
        return '等腰' + self.name

    @pyDatalog.program()
    def _():
        # (Triangle.IsoscelesTriangle(X, K)) <= \
        # (Y == X.segment_AB) & (Z == X.segment_AC) & (
        #     K == (IsoscelesTriangle(X.point_A, X.point_B, X.point_C, X.point_A)))
        print("IsoscelesTriangle Rule!")
        # (Triangle.IsoscelesTriangle2(X, K)) <= (Y == (lambda X: X.segment_AB)) & (Z == (lambda X: X.segment_AC)) & ( \
        #     # Segment.length_equ(X, Y)) &\
        #     (K == (lambda X: IsoscelesTriangle(X.point_A, X.point_B, X.point_C, X.point_A))))
        # (Triangle.IsoscelesTriangle(X, K)) <= (K == X.f())
        # Triangle.IsoscelesTriangle(X, K) <= (K == (lambda X : IsoscelesTriangle(X.point_A, X.point_B, X.point_C, X.point_A)))

        # Triangle.sum_of_inner_angle(X, Y) <= (Y == X.get_sum_of_inner_angle())


class Plane(AbstractData):
    def __init__(self, name):
        super(Plane, self).__init__()
        self.name = name

    def __repr__(self):
        return self.name

if __name__ == '__main__':


    #
    point_A = Point('A')
    point_B = Point('B')
    point_C = Point('C')
    #
    # segment_AB = Segment(point_A, point_B)
    #
    # triangle = Triangle(point_A, point_B, point_C)
    # triangle_ABC = IsoscelesTriangle(point_A, point_B, point_C, point_A)
    # # pyDatalog.assert_fact('Triangle', triangle)
    X = pyDatalog.Variable()
    K = pyDatalog.Variable()
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
    segment_AB = Segment(point_A, point_B, 1)
    segment_AC = Segment(point_A, point_C, 1)
    #
    triangle_ABC = Triangle(point_A, point_B, point_C)
    #
    # Segment.length_equ(segment_AB, X)
    # print("length_equ with " + segment_AB.get_name() + ": " + str(X))
    #
    # Triangle.IsoscelesTriangle2(triangle_ABC, X)
    # print(X)

    # Segment.obj_equ[segment_AB] == X
    # print("obj_equ with " + segment_AB.get_name() + ": " + str(X))

    AbstractData.IsoscelesTriangle(segment_AB, triangle_ABC, K)
    Triangle.test_prolog[triangle_ABC] == K
    print(K)
