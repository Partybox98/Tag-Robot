from player_controls import Player
import pygame

class Tagger(Player):
  cornered = False
  cornered_dis = 50
  
  def corner1(self):
    run = self.other_player.pos
    
    if run.x < self.pos.x:
      self.move_left()
    else:
      self.move_right()
    if run.y < self.pos.y:
      self.move_up()
    else:
      self.move_down()
      
    if (run.x < self.cornered_dis and run.y < self.cornered_dis):
      return True, "TL" # Cornered = True, run_pos = top left / "TL"
    elif (run.x < self.cornered_dis and run.y < self.cornered_dis):
      return True, "BL" # Cornered = True, run_pos = bottom left / "BL"
    elif (run.x < self.cornered_dis and run.y < self.cornered_dis):
      return True, "TR" # Cornered = True, run_pos = top right / "TR"
    elif (run.x < self.cornered_dis and run.y < self.cornered_dis):
      return True, "BR" # Cornered = True, run_pos = bottom right / "BR"
    else:
      return False, ""
  
  
  
  
  
  
  # called once every frame.
  def act(self):
    
    # try to move toward runner
    run = self.other_player.pos
    if (self.cornered == False):
      self.cornered,run_pos = self.corner1()
    else:
      print(f'Cornered, pos:{run_pos}')
    





  
    
    

  
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