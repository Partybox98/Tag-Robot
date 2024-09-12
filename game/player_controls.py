from pygame import Vector2
import pygame
import math

WIDTH = HEIGHT = 1000
class Player:
  def __init__(self) -> None:
      # game.py will use this movement vector to decide where to move the player.
      self.movement_vector = Vector2()
      self.pos = Vector2()
      # other player(will be updated by game.py)
      self.other_player = None
  
  # note that you can move in two directions at once.

  def move_up(self):
      self.movement_vector += Vector2(0, -1)
  def move_down(self):
      self.movement_vector += Vector2(0, 1)
  def move_left(self):
      self.movement_vector += Vector2(-1, 0)
  def move_right(self):
      self.movement_vector += Vector2(1, 0)

  # set the player's movement vector to 'vector'.
  def set_movement_vector(self, vector):
      self.movement_vector = vector
      
  """
  WARNING: BELOW THIS IS GAME DEFINED.
  DO NOT CALL.
  """      
  def __normalize_movement_vector__(self):
      # since a^2 + b^2 <= 1 (otherwise diagonal movement would be faster), we have to do some transformations.

      # a^2 + b^2 > 1, which means they are going at sqrt(2) times the normal rate.
      sqrtsum = math.sqrt(self.movement_vector.x ** 2 + self.movement_vector.y ** 2)
      if sqrtsum == 0: return

      self.movement_vector /= sqrtsum
  
  def __stop__(self):
      self.movement_vector = Vector2()
  
  def __repr__(self) -> str:
      return f"""Player: 
        position: {self.pos}
        movement vector: {self.movement_vector}
      """
  

class Utils:
  def get_screen_width():
      return WIDTH
  def get_screen_height():
      return HEIGHT
  # return whether position represented by vector is in bounds.
  def in_bounds(vector):
      return 0 <= vector.x <= WIDTH and 0 <= vector.y <= HEIGHT
  # calculate distance between two points.
  def calc_dist(vec1, vec2):
      return math.hypot(abs(vec1.x-vec2.x), abs(vec1.y-vec2.y))