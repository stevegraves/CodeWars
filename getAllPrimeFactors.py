def getallprimefactors(n):
    output = []
    if type(n) is not int or n <= 0:
        return output
    if n < 3:
        return [n]
    for i in range(2, n + 1):
        num = 0
        while n % i == 0:
            num += 1
            n //= i
        if num > 0:
            for j in range(num):
                output.append(i)
        if n == 1:
            return output

def getUniquePrimeFactorsWithCount(n):
    output = [[], []]
    if type(n) is not int or n <= 0:
        return output
    if n == 1:
        return [[n], [n]]
    if n == 2:
        return [[n], [n - 1]]
    for i in range(2, n + 1):
        num = 0
        while n % i == 0:
            num += 1
            n //= i
        if num > 0:
            output[0].append(i)
            output[1].append(num)
        if n == 1:
            return output

def getUniquePrimeFactorsWithProducts(n):
    output = []
    if type(n) is not int or n <= 0:
        return output
    if n < 3:
        return [n]
    result = getUniquePrimeFactorsWithCount(n)
    for i, j in zip(result[0], result[1]):
        output.append(i ** j)
    return output



getallprimefactors(100)
getUniquePrimeFactorsWithCount(100)
getUniquePrimeFactorsWithProducts(100)
