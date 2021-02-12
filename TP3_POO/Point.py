from math import pow, sqrt

class Point:
    def __init__(self, __abs = 0, __ord = 0):
        self.__abs = float(__abs)
        self.__ord = float(__ord)
    
    @property
    def __abs(self):
        return self.___abs

    @property
    def __ord(self):
        return self.___ord

    @__abs.setter
    def __abs(self, value):
        self.___abs = value

    @__ord.setter
    def __ord(self, value):
        self.___ord = value
    def __str__(self):
        print("__abs: ", self.__abs)
        print("__ord: ", self.__ord)

    def calculer_distance(self, p):
        return sqrt(pow(self.__abs - p.__abs, 2) + pow(self.__ord - p.__ord, 2))

    def calculer_milieu(self, p):
        temp_abs = (self.__abs + p.__abs) / 2
        temp_ord = (self.__ord + p.__ord) / 2
        return self.__class__(temp_abs, temp_ord)
