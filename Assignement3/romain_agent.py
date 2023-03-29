from agent import AlphaBetaAgent
from pontu_state import *
import minimax
import copy

"""
Agent skeleton. Fill in the gaps.
"""
class MyAgent(AlphaBetaAgent):
  def get_name(self):
    return 'romain agent'
  """
  This is the skeleton of an agent to play the Tak game.
  """
  def get_action(self, state, last_action, time_left):
    self.last_action = last_action
    self.time_left = time_left
    return minimax.search(state, self)

  """
  The successors function must return (or yield) a list of
  pairs (a, s) in which a is the action played to reach the
  state s.
  """
  def successors(self, state):
      actions = []
      for a in state.get_current_player_actions():
          tmp_state = state.copy()
          tmp_state.apply_action(a)
          actions.append((a,tmp_state))
      return actions

  """
  The cutoff function returns true if the alpha-beta/minimax
  search has to stop and false otherwise.
  """
  def cutoff(self, state, depth):
      if depth == 1 or state.game_over(): return True
      return False

  """
  The evaluate function must return an integer value
  representing the utility function of the board.
  """
  def evaluate(self, state):
      result = 0
      for i in range(3): #for each pawn
        result += sum(not val for val in state.adj_bridges(1 - self.id,i).values())
      return result