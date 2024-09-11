
import pygame
from pygame import Vector2
from players.tagger import Tagger
from players.runner import Runner
import time
from settings import * 
START_TIME = time.time()
# player speed
SPEED = 300
# player width
WIDTH = 20
# pygame setup
pygame.init()
# 1000x1000 px square
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
running = True

tagger = Tagger()
runner = Runner()

# execute the specified function on both players.
def execute_on_players(func):
    func(tagger)
    func(runner)

# update the position of the players using their respective movement vector
def move(player):
    player.pos += player.movement_vector * SPEED * dt

# clamp players' position to be inside the window
def clamp(player):
    player.pos.x = max(0, player.pos.x)
    player.pos.x = min(screen.get_width(), player.pos.x)
    player.pos.y = max(0, player.pos.y)
    player.pos.y = min(screen.get_height(), player.pos.y)

def update(dt):
    global running
    # run functions defined by the users to control their AI if manual mode is disabled, otherwise allow controls with WASD / arrow keys.
    keys = pygame.key.get_pressed()
    if TAGGER_IS_MANUAL:
        tagger.__manual_move__(keys)
    else:
        tagger.act()
    if RUNNER_IS_MANUAL:
        runner.__manual_move__(keys)
    else:
        runner.act()

    # draw red at tagger, blue at runner
    pygame.draw.circle(screen, "red", tagger.pos, WIDTH)
    pygame.draw.circle(screen, "blue", runner.pos, WIDTH)

    # normalize movement vectors of the players 
    execute_on_players(lambda player: player.__normalize_movement_vector__())

    # move players
    execute_on_players(move)

    # clamp players' positions
    execute_on_players(clamp)

    # reset player velocity
    execute_on_players(lambda player: player.__stop__())

    # if tagger touches runner then end game
    if abs(tagger.pos.x - runner.pos.x) <= WIDTH and \
       abs(tagger.pos.y - runner.pos.y) <= WIDTH:
        running = False

# start at opposite corners
tagger.pos = Vector2(0, 0)
runner.pos = Vector2(screen.get_width(), screen.get_height())

# give each other a reference to their opponents, so they can strategize accordingly 
tagger.other_player = runner
runner.other_player = tagger

while running:
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # update the player positions and other aspects of the game.
    update(dt)
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    
    

pygame.quit()

end = time.time() - START_TIME
print(f"Tag Time: {end}s")