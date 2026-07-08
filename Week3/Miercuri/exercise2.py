'''
2. Model the following:
a) a Point class that has two values, x and y, representing coordinates
Add suport for the following
- addition and substraction of two points
- equalitya
- string representation
Make examples showcasing these capabilities

b) a PointCollection class that has a list of points
Add support for the following
- check that a point is in the collection
- len support
- comparison between two point collections (based on length)
- addition and substraction (for both Point and PointCollection)
- string representation
Make examples showcasing these capabilities

c) a Triangle class that has 3 Point objects representing the corners of the triangle
Add support for the following
- validate that the points form a valid triangle (not a line)
- equality
- string representation
- len support (based on triangle area)
- comparison between other triangles (based on triangle area)
- in support (a triangle is within another triangle, a point is in the triangle, a point collection is in a triangle)

d) a Rectangle class that has 4 Point obejcts representing the corners of the rectangle
Add support for the following
- validate that the points form a valid rectangle
- equality
- string representation
- len support (based on rectangle area)
- comparison between other rectangles (based on rectangle area)
- in support  (a rectangle is within another rectangle, a point is in the rectangle, a point collection is in a rectangle)
'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        p = Point(0, 0)
        p.x = self.x + other.x
        p.y = self.y + other.y
        return p

    def __sub__(self):
        p = Point(0, 0)
        p.x -= other.x

    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"

class PointCollection:
    def __init__(self, points:list=None):
        self.points = list(points)

    def has(self, point):
        return point in self.points

    def __len__(self):
        return len(self.points)

    def __eq__(self, other):
        return len(self) == len(other)

    def __ne__(self, other):
        return len(self) != len(other)

    def __ls__(self, other):
        return len(self) < len(other)

    def __le(self, other):
        return len(self) <= len(other)

    def __gt__(self, other):
        return len(self) > len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def compare(self, other):
        if len(self) > len(other):
            return 1
        elif len(self) < len(other):
            return -1
        else:
            return 0

    def __add__(self, other):

        c = PointCollection(self.points)
        if isinstance(other, Point):
            c.points.append(other)
        elif isinstance(other, PointCollection):
            for p in other.points:
                c.points.append(p)
        else:
            print(f"Unknown type '{type(other)}' for PointCollection operation.")
            return None
            
        return c

    def __sub__(self, other):
        c = PointCollection(self.points)

        if (not self.has(other)):
            return c

        try:
            if isinstance(other, Point):
                c.points.remove(other)
            elif isinstance(other, PointCollection):
                for p in other.points:
                    c.points.remove(p)
            else:
                print(f"Unknown type '{type(other)}' for PointCollection operation.")
                return None
        except ValueError:
            pass

        return c

    def __str__(self):
        return " ".join([f"{c}" for c in self.points])


p1 = Point(1, 5)
p2 = Point(5, 3)
p3 = p1 + p2
print(p1, p2, p3)

coll = PointCollection([p1, p2, p3])
print("Coll:" + str(coll))
coll2 = coll + coll + p1
print("Coll2: " + str(coll2))
coll = coll - Point(1, 1)
if coll.compare(coll2) == -1:
    print("Coll is shorter than coll2")

