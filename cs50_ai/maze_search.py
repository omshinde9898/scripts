from ast import While


maze = [
    [0,0,0,0,0,0,2,0],
    [0,0,0,0,0,2,2,0],
    [0,2,2,2,0,2,0,0],
    [0,2,0,2,2,2,0,0],
    [0,1,0,0,0,0,0,0],
    ]


def prnt_maze(mze):
    for i in mze:
        print(i)

for i in maze:
    for j in i:
        if j == 2:
            i[i.index(j)] = None
        elif j == 0:
            i[i.index(j)] = 'wall'
        elif j == 1:
            i[i.index(j)] = 'You'
            pass


def current_state(mze):
    for i in mze:
        for j in i:
            if j == 'You':
                return [mze.index(i),i.index(j)]
                break
    else:
        print("player not found !!!")



def check_mov(state,mze):
    possible_pos = []
    try:
        if mze[state[0]][state[1] - 1] == None:
            possible_pos.append([state[0],state[1]-1])
    except:
        pass
    try:
        if mze[state[0]][state[1] + 1] == None:
            possible_pos.append([state[0],state[1]+1])
    except:
        pass
    try:
        if mze[state[0] - 1 ][state[1]] == None:
            possible_pos.append([state[0]-1,state[1]])
    except:
        pass
    try:
        if mze[state[0] +1 ][state[1]] == None:
            possible_pos.append([state[0]+1,state[1]])
    except:
        pass
    return possible_pos

state = current_state(maze)

#prnt_maze(maze)
print("Current State : ",current_state(maze))
print("Possible States : ",check_mov(state,maze))

Frontier = []
passed = []
_goal = [0,6]

def goal_check(state,goal):
    if state == goal:
        return True
    else:
        return False

def last_search(st,mze):
    if goal_check(st,_goal) == True:
        print("goal reached !!!!")
    else:
        for i in passed:
            for j in check_mov(st,mze):
                if j == i:
                    pass
                else:
                    Frontier.append(j)
        print("Old State : ",st)
        st = Frontier[-1]
        Frontier.remove(Frontier[-1])
        print("New State : ",st)
        passed.append(st)
        last_search(st,maze)

last_search(state,maze)
print(len(passed))


