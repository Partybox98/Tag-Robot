from player_controls import Player
from pygame import Vector2
import pygame

class Tagger(Player):
  HEIGHT = WIDTH = 1000
  centered = False
  gapv = False
  
  def center(self):
    dest = Vector2(self.WIDTH/2, self.HEIGHT/2)
    if dest.x < self.pos.x:
      self.move_left()
    else:
      self.move_right()
    if dest.y < self.pos.y:
      self.move_up()
    else:
      self.move_down()
    # if (self.pos.x < (self.WIDTH/2 + 10) and self.pos.x > (self.WIDTH/2 - 10) and self.pos.y < (self.HEIGHT/2 + 10) and self.pos.y > (self.HEIGHT/2 - 10)):
    if (self.within(self.pos.x,self.WIDTH/2,10) and self.within(self.pos.y,self.HEIGHT/2,10)):
      return True

  def gap(run):
    if (run.pos.x == 0):
      return True

  
  # called once every frame.
  def act(self):
    
    run = self.other_player.pos
    
    if (self.centered):
      self.gapv = self.gap(run)
    else:
      self.centered = self.center()
    

  
  def __manual_move__(self, keys):
    if keys[pygame.K_UP]:
        self.move_up()
    if keys[pygame.K_DOWN]:
        self.move_down()
    if keys[pygame.K_LEFT]:
        self.move_left()
    if keys[pygame.K_RIGHT]:
        self.move_right()
        
        
        
  def within(self,a,b,d):
    if ((b - d) <= a <= (b + d)):
      return True
    else:
      return False
        
        
        
    # if dest.x < self.pos.x:
    #   self.move_left()
    # else:
    #   self.move_right()
    # # important to note that smaller y == higher up.  
    # if dest.y < self.pos.y:
    #   self.move_up()
    # else:
    #   self.move_down()