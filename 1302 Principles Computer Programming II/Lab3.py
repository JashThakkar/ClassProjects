# Basic OOP / Class building using math functions and properties for class building, with given test code (defined below)

class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __le__(self, other):
        self.other = other
        if self.x <= self.other:
            return True
        else:
            return False

    def __ge__(self, other):
        self.other = other
        if self.x >= self.other:
            return True
        else:
            return False

    def __eq__(self, other):
        self.other = other
        if self.x == self.other:
            return True
        else:
            return False

# Test code

loc1 = Location(int(input('x cord: ')), int(input('y cord: ')))
loc2 = Location(int(input('x cord: ')), int(input('y cord: ')))

print(loc1 == loc2)
print(loc1 <= loc2)
print(loc1 >= loc2)
