
import time
import sys
from copy import deepcopy
from search import *


#################
# Problem class #
#################
class TowerSorting(Problem):

    def actions(self, state):
        """Returns the list of all possible actions that can be taken rom the current state"""
        actions = []
        num_towers = state.number
        siz_towers = state.size
        for i in reversed(range(num_towers)):
            for j in reversed(range(num_towers)):
                # if the i-th tower is not empty and the j-th tower is not full
                if i != j and len(state.grid[j]) < siz_towers and len(state.grid[i]) > 0:
                    # move the top disk from i-th tower to j-th tower
                    actions.append((i,j))
        #print(actions)
        return actions

    def result(self, state, action):
        """Returns the new state after taking the given action"""
        i, j = action
        #print(action)
        current = deepcopy(state)
        current.move = f"Move disk from tower {i} to tower {j}"
        current.grid[j].append(current.grid[i].pop())
        #print(current.grid)
        return current

    def goal_test(self, state):
        height = len(state.grid[0])
        for i in range(len(state.grid)):
            # print(state.grid)
            if state.grid[i] != []:
                for j in range(len(state.grid[i])):
                    if state.grid[i][j] != state.grid[i][0] or len(state.grid[i]) != height:
                        return False
        return True
                


###############
# State class #
###############
class State:

    def __init__(self, number, size, grid, move="Init"):
        self.number = number
        self.size = size
        self.grid = grid
        self.move = move

    def __str__(self):
        s = self.move + "\n"
        for i in reversed(range(self.size)):
            for tower in self.grid:
                if len(tower) > i:
                    s += "".join(tower[i]) + " "
                else:
                    s += ". "
            s += "\n"
        return s

    def __eq__(self, other):
        return (self.number == other.number and self.size == other.size and self.grid == other.grid)

    def __hash__(self):
        return hash(str(self.grid))


######################
# Auxiliary function #
######################
def read_instance_file(filepath):
    with open(filepath) as fd:
        lines = fd.read().splitlines()

    number_tower, size_tower = tuple([int(i) for i in lines[0].split(" ")])
    initial_grid = [[] for i in range(number_tower)]
    for row in lines[1:size_tower+1]:
        elems = row.split(" ")
        for index in range(number_tower):
            if elems[index] != '.':
                initial_grid[index].append(elems[index])

    for tower in initial_grid:
        tower.reverse()

    return number_tower, size_tower, initial_grid


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: ./sort_tower.py")
        
    filepath = sys.argv[1]

    number, size, initial_grid = read_instance_file(filepath)
    # print(number, size, initial_grid)    
    
    
    init_state = State(number, size, initial_grid, "Init")
    problem = TowerSorting(init_state)
    
    # Tests
    #print(problem.actions(init_state))
    #(problem.result(init_state, (2, 1)))
    #print(problem.goal_test(init_state))
    
    # Example of search
    start_timer = time.perf_counter()
    node, nb_explored, remaining_nodes = depth_first_graph_search(problem)
    end_timer = time.perf_counter()

    # Example of print
    path = node.path()

    for n in path:
        # assuming that the __str__ function of state outputs the correct format
        print(n.state)

    print(f"{str(end_timer - start_timer)} & {nb_explored} & {remaining_nodes}")
