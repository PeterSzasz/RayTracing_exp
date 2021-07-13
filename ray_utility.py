from math import sqrt

class Vec3:
    def __init__(self, x = 0.0, y = 0.0, z = 0.0) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"

    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    def __add__(self, r):
        return Vec3(self.x + r.x, self.y + r.y, self.z + r.z)

    def __sub__(self, r):
        return self + -r

    def __mul__(self, r):
        if isinstance(r, int) or isinstance(r, float):
            return Vec3(self.x*r, self.y*r, self.z*r)
        if isinstance(r, Vec3):
            return Vec3(self.x*r.x, self.y*r.y, self.z*r.z)

    def __truediv__(self, r):
        if r == 0 or r == None:
            raise ZeroDivisionError
        return self * (1/r)

    def __eq__(self, r):
        if self.x == r.x and self.y == r.y and self.z == r.z:
            return True
        else:
            return False

    def dot(self, r):
        return self.x*r.x + self.y*r.y + self.z*r.z

    def cross(self, r):
        return Vec3(self.y*r.z - self.z*r.y,
                    self.z*r.x - self.x*r.z,
                    self.x*r.y - self.y*r.x)

    def length_squared(self):
        return self.x*self.x + self.y*self.y + self.z*self.z

    def length(self):
        return sqrt(self.length_squared())

    def as_unit_vector(self):
        if self.length() == 0:
            return Vec3()
        else:
            return self / self.length()


class Ray:
    def __init__(self, origin: Vec3, direction: Vec3) -> None:
        self.orig = origin
        self.dir = direction.as_unit_vector()

    def at(self, t: float):
        return self.orig + self.dir*t


if __name__ == "__main__":
    v1 = Vec3(2,3,4)
    v2 = Vec3(5,6,7)
    print(v1)                   # (2,3,4)
    print(v2)                   # (5,6,7)
    print(v1*v2)                # (10,18,28)
    print(v1/2)                 # (1.0,1.5,2.0)
    print(v1.length())          # 5.385164807134504
    print(v1.as_unit_vector())  # (0.3713906763541037,0.5570860145311556,0.7427813527082074)
    print(v1.dot(v2))           # 56
    print(v1.cross(v2))         # (-3,6,-3)
    print(v1==v1)               # True
    print(v1==v2)               # False
    # TODO: goto unittests