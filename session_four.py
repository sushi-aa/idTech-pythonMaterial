#NEW: Import math library
import pygame, math
from pygame.locals import *
from tetris_pieces import *

pygame.init()

# Colors
black = (0,0,0)
cyan = (0,255,255)
blue = (0,0,255)
orange = (255,100,10)
red = (255,0,0)
yellow = (255,255,0)
green = (0,255,0)
purple = (160,32,240)
gray = (190, 190, 190)
colors = [black, cyan, blue, orange, yellow, green, purple, red]

# Variables for window and tiles
clock = pygame.time.Clock()
FPS = 60
WIDTH = 640
HEIGHT = 480
TILE_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")


def draw_board(board, board_surface):
   for row in range(ROWS):
       for col in range(COLS):
           currentTile = board[row][col]
           tile_x = col * TILE_SIZE
           tile_y = row * TILE_SIZE
           draw_tile(tile_x, tile_y, currentTile, board_surface)


def draw_tile(posX, posY, tile, surface):
   tile_color = colors[tile]
   rect = Rect((posX,posY), (TILE_SIZE, TILE_SIZE))
   pygame.draw.rect(surface, tile_color, rect)
   pygame.draw.rect(surface, gray, rect.inflate(1,1),1)


def draw_play_area(screen_position, screen_surface, board_surface):
   rows_toShow = 20.5
   topY = board_surface.get_height() - rows_toShow * TILE_SIZE
   screen_surface.blit(board_surface,screen_position, Rect((0, topY), (board_surface.get_width(), rows_toShow * TILE_SIZE)))

def draw_tetrimino(posX,posY, tetrimino, board_surface):
   topX = posX
   topY = posY
   rows = len(tetrimino)
   cols = len(tetrimino[0])

   for row in range(rows):
       for col in range(cols):
           tile = tetrimino[row][col]
           if tile != 0: # tile is not black
               tileX = (topX + col) * TILE_SIZE
               tileY = (topY + row) * TILE_SIZE
               draw_tile(tileX, tileY, tile, board_surface)

# NEW: Drop time function this is standard Tetris guidelines. reference: https://tetris.fandom.com/wiki/Tetris_Guideline
def calculate_drop_time(level):
   return math.floor(math.pow((0.8 - ((level - 1) * 0.007)), level-1) * 60)

# NEW: Variables for player information
level = 1
score = 0
new_level = 5 * level
drop_clock = 0
currentDropTime = baseDropTime = calculate_drop_time(level)


# Variables for board
ROWS = 40
COLS = 10
board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
board_surface = pygame.Surface((COLS*TILE_SIZE, ROWS * TILE_SIZE))

# Game States
RESTART = -1
PLAYING = 0
GAME_OVER = 1
game_state = PLAYING

# Create first tetrimino
active_tetrimino = Tetrimino()
active_tetrimino.grid_ref = board
active_tetrimino.reset()

#Game Loop
while True:
   while game_state == PLAYING:
       clock.tick(FPS)
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               quit()

 # NEW: Controlling the tetrinomo
           elif event.type == KEYDOWN:
               if event.key == pygame.K_RIGHT:
                   active_tetrimino.move(1,0)
               elif event.key == pygame.K_LEFT:
                   active_tetrimino.move(-1,0)
               elif event.key == pygame.K_UP or event.key == pygame.K_x:
                   active_tetrimino.rotate(1)
               elif event.key == pygame.K_z or event.key == pygame.K_RCTRL:
                   active_tetrimino.rotate(-1)


       # NEW: Drop clock which indicates how fast the pieces will fall down
       # Increase the drop clock each frame, once we pass current_drop_time, it's time to fall.
       drop_clock += 1
       if drop_clock >= currentDropTime:
           active_tetrimino.move(0, 1)
           drop_clock = 0

       # DELETE: active_tetrimino.move(0,1)
       screen.fill(gray)
       draw_board(board, board_surface)


       # drawing to the board
       draw_tetrimino(active_tetrimino.x, active_tetrimino.y, pieces[active_tetrimino.type][active_tetrimino.rotation],board_surface)
       draw_play_area((10,10), screen, board_surface)
       pygame.display.update()
