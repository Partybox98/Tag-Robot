from player_controls import Player
import pygame

class Tagger(Player):
  # called once every frame.
  def act(self):
    # SAMPLE CODE, feel free to delete
    
    # try to move toward runner
    dest = self.other_player.pos

    if dest.x < self.pos.x:
      self.move_left()
    else:
      self.move_right()
    # important to note that smaller y == higher up.  
    if dest.y < self.pos.y:
      self.move_up()
    else:
      self.move_down()

  
  def __manual_move__(self, keys):
    if keys[pygame.K_UP]:
        self.move_up()
    if keys[pygame.K_DOWN]:
        self.move_down()
    if keys[pygame.K_LEFT]:
        self.move_left()
    if keys[pygame.K_RIGHT]:
        self.move_right()