from search import *
import copy

#################
# Problem class #
#################

class SoftFlow(Problem):

    def __init__(self, initial):
        super().__init__(initial)
        self.state_intit = initial
        self.state_intit.posexam()
        self.liste = []
        
    def actions(self, state):
        actions = []
        new_pos = state.pos.copy()
        for pos, exam in zip(state.pos, state.exam.values()):
            x, y = state.pos[pos]
            listes_poss = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            for poss in listes_poss:
                new_pos[pos] = (x,y)
                if state.grid[poss[0]][poss[1]] == " " and self.liste.count(state.grid)==0:
                    actions.append((state.grid[x][y],poss))
        return actions

    def result(self, state, action):
        new_grid = []
        for i in state.grid:
            new_grid.append(i[:])

        new_pos = state.pos.copy()
        new_exam = state.exam.copy()

        new_state = State(new_grid, new_pos, new_exam)
        value = action[0]
        new_state.grid[state.pos[value][0]][state.pos[value][1]] = str(ord(value)-97)
        if (state.grid[action[1][0]][action[1][1]].isdigit() == False):
            new_state.grid[action[1][0]][action[1][1]] = action[0]
        new_pos[value] = action[1]


        self.liste.append(new_pos)
        return new_state

    def goal_test(self, state):
        h = 0
        for pos,exam in zip(state.pos.values(), state.exam.values()):
            
            h+= abs(pos[0] - exam[0])
            h+= abs(pos[1] - exam[1])
        if(h <=len(state.pos)):
            for i in range (len(state.grid)):
                for j in range (len(state.grid[i])):
                    if state.grid[i][j].isalpha():
                        state.grid[i][j] = str(ord(state.grid[i][j])-97)
        return h <=len(state.pos)

    def h(self, node):
        state = node.state
        h = 0
        for pos,exam in zip(state.pos.values(), state.exam.values()):
            
            h+= abs(pos[0] - exam[0])
            h+= abs(pos[1] - exam[1])

        return h+(100/self.nbr(state))

    
    def nbr(self,state):
        count = 1

        for key in state.pos:
            if self.distance2(state.pos[key],state.exam[str(ord(key)-97)]):
                count += 1
        return count
    
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
        state.posexam()
        return SoftFlow(state)



###############
# State class #
###############

class State:

    def __init__(self, grid,pos={},exam={}):
        self.nbr = len(grid)
        self.nbc = len(grid[0])
        self.grid = grid
        self.pos = pos
        self.exam = exam

    def posexam(self):
        for i, line in enumerate(self.grid):
            for j, x in enumerate(line):
                if(x != "#" and x!= " "):
                    if x.isalpha():
                        self.pos[x] = (i, j)
                    else:
                        self.exam[x] = (i, j)
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

        return State(grid)





#####################
# Launch the search #
#####################

problem = SoftFlow.load(sys.argv[1])



# example of print
def test():
    node = astar_search(problem)
    path = node.path()

    print('Number of moves: ', str(node.depth))
    for n in path:
        print(n.state)  # assuming that the _str_ function of state outputs the correct format
        print()

test()
