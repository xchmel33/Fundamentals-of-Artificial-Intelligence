from tasks import task


def printStep(Open, i, reverse=True, Closed=[]):
    if reverse:
        Open.reverse()
    print("\nSTEP:", i, "\nOPEN:", Open)
    if Closed:
        print("CLOSED:", Closed)
    if reverse:
        Open.reverse()


def BFS(task, OPEN=None, modification=False, CLOSED=None, debug=False):

    # krok 1
    if not OPEN:
        OPEN = [[task.startState]]  # zostrojit frontu OPEN a umiestnit do nej pociatocny uzol
        if debug:
            printStep(OPEN, task.expands, reverse=False, Closed=CLOSED)

    # krok 2
    if not OPEN:
        return False  # ak je fronta prazdna uloha nema riesenie

    # krok 3
    first = OPEN.pop(0)  # vybrat s fronty prvy uzol

    # krok 4
    if first[0] in task.goalStates:
        first.reverse()
        print("SOLVED! PATH: ", first)
        return first  # vybraty je uzol cielovy -> uloha vyriesena

    # krok 5
    newTasks = task.expand(first[0])  # expandovat uzol
    if CLOSED is not None:
        CLOSED.append(first[0])  # expandovany uzol umiestnit do CLOSED
    for newTask in newTasks:
        if CLOSED and newTask in CLOSED:  # preskocit naslednika ak je v CLOSED
            continue
        if modification and newTask in first:  # preskocit naslednika ak je v OPEN
            continue
        OPEN.append([newTask]+first)  # naslednikov umiestint do OPEN
    if debug:
        printStep(OPEN, task.expands, reverse=False, Closed=CLOSED)
    return BFS(task, OPEN=OPEN, modification=modification, CLOSED=CLOSED, debug=debug)  # pokracovat od kroku 2


def DFS(task, OPEN=None, modification=False, debug=False):

    # krok 1
    if OPEN is None:
        OPEN = [[task.startState]]  # zostrojit zasobnik OPEN, umiestnit do neho pociatocny uzol
        if debug:
            printStep(OPEN, task.expands)

    # krok 2
    if not OPEN:
        return False, False  # ak je zasobnik prazdny uloha nema riesenie

    # krok 3
    first = OPEN.pop()  # vybrat zo zasobniku vrchol

    # krok 4
    if first[0] in task.goalStates:
        if debug:
            printStep(OPEN, task.expands+1)
        return first, task.expands

    # krok 5
    newTasks = task.expand(first[0])  # expandovat uzol
    for newTask in newTasks:
        skip = False
        if modification:
            for o in OPEN:
                if newTask in o:
                    skip = True
            if newTask in first:
                skip = True
        if skip:
            continue
        OPEN.append([newTask]+first)
    if debug:
        printStep(OPEN, task.expands)
    return DFS(task, OPEN, modification=modification)


def DLS(task, OPEN=None, debug=False, modification=False, maxDepth=10, ids=False):

    # krok 1
    if OPEN is None:
        OPEN = [[task.startState]]  # zostrojit zasobnik OPEN, umiestnit do neho pociatocny uzol

    # krok 2
    if not OPEN:
        if ids:
            return True, False
        printStep(OPEN, task.expands+1)
        print("OPEN IS EMPTY -> SEARCH FAILED!")
        return False, False  # ak je zasobnik prazdny uloha nema riesenie

    # krok 3
    if debug:
        printStep(OPEN, task.expands)
    first = OPEN.pop()  # vybrat zo zasobniku vrchol
    curDepth = first.__len__()-1
    print("Current Depth:", curDepth)

    # krok 4
    if first[0] in task.goalStates:
        if debug:
            printStep(OPEN, task.expands+1)
            print("SOLVED! PATH: ", first)
            print("Current Depth:", curDepth)
        if ids:
            return False, True, []
        return first, task.expands

    # krok 5
    if curDepth < maxDepth:
        newTasks = task.expand(first[0])  # expandovat uzol
        for newTask in newTasks:
            skip = False
            if modification:
                for o in OPEN:
                    if newTask in o:
                        skip = True
                if newTask in first:
                    skip = True
            if skip:
                continue
            OPEN.append([newTask]+first)
    else:
        task.expands += 1
    return DLS(task, OPEN, modification=modification, debug=debug, maxDepth=maxDepth, ids=ids)


def IDS(task, maxDepth=1):
    depthReached, solved = DLS(task, maxDepth=maxDepth, modification=True, debug=True, ids=True)
    if depthReached:
        IDS(task, maxDepth=maxDepth+1)
    elif not solved:
        return False
    else:
        return True
