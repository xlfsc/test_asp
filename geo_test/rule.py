from data_model import *
from pyDatalog import pyDatalog


class Relation(pyDatalog.Mixin):
    def __init__(self):
        super(Relation, self).__init__()

    @pyDatalog.program()
    def _():
        Relation.line_parallel_plane(X, Y) <= (Relation.line_parallel(X, Z)) & (Relation.line_in_plane(Z, Y))


class Rule(pyDatalog.Mixin):
    def __init__(self):
        pass

    @pyDatalog.program()
    def _():
        # 试验Rule嵌入lambda，worked!
        Triangle.triangle_name(X, Y) <= (Y == (lambda X: X.name))
        Segment.end_point(X, Y) <= (Segment.point_A[X] == Y)

        # TODO 验证生成的等式如何参与运算
        # TODO 验证生成的等式是否插入事实库

        Triangle.sum_of_inner_angle(X, Y) <= (Y == (lambda X: X.get_sum_of_inner_angle()))

        IsoscelesTriangle.waist_equ(X, Y) <= (
            Y == (lambda X: Equality(Express(X.get_hypotenuses()[0].name), Express(X.get_hypotenuses()[1].name))))

        IsoscelesTriangle.bottom_angle_equ(X, Y) <= (
            Y == (lambda X: Equality(Express(X.get_bottom_angles()[0].name), Express(X.get_bottom_angles()[1].name))))

        # TODO 尝试生成等式【报错】
        # Equality(Y) <= (IsoscelesTriangle(X)) & (
        #     Y == (lambda X: Equality(Express(X.get_hypotenuses()[0].name), Express(X.get_hypotenuses()[1].name))))

        # TODO 验证触发方式
        # TODO 验证能否搜集所有的等式，用于约化一个等式。比如：直角三角形根据勾股定理逆定理的判定
        # TODO 验证线面平行判定定理的实现
        # TODO 验证等腰三角形的判定，验证X是等腰三角形是否成立是可行的，但是解题中不一定知道是否需要验证等腰三角形
        # TODO 验证继承：等腰三角形也具有内角和


point_A = Point('A')
point_B = Point('B')
point_C = Point('C')

segment_AB = Segment(point_A, point_B)

X = pyDatalog.Variable()


def test_end_point():
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


test_super_rule()
