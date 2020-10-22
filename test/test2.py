from pyDatalog import pyDatalog

#
# pyDatalog.load("""
#     Segment.end_point(X, Y) <= (Segment(X)) & (1 == Y)
#     + (Segment('AB'))
#
# """)

pyDatalog.load("""
    Triangle.triangle_name(X, Y) <= (Triangle(X)) & ('ABC' == Y)
    + (Triangle('AB'))

""")
print(pyDatalog.ask('Triangle.triangle_name("AB",X)'))
