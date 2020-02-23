from operator import itemgetter


# initial solution

def closest1(strng):
    if len(strng) == 0:
        return []
    nums = [int(x) for x in (strng.split())]
    indx = [x for x in range(len(nums))]
    weights = []
    for x in strng.split():
        s = 0
        for i in x:
            s += int(i)
        weights.append(s)

    total = []
    for w, i, n in zip(weights, indx, nums):
        total.append([w, i, n])

    result = sorted(total, key=itemgetter(0))

    diff = abs(result[0][0] - result[1][0])
    final_indx = [0, 1]
    for i, x in enumerate(result):
        try:
            a = abs(x[0] - result[i + 1][0])
            if a < diff:
                diff = a
                final_indx = [i, i + 1]
        except:
            break

    return [result[final_indx[0]], result[final_indx[1]]]


# Best Practice
def closest(s):
    wght = sorted([[sum(int(c) for c in n), i, int(n)] for i, n in enumerate(s.split())], key=lambda k: (k[0], k[1]))
    print(wght)
    diff = [abs(a[0] - b[0]) for a, b in zip(wght, wght[1:])]
    print(diff)
    return [wght[diff.index(min(diff))], wght[diff.index(min(diff)) + 1]] if wght else []


closest("456899 50 11992 176 272293 163 389128 96 290193 85 52")
closest("239382 162 254765 182 485944 134 468751 62 49780 108 54")
