def gcdIter(a, b):
    test = min(a, b)

    while a % test != 0 or b % test != 0:
        test -= 1

    return test
