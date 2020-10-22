from pyDatalog import pyDatalog

pyDatalog.load("""
    perp(X, Z) <= perp(X, Y) & line(Z) & lineInPlane(Z, Y)
    perp(X, Z) <= perp(X, Y) & perp(X, Z) & lineInPlane(Y, P) & lineInPlane(Z, P) & (Z != Y)
    sec(X) <= first(X)
    + first('b')
    + ~first('a')
    + ~sec(a)
    
    + perp('SA', 'ABC')
    + line('BC')
    + lineInPlane('BC', 'ABC')
    + perp('BC', 'AC')
    + lineInPlane('BC', 'SAC')
    + lineInPlane('AC', 'SAC')
"""
               )
X = pyDatalog.Variable()

print(pyDatalog.ask('first(X)'))
