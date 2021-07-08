#named tiples

class Point3D:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z


from collections import namedtuple

Point2D=namedtuple('Point2D',['x','y'])
pt1=Point2D(3,9)
print(type(pt1))
print(pt1)


pt1=Point3D(1,2,3)
pt2=Point3D(1,2,3)

print(pt1 is pt2)
print(pt1 == pt2)
print(pt1.x==pt2.x)


class Point3D:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def __repr__(self): 
        return f'{self.__class__.__name__}x={self.x}, y={self.y},z={self.z}'

    def __eq__(self, other):
        if isinstance(other,Point3D):
            return self.x==other.x and self.y==other.y and self.z==other.z


pt1=Point3D(1,2,3)
pt2=Point3D(1,2,3)
'''__repr__ and __eq__ would have been 
    unnecessary if namedtuples were used'''

print(pt1 is pt2)
print(pt1 == pt2)

# print(max(pt1)) 'this would have worked if it was a named tuple'
pt1=namedtuple('pt1',('x','y'))
namedtup=pt1(3,2.99)
print(max(namedtup))

#