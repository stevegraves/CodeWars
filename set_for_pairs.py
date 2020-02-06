def sum_pairs(ints, s):
    cache = set()
    for i in ints:
        if s - i in cache:
            return [s-i, i]
        cache.add(i)
    return None





sum_pairs([1, 4, 8, 7, 3, 15], 8)
sum_pairs([4, 3, 2, 3, 4],         6)
