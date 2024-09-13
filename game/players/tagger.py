from player_controls import Player
from pygame import Vector2
import pygame

class Tagger(Player):
  cornered = False
  cornered_dis = 100 # find correct value
  HEIGHT = WIDTH = 1000
  centered = False
  run_pos = ""
  
  def corner1(self): # fix movement to corner better
    run = self.other_player.pos
    
    r_left = False
    r_up = False
    
    if run.x < self.WIDTH/2:
      r_left = True
    if run.y < self.WIDTH/2:
      r_up = True
      
    r_quad = ""
    if (r_left):
      r_quad += "left"
    else:
      r_quad += "right"
    r_quad += " "
    if (r_up):
      r_quad += "up"
    else:
      r_quad += "down"
    return r_quad
      
      
      
    # change to give directions for cornering
    
    
    
    # if (run.x < self.cornered_dis and run.y < self.cornered_dis):
    #   return "TL"
    # elif (run.x < self.cornered_dis and run.y > self.HEIGHT - self.cornered_dis):
    #   return "BL"
    # elif (run.x > self.HEIGHT - self.cornered_dis and run.y < self.cornered_dis):
    #   return "TR" 
    # elif (run.x > self.HEIGHT - self.cornered_dis and run.y < self.HEIGHT - self.cornered_dis):
    #   return "BR"
    # else:
    #   return ""
  
  def center(self): # fix pls
    dest = Vector2(self.WIDTH/2, self.HEIGHT/2)
    if dest.x < self.pos.x:
      self.move_left()
    else:
      self.move_right()
    # important to note that smaller y == higher up.  
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
    
    
    
    # try to move toward runner
    run = self.other_player.pos
    
    if (self.centered):
      if (self.run_pos == ""):
        self.run_pos = self.corner1()
      else:
        self.cornered = True
        print(f'Cornered, pos:{self.run_pos}')
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