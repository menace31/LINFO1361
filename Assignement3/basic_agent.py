import minimax
import random
from agent import Agent

class MyAgent(Agent):

  def get_action(self, state, last_action, time_left):
    print(state.cur_pos)
    actions = state.get_current_player_actions()
    action = random.choice(actions)
    return action
  
  def get_name(self):
    return 'Dummy agent'