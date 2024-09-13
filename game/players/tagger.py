from player_controls import Player
from pygame import Vector2
import pygame

class Tagger(Player):
  cornered = False
  cornered_dis = 100 # find correct value
  HEIGHT = WIDTH = 1000
  centered = False
  
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
      
    if (self.pos == dest):
      return True
    else:
      return self.centered


  
  
  
  
  # called once every frame.
  def act(self):
    
    run = self.other_player.pos
    
    if (self.centered):
      print("done")
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
        
        
        
        
        
        
        
    # if dest.x < self.pos.x:
    #   self.move_left()
    # else:
    #   self.move_right()
    # # important to note that smaller y == higher up.  
    # if dest.y < self.pos.y:
    #   self.move_up()
    # else:
    #   self.move_down()