def iterPower(base, exp):
    accumulator = 1
    while exp > 0:
        accumulator *= base
        exp -= 1
    return accumulator
