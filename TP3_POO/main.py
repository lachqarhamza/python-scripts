from Point import Point
from TroisPoints import TroisPoints

# test Point class ---------------------------
# test constructor
testPoint = Point(1, 2)

# test __str__ function
testPoint.__str__()

# test distance calculation
point2 = Point(4, 3)
d1 = testPoint.calculer_distance(point2)
d2 = point2.calculer_distance(testPoint)
print("distance is: ", d1)
print("distance is: ", d2)

# test middle calculation
m = testPoint.calculer_milieu(point2)
m.__str__()

# test TroisPoints class ----------------------
# test the constructor
a = Point(0, 0)
b = Point(1, 1)
c = Point(2, 3)

tp = TroisPoints(a, b, c)

# test sont alignes
print(tp.sont_alignes())

# test est_isocele function
print(tp.est_isocele())
