# 2. Model the following:
# a) a Point class that has two values, x and y, representing coordinates
# Add suport for the following
# - addition and substraction of two points
# - equality
# - string representation
# Make examples showcasing these capabilities
#
# b) a PointCollection class that has a list of points
# Add support for the following
# - check that a point is in the collection
# - len support
# - comparison between two point collections (based on length)
# - addition and substraction (for both Point and PointCollection)
# - string representation
# Make examples showcasing these capabilities
#
# c) a Triangle class that has 3 Point objects representing the corners of the triangle
# Add support for the following
# - validate that the points form a valid triangle (not a line)
# - equality
# - string representation
# - len support (based on triangle area)
# - comparison between other triangles (based on triangle area)
# - in support (a triangle is within another triangle, a point is in the triangle, a point collection is in a triangle)
#
# d) a Rectangle class that has 4 Point obejcts representing the corners of the rectangle
# Add support for the following
# - validate that the points form a valid rectangle
# - equality
# - string representation
# - len support (based on rectangle area)
# - comparison between other rectangles (based on rectangle area)
# - in support  (a rectangle is within another rectangle, a point is in the rectangle, a point collection is in a rectangle)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def _add_(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"


class PointCollection:
    def __init__(self, points):
        self.points = points

    def __contains__(self, point):
        return point in self.points

    def __len__(self):
        return len(self.points)

    def __eq__(self, other):
        return self.points == other.points

    def __gt__(self, other):
        return len(self) > len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __add__(self, other):
        if isinstance(other, Point):
            return PointCollection(self.points + [other])
        elif isinstance(other, PointCollection):
            return PointCollection(self.points + other.points)

    def __sub__(self, other):
        if isinstance(other, Point):
            return PointCollection([p for p in self.points if p != other])
        elif isinstance(other, PointCollection):
            return PointCollection([p for p in self.points if p not in other.points])

    def __str__(self):
        return f"PointCollection({[str(p) for p in self.points]})"


class Triangle:
        def __init__(self, p1, p2, p3):
            self.points = [p1, p2, p3]
            if self._area() == 0:
                raise ValueError("Points do not form a valid triangle (are colinear)")

        def _area(self):
            a, b, c = self.points
            return abs((a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y)) / 2)

        def __len__(self):
            return int(self._area())

        def __eq__(self, other):
            return set(self.points) == set(other.points)

        def __gt__(self, other):
            return self._area() > other._area()

        def __lt__(self, other):
            return self._area() < other._area()

        def __contains__(self, item):
            if isinstance(item, Point):
                a, b, c = self.points
                total_area = self._area()
                area1 = Triangle(item, b, c)._area()
                area2 = Triangle(a, item, c)._area()
                area3 = Triangle(a, b, item)._area()
                return total_area == area1 + area2 + area3
            elif isinstance(item, PointCollection):
                return all(p in self for p in item.points)
            elif isinstance(item, Triangle):
                return all(p in self for p in item.points)
            return False

        def __str__(self):
            return f"Triangle({', '.join(str(p) for p in self.points)})"