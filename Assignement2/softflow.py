from search import *
import copy

#################
# Problem class #
#################

class SoftFlow(Problem):

    def __init__(self, initial):
        super().__init__(initial)
        self.state_intit = initial
        self.state_intit.posexam()                                                             # initialise l'état initial (position et objectif)
        self.store = []
        
    def actions(self, state):
        actions = []
        for pos in state.pos:                                                                   #pour chaque (agent/objectif) différents:
            x, y = state.pos[pos]
            listes_poss = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)] 
            for poss in listes_poss:
                new_pos = state.pos.copy()
                new_pos[pos] = poss                                                             # regarde toutes les actions possible
                string = ""
                for i in state.pos:
                    string+=i+str(new_pos[i])
                if state.grid[poss[0]][poss[1]] == " " and self.store.count(string) == 0:                                         # et verifie qu'elle est legal.
                    actions.append((pos,poss))
        return actions
    

    def result(self, state, action):

        lettre,(x,y) = action                                                                   # initialisation en décomposant (position,lettre de l'agent qui bouge,valeur de son objectif)
        value = str(ord(lettre)-97)

        new_state = state.copy()
        
        new_state.grid[state.pos[lettre][0]][state.pos[lettre][1]] = value                      # remplace l'ancienne position de l'agent par la valeur associé

        if (self.distance((x,y),new_state.exam[value]) == False):                               # verifie si touche l'objectif
            new_state.grid[x][y] = lettre                                                       #       - si non -> nouvelle position = lettre de l'agent
        else:
            new_state.grid[x][y] = value                                                        #       - si oui -> nouvelle position = numéro de l'objectif

        new_state.pos[lettre] =(x,y)                                                            # actualise la position de l'agent
        string = ""
        for i in new_state.pos:
            string+=i+str(new_state.pos[i])
        self.store.append(string)

        return new_state

    def goal_test(self, state):
        h = 0
        for pos,exam in zip(state.pos.values(), state.exam.values()):                           # calcul la somme des distances Manathan de tous les agents
            h+= abs(pos[0] - exam[0])
            h+= abs(pos[1] - exam[1])

        return h == len(state.pos)                                                            # vérifie si tous les agents sont à une distant de 1 de l'objectif (siils sont à coté)     

    def h(self, node):
        state = node.state
        h = 0
        for pos,exam in zip(state.pos.values(), state.exam.values()):
            
            h+= abs(pos[0] - exam[0])
            h+= abs(pos[1] - exam[1])
        return h+(100/self.nbr(state))                                                               # calcule l'heuristique et ajoute une valeur indirectement proportionnelle au nombre d'agent ayant trouvé leur goal

    
    def nbr(self,state):
        count = 1

        for key in state.pos:
            if self.distance(state.pos[key],state.exam[str(ord(key)-97)]):
                count += 1
        return count
    
    
    def distance(self,pos,exam):
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
    
    def copy(self):
        new_pos = self.pos.copy()
        new_exam = self.exam.copy()
        new_grid = [i[:] for i in self.grid]

        return State(new_grid, new_pos, new_exam)





#####################
# Launch the search #
#####################

problem = SoftFlow.load(sys.argv[1])

# example of print

node = astar_search(problem)
path = node.path()

print('Number of moves: ', str(node.depth))
for n in path:
    print(n.state)  # assuming that the _str_ function of state outputs the correct format
    print()