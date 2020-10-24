from data_model import *
from pyDatalog import pyDatalog


class Rule(pyDatalog.Mixin):
    def __init__(self):
        super(Rule, self).__init__()
        pass

    @pyDatalog.program()
    def _():
        # TODO 验证生成的等式如何参与运算
        # TODO 验证生成的等式是否插入事实库

        # Segment.length_equ(X, Y) <=



        IsoscelesTriangle.bottom_angle_equ(X, Y) <= (
            Y == (lambda X: Equality(Express(X.get_bottom_angles()[0].name), Express(X.get_bottom_angles()[1].name))))

        # TODO 尝试生成等式【报错】
        # Equality(Y) <= (IsoscelesTriangle(X)) & (
        #     Y == (lambda X: Equality(Express(X.get_hypotenuses()[0].name), Express(X.get_hypotenuses()[1].name))))

        # TODO 验证触发方式
        # TODO 验证能否搜集所有的等式，用于约化一个等式。比如：直角三角形根据勾股定理逆定理的判定
        # TODO 验证线面平行判定定理的实现
        # TODO 验证等腰三角形的判定，验证X是等腰三角形是否成立是可行的，但是解题中不一定知道是否需要验证等腰三角形
        # (IsoscelesTriangle[X]) <= (Triangle(X)) & (
        #     Segment.length_equ(Y, Z)) & (Y == (lambda X: X.segment_AB)) & (Z == (lambda X: X.segment_AC))
        # (IsoscelesTriangle[X]) <= (Segment.length_equ(Y, Z)) & (Y == X.get_hypotenuses[0]) & (Z == X.get_hypotenuses[1])
        # (Triangle.IsoscelesTriangle(X, K)) <= \
        # (Y == X.segment_AB) & (Z == X.segment_AC) &  ((X.f(X.point_A)) == K)
        # (Triangle.IsoscelesTriangle1(X, K)) <= (K == X.f())

        # worked!
        # (Triangle.IsoscelesTriangle2(X, K)) <= (Y == (lambda X: X.segment_AB)) & (Z == (lambda X: X.segment_AC)) & ( \
        #     # Segment.length_equ(X, Y)) &\
        #     (K == (lambda X: IsoscelesTriangle(X.point_A, X.point_B, X.point_C, X.point_A))))

        # pyDatalog.create_terms('M,N')
        # work failed! 执行此规则，并不会触发Segment.obj_equ


print('start!')
pyDatalog.create_terms('ObjEqual, lenth_equ, IsosceleTriangle, equality, X, Y, K, M, N, Z, T')

ObjEqual(X, Y) <= ((Segment.point_A[X] == Segment.point_A[Y]) & (Segment.point_B[X] == Segment.point_B[Y])) or (
    (Segment.point_A[X] == Segment.point_B[Y]) & (Segment.point_B[X] == Segment.point_A[Y]))

lenth_equ(X, Z) <= (Segment.length[X] == Y) & (Segment.length[Z] == Y) & (Y != None)

equality(X, Y) <= (Triangle.type[T] == True) & (X == T.get_sum_of_inner_angle()) & (Y == (lambda X: Express('180')))

IsosceleTriangle(X, K) <= (Y == (Triangle.segment_AB[X])) & (Z == (Triangle.segment_AC[X])) & (
    (Segment.type[M] == True) & (Segment.type[N] == True)) & (M != N) & (ObjEqual(Y, M)) & (ObjEqual(Z, N)) & (
                              lenth_equ(M, N)) & (K == (lambda X: X.point_A))

equality(X, Y) <= (IsosceleTriangle(T, K)) & ()

point_A = Point('A')
point_B = Point('B')
point_C = Point('C')


def test_judge_IsoscelesTriangle_2():
    segment_AB = Segment(point_A, point_B, 1)
    segment_AC = Segment(point_A, point_C, 1)

    triangle_ABC = Triangle(point_A, point_B, point_C)

    # Segment.length_equ(segment_AB, Y)
    # print("length_equ with " + segment_AB.get_name() + ": " + str(Y))

    # Segment.obj_equ[segment_AB] == X
    # print("obj_equ with " + segment_AB.get_name() + ": " + str(X))

    X = pyDatalog.Variable()
    Y = pyDatalog.Variable()

    IsosceleTriangle(triangle_ABC, X)
    print(X)

    equality(X, Express('180'))
    print(X)


test_judge_IsoscelesTriangle_2()
# TODO 验证继承：等腰三角形也具有内角和

X = pyDatalog.Variable()
Y = pyDatalog.Variable()


def test_triangle_name():
    triangle = Triangle(point_A, point_B, point_C)
    Triangle.triangle_name(triangle, X)
    print(X)


def test_end_point():
    segment_AB = Segment(point_A, point_B)
    Segment.end_point(segment_AB, X)
    print(X)


def test_sum_of_inner_angle():
    triangle = Triangle(point_A, point_B, point_C)
    Triangle.sum_of_inner_angle(triangle, X)
    print(X)


# 验证Fact的继承，Rule也可以匹配
def test_super_rule():
    triangle_ABC = IsoscelesTriangle(point_A, point_B, point_C, point_A)
    Triangle.sum_of_inner_angle(triangle_ABC, X)
    print(X)

    right_triangle = RightTriangle(point_A, point_B, point_C, point_A)
    Triangle.sum_of_inner_angle(right_triangle, X)
    print(X)


def test_property_of_IsoscelesTriangle():
    triangle_ABC = IsoscelesTriangle(point_A, point_B, point_C, point_A)
    IsoscelesTriangle.waist_equ(triangle_ABC, X)
    print(X)

    IsoscelesTriangle.bottom_angle_equ(triangle_ABC, X)
    print(X)


def test_verify_generate_equality():
    triangle_ABC = IsoscelesTriangle(point_A, point_B, point_C, point_A)
    pyDatalog.assert_fact('IsoscelesTriangle', triangle_ABC)
    Equality(X)
    print(X)


def test_judge_IsoscelesTriangle():
    segment_AB = Segment(point_A, point_B, 1)
    segment_AC = Segment(point_A, point_C, 1)

    triangle_ABC = Triangle(point_A, point_B, point_C)

    # Segment.length_equ(segment_AB, Y)
    # print("length_equ with " + segment_AB.get_name() + ": " + str(Y))

    # Segment.obj_equ[segment_AB] == X
    # print("obj_equ with " + segment_AB.get_name() + ": " + str(X))

    Triangle.IsoscelesTriangle(triangle_ABC, X)
    print(X)

# test_judge_IsoscelesTriangle()
