import math
from fractions import Fraction


# initial solution
def mixed_fraction(s):
    output = [int(n) for n in s.split('/')]
    n = output[0]
    d = output[1]
    g_d = math.gcd(n, d)
    if d == 0:
        raise ZeroDivisionError
    if n == 0:
        return str(0)
    if math.modf(n/d)[0] == 0:
        return str(n//d)
    if abs(d) > abs(n):
        return str(Fraction(n, d))
    n //= g_d
    d //= g_d
    if n/d < 0:
        n = abs(n)
        d = abs(d)
        return '-{} {}/{}'.format((n//d), n % d, d)
    return '{} {}/{}'.format(math.floor(n/d), abs(n % d), abs(d))

# Best practice
"""
def mixed_fraction(s):
    f = Fraction(*map(int, s.split('/')))
    if f.denominator == 1: return str(f.numerator)
    n = abs(f.numerator) / f.denominator * (1 if f.numerator > 0 else -1)
    f = abs(f - n) if n else f - n
    return "{} {}".format(n, f) if n else str(f)
"""





mixed_fraction('42/9')
mixed_fraction('6/3')
mixed_fraction('4/6')
mixed_fraction('0/18891')
mixed_fraction('-10/7')
