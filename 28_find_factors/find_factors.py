def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    factors = []
    half = int(num/2)
    for i in range(1,half+1):
        if num % i == 0:
            factors.append(i)
            factors.append(int(num/i))
    factors.sort()
    no_dupes = list(set(factors))
    no_dupes.sort()
    return no_dupes
