from search import *
import copy

#################
# Problem class #
#################

class SoftFlow(Problem):

    def __init__(self, initial):
        super().__init__(initial)
        self.state_intit = initial
        
    def actions(self, state):
        actions = []
        for pos, exam in zip(state.pos.values(), state.exam.values()):
            x, y = pos
            listes_poss = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            for poss in listes_poss:
                if state.grid[poss[0]][poss[1]] == " " and self.distance2(pos,exam) == False:
                    actions.append((state.grid[x][y],poss))
        return actions

    def result(self, state, action):
        new_grid = []
        for i in state.grid:
            new_grid.append(i[:])

        new_pos = state.pos.copy()

        new_state = State(new_grid, new_pos, state.exam)
        value = action[0]
        new_state.grid[state.pos[value][0]][state.pos[value][1]] = str(value)
        if (state.grid[action[1][0]][action[1][1]].isdigit() == False):
            new_state.grid[action[1][0]][action[1][1]] = action[0]
        new_pos[value] = action[1]
        char = str(ord(action[0])-97)
        if(self.distance2(new_pos[action[0]],state.exam[char])):
            del new_pos[action[0]]

        print(new_state)
        return new_state

    def goal_test(self, state):
        return state.pos == state.exam

    def h(self, node):
        state = node.state
        h = 0
        for pos,exam in zip(state.pos.values(), state.exam.values()):
            
            h+= abs(pos[0] - exam[0])
            h+= abs(pos[1] - exam[1])

        return h
    
    def distance2(self,pos,exam):
        h = 0
        h+= abs(pos[0] - exam[0])
        h+= abs(pos[1] - exam[1])
        if h <= 1:
            return True
        return False
        

    def load(path):
        with open(path, 'r') as f:
            lines = f.readlines()
            
        state = State.from_string(''.join(lines))
        return SoftFlow(state)



###############
# State class #
###############

class State:

    def __init__(self, grid, pos=None, exam=None):
        self.nbr = len(grid)
        self.nbc = len(grid[0])
        self.grid = grid
        self.pos = pos
        self.exam = exam
        
    def __str__(self):
        return '\n'.join(''.join(row) for row in self.grid)

    def __eq__(self, other_state):
        pass

    def __hash__(self):
        return hash(str(self.grid))
    
    def __lt__(self, other):
        pass

    def from_string(string):
        lines = string.strip().splitlines()
        grid = list(map(lambda x: list(x.strip()), lines))
        pos = {}
        exam = {}
        for i, line in enumerate(lines):
            for j, x in enumerate(line.strip()):
                if(x != "#" and x!= " "):
                    if x.isalpha():
                        pos[x] = (i, j)
                    else:
                        exam[x] = (i, j)
        return State(grid, pos, exam)





#####################
# Launch the search #
#####################

problem = SoftFlow.load(sys.argv[1])

#print(problem.state_intit.pos)
#print(problem.state_intit.exam)
#a = problem.actions(problem.state_intit)
#print(a)


# example of print
def test():
    node = astar_search(problem)
    path = node.path()

    print('Number of moves: ', str(node.depth))
    print(node.state)
    #for n in path:
        #print(n.state)  # assuming that the _str_ function of state outputs the correct format
        #print()

test()
