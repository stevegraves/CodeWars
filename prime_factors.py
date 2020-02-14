# Find prime factors in format '(2**2)(5**2)' (for 100)
def primeFactors(n):
    result = ''
    for i in range(2, n + 1):
        num = 0
        while (n % i == 0):
            num += 1
            n //= i
        if num > 0:
            result += '({}{})'.format(i, '**%d' % num if num > 1 else '')
        if n == 1:
            return result
