from Point import Point

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

