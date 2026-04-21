from collections import namedtuple
Point = namedtuple('Point', 'x,y,z')
pt_a = Point(0,1,-4)
print(pt_a.y, pt_a.x, pt_a.z)