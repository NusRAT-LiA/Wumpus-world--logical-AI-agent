import pygame

# Speed
SPEED = 50          # Change the speed of the game here.

# Window
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 710
CAPTION = 'Wumpus World'

# Cell
IMG_INITIAL_CELL = './Assets/Images/initial_cell.png'
IMG_DISCOVERED_CELL = './Assets/Images/discovered_cell.png'

# Object
IMG_PIT = './Assets/Images/pit.png'
IMG_WUMPUS = './Assets/Images/wumpus.png'
IMG_GOLD = './Assets/Images/gold.png'

# Hunter
IMG_HUNTER_RIGHT = './Assets/Images/hunter_right.png'
IMG_HUNTER_LEFT = './Assets/Images/hunter_left.png'
IMG_HUNTER_UP = './Assets/Images/hunter_up.png'
IMG_HUNTER_DOWN = './Assets/Images/hunter_down.png'

IMG_ARROW_RIGHT = './Assets/Images/arrow_right.png'
IMG_ARROW_LEFT = './Assets/Images/arrow_left.png'
IMG_ARROW_UP = './Assets/Images/arrow_up.png'
IMG_ARROW_DOWN = './Assets/Images/arrow_down.png'

# Map
MAP_LIST = ['./Assets/Input/map_1.txt']
MAP_NUM = len(MAP_LIST)

# Output
OUTPUT_LIST = ['./Assets/Output/result_1.txt']

# Fonts
FONT_GRINCHED = './Assets/Fonts/Grinched.ttf'

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GREY = (170, 170, 170)
DARK_GREY = (75, 75, 75)
RED = (255, 0, 0)
GREEN = (60,179,113)

# state
RUNNING = 'running'
GAMEOVER = 'gameover'
WIN = 'win'
TRYBEST = 'trybest'
MAP = 'map'

LEVEL_1_POS = pygame.Rect(235, 120, 500, 50)
LEVEL_2_POS = pygame.Rect(235, 200, 500, 50)
LEVEL_3_POS = pygame.Rect(235, 280, 500, 50)
LEVEL_4_POS = pygame.Rect(235, 360, 500, 50)
LEVEL_5_POS = pygame.Rect(235, 440, 500, 50)
EXIT_POS = pygame.Rect(235, 520, 500, 50)
