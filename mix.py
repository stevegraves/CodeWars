from operator import itemgetter
from collections import Counter


# My initial solution
def mix(s1, s2):
    dict1 = {}
    dict2 = {}
    combo = []
    output = ''
    for i in s1:
        if i.islower():
            dict1.setdefault(i, 0)
            dict1[i] += 1
    for i in s2:
        if i.islower():
            dict2.setdefault(i, 0)
            dict2[i] += 1
    dict1 = {k: v for k, v in sorted(dict1.items(), key=lambda item: item[1]) if v > 1}
    dict2 = {k: v for k, v in sorted(dict2.items(), key=lambda item: item[1]) if v > 1}

    for k, v in dict2.items():
        if k in dict1:
            if dict1[k] > v:
                combo.append([dict1[k], k, 1])
            elif dict1[k] < v:
                combo.append([v, k, 2])
            else:
                combo.append([v, k, 3])
        else:
            combo.append([v, k, 2])

    for k, v in dict1.items():
        if k in dict2:
            pass
        else:
            combo.append([v, k, 1])

    combo1 = sorted(combo, key=itemgetter(1))
    combo2 = sorted(combo1, key=itemgetter(2))
    combo3 = sorted(combo2, key=itemgetter(0), reverse=True)

    for i, j in enumerate(combo3):
        if j[2] == 3:
            j[2] = '='
        if i == len(combo3) - 1:
            output += '{}:{}'.format(j[2], j[1] * j[0])
        else:
            output += '{}:{}/'.format(j[2], j[1] * j[0])

    return output


# 'Best Practice'
def mix2(s1, s2):
    c1 = Counter(filter(str.islower, s1))
    c2 = Counter(filter(str.islower, s2))
    res = []
    for c in set(c1 + c2):
        n1, n2 = c1.get(c, 0), c2.get(c, 0)
        if n1 > 1 or n2 > 1:
            res.append(('1', c, n1) if n1 > n2 else
                       ('2', c, n2) if n2 > n1 else ('=', c, n1))
    res = ['{}:{}'.format(i, c * n) for i, c, n in res]
    print(res)
    print('/'.join(sorted(res, key=lambda s: (-len(s), s))))

# mix("Are they here", "yes, they are here")
# mix("looping is fun but dangerous", "less dangerous than coding")
# mix(" In many languages", " there's a pair of functions")
