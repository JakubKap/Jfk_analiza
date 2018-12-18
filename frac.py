
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    return (a*b)//gcd(a,b)


class Fraction:

    def __init__(self, nom: int, den: int):
        
        assert (den != 0), "0 w mianowniku"

        self.nom = nom
        self.den = den
        self = self.norm()

    def __str__(self):
        return "{}/{}".format(self.nom, self.den)

    def __reversed__(self):
        return Fraction(self.den, self.nom)

    def __add__(self, other):
        common = lcm(self.den, other.den)
        return Fraction( self.nom * common / self.den + other.nom * common / other.den, common )

    def __sub__(self, other):
        return self + other.negative()

    def __mul__(self, other):
        return Fraction(self.nom * other.nom, self.den * other.den)

    def __div__(self, other):
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

def fmin(*args):
    result = args[0]
    _result = result.nom / result.den

    for a in args[1:]:
        if (a.nom / a.den) < _result:
            result = a
            _result = result.nom / result.den

    return result

print(fmin(f(2, 3), f(3, 4), f(1,5), f(8, 9)))
