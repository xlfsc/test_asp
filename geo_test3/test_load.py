from pyDatalog import pyDatalog

pyDatalog.load("""
    ancestor(X, Y) <= parent(X, Y)
    ancestor(X, Y) <= parent(X, Z) & ancestor(Z, Y)
    + parent('bill', 'John Adams')
"""
)

pyDatalog.assert_fact('parent', 'bill', 'John Adams')
print(pyDatalog.ask('parent(bill, X)'))
print(pyDatalog.ask('ancestor(bill,X)'))