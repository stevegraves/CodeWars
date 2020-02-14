import math


# Boolean primality check with 6k +/- 1 pattern
def is_prime(n):
    if n <= 6:
        return n == 2 or n == 3 or n == 5
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = int(math.sqrt(n))
    t = 5
    while t <= limit:
        if n % t == 0 or n % (t + 2) == 0:
            return False
        t += 6
    return True


# find first prime pair of given gap within range
def gap(g, m, n):
    previous = None
    for i in range(m, n + 1):
        if is_prime(i):
            if previous:
                if i - previous == g:
                    return [previous, i]
                else:
                    previous = i
            else:
                previous = i
    return None
