def pyth_triple(m):
    a = 2 * m + 2
    b = m * (m + 2)
    c = m * m + 2 * m +2
    if a > b:
        return [b, a, c]
    else:
        return [a, b, c]