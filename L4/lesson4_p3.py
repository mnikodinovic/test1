__author__ = 'miroslav'

# print [(i, j) for i in range(3) for j in range(3) if (0 < i + j <= 2)]


def csuccessors(state):
    """Find successors (including those that result in dining) to this
    state. But a state where the cannibals can dine has no successors."""
    operacije = {(1, 0): 'M', (2, 0): 'MM', (1, 1): 'MC', (0, 1): 'C', (0, 2): 'CC'}
    m1, c1, b1, m2, c2, b2 = state
    if c1 > m1 or c2 > m2:
        return dict()
    else:
        if b1 == 1:
            smjer = '->'
            return dict(((m1 - i, c1 - j, 0, m2 + i, c2 + j, 1), operacije[i, j] + smjer)
                        for i in range(m1 + 1)
                        for j in range(c1 + 1) if (0 < i + j <= 2))
        else:
            smjer = '<-'
            return dict(((m1 + i, c1 + j, 1, m2 - i, c2 - j, 0), smjer + operacije[i, j])
                        for i in range(m2 + 1)
                        for j in range(c2 + 1) if (0 < i + j <= 2))


def test():
    assert csuccessors((2, 2, 1, 0, 0, 0)) == {(2, 1, 0, 0, 1, 1): 'C->',
                                               (1, 2, 0, 1, 0, 1): 'M->',
                                               (0, 2, 0, 2, 0, 1): 'MM->',
                                               (1, 1, 0, 1, 1, 1): 'MC->',
                                               (2, 0, 0, 0, 2, 1): 'CC->'}
    assert csuccessors((1, 1, 0, 4, 3, 1)) == {(1, 2, 1, 4, 2, 0): '<-C',
                                               (2, 1, 1, 3, 3, 0): '<-M',
                                               (3, 1, 1, 2, 3, 0): '<-MM',
                                               (1, 3, 1, 4, 1, 0): '<-CC',
                                               (2, 2, 1, 3, 2, 0): '<-MC'}
    assert csuccessors((1, 4, 1, 2, 2, 0)) == {}
    return 'tests pass'

print csuccessors((2, 2, 1, 0, 0, 0))
print csuccessors((1, 1, 0, 4, 3, 1))
print test()