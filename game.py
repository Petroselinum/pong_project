import pgzrun
from random import randint, choice

# Additional functions
def update_ball_position():
    ball.x += ball.speed if ball.direction_x == 'right' else -ball.speed
    ball.y += ball.speed if ball.direction_y == 'up' else -ball.speed
    if ball.x < 5: ball.direction_x = 'right'
    elif ball.x > WIDTH-5: ball.direction_x = 'left'
    if ball.y < 5: ball.winner = 'Gamer B'
    elif ball.y > HEIGHT-5: ball.winner = 'Gamer A'

# Game start
WIDTH= 1280
HEIGHT= 853
TITLE= 'PONG IS COOL'

# Objects definitions
class Palette:
    def __init__(self, palette, position):
        '''Palette features'''
        self.palette=palette
        self.palette.x=position[0]
        self.palette.y=position[1]
        self.palette.speed=5
    def drawing(self):
        '''Object method'''
        self.palette.draw()
    def move(self, direction):
        '''x-axis position update'''
        self.palette.x += self.palette.speed if direction == 'right' else -self.palette.speed

palette_a = Actor('palette.png')
palette_a.y = 10
palette_a.x = randint(70, 1210)
palette_b = Actor('palette.png')
palette_b.y = 843
palette_b.x= randint(70, 1210)
ball = Actor('ball.png')
ball.y = HEIGHT//2
ball.x = WIDTH//2

# Options
ball.direction_x= choice(('left', 'right'))
ball.direction_y= choice(('up', 'down'))
ball.speed=2
ball.winner= None

# Main Control functions
def update():
    update_ball_position()

def draw():
    screen.blit('nature-g4925778c3_1280', (0, 0))
    palette_a.draw()
    palette_b.draw()
    ball.draw()
pgzrun.go()
