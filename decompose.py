def decompose(n):
    output = [n]
    total = 0
    while output:
        current = output.pop()
        total += current ** 2
        for i in range(current - 1, 0, -1):
            if total - (i ** 2) >= 0:
                total -= i ** 2
                output.append(i)
                if total == 0:
                    output.sort()
                    return output
    return None

decompose(10) # [3, 4]
#decompose(8) # None
#decompose(50) # [1, 3, 5, 8, 49]
