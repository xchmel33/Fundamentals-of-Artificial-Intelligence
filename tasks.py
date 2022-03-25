class Task(object):

    def __init__(self, StartState, GoalStates):
        self.startState = StartState
        self.operators = []
        self.goalStates = GoalStates
        self.expands = 0

    # idea:
    # from any state apply operators to get new states
    def expand(self, state):
        newStates = []
        for operator in self.operators:
            newState = operator(state)
            if newState:
                newStates.append(newState)
        self.expands += 1
        return newStates


class FillJugsTask(Task):

    def __init__(self, maxFirst, maxSecond, *args, **kwargs):
        super(FillJugsTask, self).__init__(*args, **kwargs,  maxFirst, maxSecond)

        def fillBigger(state):
            if state[0] != maxFirst:
                return [maxFirst, state[1]]
            else:
                return False

        def fillSmaller(state):
            if state[1] != maxSecond:
                return [state[0], maxSecond]
            else:
                return False

        def emptyBigger(state):
            if state[0] != 0:
                return [0, state[1]]
            else:
                return False

        def emptySmaller(state):
            if state[1] != 0:
                return [state[0], 0]
            else:
                return False

        def fromSmallerToBigger(state):
            if state[0] == 4 or state[1] == 0:
                return False
            x = 4 - state[0]
            if x > state[1]:
                x = state[1]
            return [state[0]+x, state[1]-x]

        def fromBiggerToSmaller(state):
            if state[1] == 3 or state[0] == 0:
                return False
            x = 3 - state[1]
            if x > state[0]:
                x = state[0]
            return [state[0]-x, state[1]+x]

        self.operators = [fillBigger, fillSmaller, emptyBigger, emptySmaller, fromSmallerToBigger, fromBiggerToSmaller]


class Loyd8Task(Task):

    def __init__(self, *args, **kwargs):
        super(Loyd8Task, self).__init__(*args, **kwargs)

        def operators(state):
            return False
        
        self.operators = [operators]
