from player_controls import Player, Utils
from pygame import Vector2
import pygame
import copy
import math
class Runner(Player):
  # called once every frame.
  def act(self):
    # get other player's movement vector
    tagger = self.other_player

    # try all rotations(in increments of 3 to not be too computationally intensive) and find the one that gives the most distance
    cand_vector = copy.deepcopy(tagger.movement_vector)
    
    best_dist = 0
    best_vector = cand_vector
    for i in range(120):
      # try the rotated version
      new_vector = cand_vector.rotate(i*3)
      
      # raycast 5 steps forward
      new_pos = self.pos + new_vector * 10

      # out of bounds, invalid
      if not Utils.in_bounds(new_pos):
        continue
      
      # we don't want our runner to stay in the corner, so calculate a weight that gets better as we get further away from the corner
      weight = min(new_pos.x, Utils.get_screen_width()-new_pos.x) +min(new_pos.y, Utils.get_screen_height()-new_pos.y)
      weight *= 100
      # the further away from the wall we are, the less it matters. I found that sqrt works best for this purpose, experimentation with different constants, logs, etc are welcome
      weight = math.sqrt(weight) 

      # calculate distance
      dist = Utils.calc_dist(tagger.pos, self.pos + new_vector * 10) + weight

      # new best distance, update accordingly
      if dist > best_dist:
        best_dist = dist
        best_vector = new_vector

    self.set_movement_vector(best_vector)  


  def __manual_move__(self, keys):
    if keys[pygame.K_w]:
        self.move_up()
    if keys[pygame.K_s]:
        self.move_down()
    if keys[pygame.K_a]:
        self.move_left()
    if keys[pygame.K_d]:
        self.move_right()