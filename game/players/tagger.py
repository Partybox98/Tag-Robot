from player_controls import Player
from pygame import Vector2
import pygame

class Tagger(Player):
  HEIGHT = WIDTH = 1000
  state = 0 # 0 is close gap, 1 is wall, 2 is chase?
  

  def gap(self,run,dis):
    if (self.within(self.pos.x,run.x,dis) and self.within(self.pos.y,run.y,dis)):
      return 1
    else:
      if run.x < self.pos.x:
        self.move_left()
      else:
        self.move_right()
      if run.y < self.pos.y:
        self.move_up()
      else:
        self.move_down()
      return 0


  def wall(self,run,dis):
    if (self.within(self.pos.x,run.x,dis) and self.within(self.pos.y,run.y,dis)):
      if ((self.pos.x - run.x) < (self.pos.y - run.y)): #figure out if it should block x or y
        if run.x < self.pos.x:
          self.move_left()
        else:
          self.move_right()
      else:
        if run.y < self.pos.y:
          self.move_up()
        else:
          self.move_down()
      if (self.within(self.pos.x,run.x,dis/2) and self.within(self.pos.y,run.y,dis/2)):
        return 2
      else:
        return 1
    else:
      return 0
  # called once every frame.
  def act(self):
    dis = 220
    run = self.other_player.pos
    
    if (self.state == 0):
      self.state = self.gap(run,dis)
    elif (self.state == 1):
      self.state = self.wall(run,dis+20)
    elif (self.state == 2):
      print("done") # make a prediction chase function to finish catching it
    else:
      print("error")
    

  
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