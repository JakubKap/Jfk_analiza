
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


class Fraction:

    def __init__(self, nom: int, den: int):
        assert (den != 0), "0 w mianowniku"

        self.nom = nom
        self.den = den
        self = self.norm()

    def __str__(self):
        if self.den == 1:
            return "{}".format(self.nom)
        else:
            return "{}/{}".format(self.nom, self.den)

    def __reversed__(self):
        return Fraction(self.den, self.nom)

    def __add__(self, other):
        common = lcm(self.den, other.den)
        return Fraction(self.nom * common / self.den + other.nom * common / other.den, common)

    def __sub__(self, other):
        return self + other.negative()

    def __mul__(self, other):
        return Fraction(self.nom * other.nom, self.den * other.den)

    def __mod__(self, other):
        result = self
        while result > other:
            result -= other
        return Fraction(self.nom)

    def __pow__(self, other):
        return Fraction(self.nom ** other, self.den ** other)

    def __floordiv__(self, other):
        return (self / other) - (self % other)

    def __gt__(self, other):
        common = lcm(self.den, other.den)
        return (self.nom * common / self.den) > (other.nom * common / other.den)

    def __truediv__(self, other):
        return self * reversed(other)

    def negative(self):
        return Fraction(-self.nom, self.den)

    def invert(self):
        return reversed(self)

    def norm(self):
        divisor = gcd(self.nom, self.den)

        if divisor == 1:
            return self

        return Fraction(self.nom / divisor, self.den / divisor)


# Quick fraction
def f(nom, den):
    return Fraction(nom, den)


def fmin(args):
    result = args[0]
    _result = result.nom / result.den

    for a in args[1:]:
        if (a.nom / a.den) < _result:
            result = a
            _result = result.nom / result.den

    return result

def fmax(args):
    result = args[0]
    _result = result.nom / result.den

    for a in args[1:]:
        if (a.nom / a.den) > _result:
            result = a
            _result = result.nom / result.den

    return result

def fsqrt(a):
    pass

def fabs(a):
    if a < f(0, 1):
        return a.negative()
    return a

def ffloor(a):
    return f(a.nom - (a.nom % a.den), a.den)

def fceil(a):
    return f(a.nom + a.den - (a.nom % a.den), a.den)

def fround(a):
    modu = (a.nom % a.den) / a.den
    if modu >= 0.5:
        return fceil(a)
    return floor(a)




print(fmin(f(2, 3), f(3, 4), f(1, 5), f(8, 9)))