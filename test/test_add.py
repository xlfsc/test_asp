from pyDatalog import pyDatalog


class Rational(pyDatalog.Mixin):
    def __init__(self, num):
        super(Rational, self).__init__()
        self.num = num
    def __repr__(self):
        return self.num

    @pyDatalog.program()
    def _():
        Employee.salary_class[X] = Employee.salary[X] // 1000
        Employee.indirect_manager(X, Y) <= (Employee.manager[X] == Y) & (Y != None)
        Employee.indirect_manager(X, Y) <= (Employee.manager[X] == Z) & Employee.indirect_manager(Z, Y)
