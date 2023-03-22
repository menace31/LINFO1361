from search import *
import sys
import string
from copy import deepcopy
import time


#################
# Problem class #
#################

class SoftFlow(Problem):
    
    def __init__(self, initial):
        self.initial = initial
        self.pos_end = [0]*10  # position of goal points
        for i in range(initial.nbr):
            for j in range(initial.nbc):
                if initial.grid[i][j].isdigit():
                    self.pos_end[int(initial.grid[i][j])] = (i,j)
                    
    def actions(self, state):
        actions = []
        for i in state.pos_cable.keys():
            
            if state.pos_cable[i] != self.pos_end[ord(i) - 97]:
                d = state.pos_cable.get(i)

                if d[0] + 1 <= state.nbr and state.grid[d[0] + 1][d[1]] == ' ':
                    actions.append((d[0],d[1],d[0] + 1, d[1])) #move down
                    
                if d[0] - 1 >= 0 and state.grid[d[0] - 1][d[1]] == ' ':
                    actions.append((d[0],d[1],d[0] - 1, d[1])) #move up

                    
                if d[1] + 1 <= state.nbc and state.grid[d[0]][d[1]+1] == ' ':
                    actions.append((d[0],d[1],d[0], d[1]+1)) #move right
                    
                if d[1] - 1 >= 0 and state.grid[d[0]][d[1]- 1] == ' ':
                    actions.append((d[0],d[1],d[0], d[1]- 1)) #move left
                
        return actions

    def result(self, state, action):
        x1, y1, x2, y2 = action
        new_state = State(deepcopy(state.grid)) # copy itinial grid
        new_state.grid[x2][y2] = state.grid[x1][y1]
        new_state.pos_cable[new_state.grid[x2][y2]] = (x2, y2)
        new_state.grid[x1][y1] = str(ord(new_state.grid[x1][y1]) - 97) #turn a -> 0, b -> 1, etc
        
        
        if self.dist(new_state.grid[x2][y2],new_state) <= 1:
            d = new_state.grid[x2][y2]
            new_state.pos_cable[d] = self.pos_end[ord(d)- 97]
            new_state.grid[x2][y2] = str(ord(d)- 97)
            
        return new_state

    def goal_test(self, state):
        return sum(word in string.ascii_lowercase for sublist in state.grid for word in sublist) == 0; #if there are no moreletter (a to z) on the grid. Assuming that it won't overlap anything

    def h(self, node):
        # add the Manhattan distance between the entry and exit points to the heuristic value
        h = 0.0
        for i in node.state.pos_cable.keys():
            d = node.state.pos_cable.get(i)
            e = self.pos_end[ord(i) - 97]
            h += abs(d[0] - e[0]) + abs(d[1] - e[1])  
        return h

    def load(path):
        with open(path, 'r') as f:
            lines = f.readlines()
        
        state = State.from_string(''.join(lines))
        return SoftFlow(state)
    
    def dist(self,n, state):
        # Calculates the distance between n and its goal
        d = state.pos_cable.get(n)
        e = self.pos_end[ord(n) - 97]
        return abs(d[0] - e[0]) + abs(d[1] - e[1])



###############
# State class #
###############

class State:

    def __init__(self, grid):
        self.nbr = len(grid) # number of rows
        self.nbc = len(grid[0]) # number of columns
        self.grid = grid
        self.pos_cable = {}
        for i in range(self.nbr):
            for j in range(self.nbc):
                if grid[i][j] in string.ascii_lowercase:
                    self.pos_cable[grid[i][j]] = (i,j)
                    
        
    def __str__(self):
        return '\n'.join(''.join(row) for row in self.grid)

    def __eq__(self, other_state):
        return self.grid == other_state.grid and self.pos_cable == other_state.pos_cable

    def __hash__(self):
        return hash(str(self.grid)) ^ hash(str(self.pos_cable))
    
    def __lt__(self, other):
        return hash(self) < hash(other)

    def from_string(string):
        lines = string.strip().splitlines()
        return State(list(
            map(lambda x: list(x.strip()), lines)
        ))






#####################
# Launch the search #
#####################

problem = SoftFlow.load(sys.argv[1])

node = astar_search(problem)


# example of print
path = node.path()

print('Number of moves: ', str(node.depth))
# for n in path:
#     print(n.state)  # assuming that the _str_ function of state outputs the correct format
#     print()


