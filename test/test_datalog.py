from pyDatalog import pyDatalog

pyDatalog.create_terms('factorial, N, X')
factorial[N] = N * factorial[N-1]
factorial[1]=1
print(N==factorial[3])

print(X.in_(range(5)) & (X<2))

pyDatalog.create_terms('X,Y,Z,parallel,perpetual')

(perpetual(Y,Z)) <= ((parallel(X,Y)) & (perpetual(X,Z)))

+perpetual('l', 'α')
+parallel('α','β')

print(perpetual(Z,'β'))

pyDatalog.create_terms('X,Y,Z, salary, tax_rate, tax_rate_for_salary_above, net_salary')
salary['foo'] = 60
salary['bar'] = 110

print(salary[X]==Y)
print({X.data[i]:Y.data[i] for i in range(len(X.data))})

+(tax_rate[None]==0.33)
net_salary[X]=salary[X]*(1-tax_rate[None])
print(net_salary[X]==Z)

(tax_rate_for_salary_above[X] == 0.33) <= (0<=X)
(tax_rate_for_salary_above[X] == 0.50) <= (100<=X)

del net_salary[X]
net_salary[X] = salary[X] * (1 - tax_rate_for_salary_above[salary[X]])

print(net_salary[X] == Y)