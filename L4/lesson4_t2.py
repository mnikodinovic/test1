__author__ = 'miroslav'

# -----------------
# User Instructions
#
# In this problem, you will solve the pouring problem for an arbitrary
# number of glasses. Write a function, more_pour_problem, that takes
# as input capacities, goal, and (optionally) start. This function should
# return a path of states and actions.
#
# Capacities is a tuple of numbers, where each number represents the
# volume of a glass.
#
# Goal is the desired volume and start is a tuple of the starting levels
# in each glass. Start defaults to None (all glasses empty).
#
# The returned path should look like [state, action, state, action, ... ]
# where state is a tuple of volumes and action is one of ('fill', i),
# ('empty', i), ('pour', i, j) where i and j are indices indicating the
# glass number.



def more_pour_problem(capacities, goal, start=None):
    """The first argument is a tuple of capacities (numbers) of glasses; the
    goal is a number which we must achieve in some glass.  start is a tuple
    of starting levels for each glass; if None, that means 0 for all.
    Start at start state and follow successors until we reach the goal.
    Keep track of frontier and previously explored; fail when no frontier.
    On success return a path: a [state, action, state2, ...] list, where an
    action is one of ('fill', i), ('empty', i), ('pour', i, j), where
    i and j are indices indicating the glass number."""
    global cilj
    cilj = goal
    global kapaciteti
    kapaciteti = capacities
    if not start:
        start = tuple([0 for i in capacities])
    return shortest_path_search(start, psuccessors, pis_goal)


def shortest_path_search(start, successors, is_goal):
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    if is_goal(start):
        return [start]
    explored = set()
    frontier = [[start]]
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (state, action) in successors(s).items():
            # print 'provjeravam stanje: ', state, ' i akciju: ', action
            if state not in explored:
                explored.add(state)
                print 'explored: ', len(explored)
                path2 = path + [action, state]
                # print 'path: ', path2
                if is_goal(state):
                    # print 'cilj nadjen, vracamo pobjednicki put'
                    return path2
                else:
                    frontier.append(path2)
                    # print 'frontier: ', frontier
    return Fail


def psuccessors(state):
    """State is a tuple of numbers signifying amount
    of liquid in each glass.
    state = (l1, l2..., ln)"""
    # print 'psuccessors pozvan sa: ', state
    num_states = range(len(state))
    successors = dict()
    # praznjenje casa
    for i in num_states:
        if state[i] > 0:
            state1 = tuple([state[j] if j != i else 0 for j in num_states])  # matrica sa ispraznjenom casom 'i'
            op1 = 'empty', i
            successors[state1] = op1

    # punjenje casa
    for i in range(len(state)):
        if state[i] < kapaciteti[i]:
            state1 = tuple(
                [state[j] if j != i else kapaciteti[i] for j in num_states])  # matrica sa napunjenom casom 'i'
            op1 = 'fill', i
            successors[state1] = op1

    # presipanje casa
    for i in num_states:
        for j in num_states:
            # print 's[', i, ']=', state[i], ';s[', j, ']=', state[j], 'c[', i, ']=', capacities[i], ';c[', j, ']=', capacities[j]
            if state[i] > 0 and state[j] < kapaciteti[j] and i != j:
                l1 = state[i]  # amount of liquid in first glass, the one being poured from
                l2 = state[j]  # amount of liquid in second glass, the one being poured to
                c1 = kapaciteti[i]
                c2 = kapaciteti[j]
                state1 = tuple([state[k] if k != j else min(c2, l2 + l1) for k in num_states])
                state2 = tuple([state1[k] if k != i else max(0, l2 + l1 - c2) for k in num_states])
                op1 = 'pour', i, j
                successors[state2] = op1
    # print '------', successors
    return successors


def pis_goal(state):
    if state:
        # print 'pis_goal: provjeravam je li cilj = ', cilj, ' unutar state = ', state, ' i rezultat je: ', cilj in state
        return cilj in state
    else:
        return False


Fail = []


def test_more_pour():
    assert more_pour_problem((1, 2, 4, 8), 4) == [
        (0, 0, 0, 0), ('fill', 2), (0, 0, 4, 0)]
    assert more_pour_problem((1, 2, 4), 3) == [
        (0, 0, 0), ('fill', 2), (0, 0, 4), ('pour', 2, 0), (1, 0, 3)]
    starbucks = (8, 12, 16, 20, 24)
    assert not any(more_pour_problem(starbucks, odd) for odd in (3, 5, 7, 9))
    assert all(more_pour_problem((1, 3, 9, 27), n) for n in range(28))
    assert more_pour_problem((1, 3, 9, 27), 28) == []
    return 'test_more_pour passes'


print test_more_pour()
# print more_pour_problem((8, 12, 16, 20, 24), 3)