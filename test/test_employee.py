from pyDatalog import pyDatalog

class Employee(pyDatalog.Mixin):

    def __init__(self, name, manager, salary):
        super(Employee, self).__init__()
        self.name = name
        self.manager = manager
        self.salary = salary

    def __repr__(self):
        return self.name

    @pyDatalog.program()
    def _():
        Employee.salary_class[X] = Employee.salary[X] // 1000
        Employee.indirect_manager(X, Y) <= (Employee.manager[X] == Y) & (Y != None)
        Employee.indirect_manager(X, Y) <= (Employee.manager[X] == Z) & Employee.indirect_manager(Z, Y)


John = Employee('John', None, 6800)
Mary = Employee('Mary', John, 6300)

print(Mary.salary_class)

X = pyDatalog.Variable()
# pyDatalog.create_terms('X')

Employee.salary[X] == 6300
print(X)

Employee.salary_class[X] == 6
print(X)

Employee.indirect_manager(Mary, X)
print(X)