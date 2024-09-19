#Import the pygame library
import pygame
import random

#Define the colors
BLACK = (0,0,0)
PINK = (255,0,255)
WHITE = (255,255,255)

#Initialize the game engine
pygame.init()

#Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")

class Paddle(pygame.sprite.Sprite):
    def __init__(self, width, height, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        #draw the paddle
        pygame.draw.rect(self.image, color, [0,0,width,height])
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
            self.rect.y -= pixels

    def moveDown(self, pixels):
            self.rect.y += pixels

'''
This class represents a ball. It derives from the "Sprite"
class in Pygame.
'''

class Ball(pygame.sprite.Sprite):
    def __init__(self, width, height, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        #draw the paddle
        pygame.draw.rect(self.image, color, [0,0,width,height])
        self.rect = self.image.get_rect()

        #Fetch the rectangle object that has dimensions of the image
        self.rect = self.image.get_rect()

        #To make the speed of ball random
        self.velocity = [random.randint(1,3), random.randint(1,3)]
        
        #To make the speed of ball same
        #self.velocity = [2,2]

    def update(self):
            self.rect.x += self.velocity[0]
            self.rect.y += self.velocity[1]

#The clock will be used to control how fast the screen updates.
clock = pygame.time.Clock()

#Create the paddle A
paddleA = Paddle(10, 100, WHITE)
paddleA.rect.x = 20
paddleA.rect.y = 200

#Create the paddle B
paddleB = Paddle(10, 100, PINK)
paddleB.rect.x = 670
paddleB.rect.y = 200

#Create the ball sprite
ball = Ball(10, 10, PINK)
ball.rect.x = 300
ball.rect.y = 300

#This list will contain all the sprites we intend to use in our game
all_sprites_list = pygame.sprite.Group()

#Add the paddles and ball to the list of sprites
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

scoreA = 0
scoreB = 0

keep_going = True
game_Over = False

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #If the user clicks the close button
            keep_going = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                keep_going = False
            if event.key == pygame.K_r:
                scoreA = 0
                scoreB = 0
                ball.rect.x = 350
                ball.rect.y = 250
                ball.velocity = [random.randint(1, 3), random.randint(-3, -3)]
                game_Over = False

    keys = pygame.key.get_pressed()

    #Moving the paddle B when the user uses up and down arrow keys
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)

    #Moving the paddle A when the user uses W and S keys
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)

    #Game logic should go here
    all_sprites_list.update()

    #Check if the ball is bouncing against any of the 4 walls
    if ball.rect.x <= 20 and not game_Over:
        ball.velocity[0] *= -1
        scoreB += 1

    if ball.rect.x >= 680 and not game_Over:
        ball.velocity[0] *= -1
        scoreA += 1

    if ball.rect.y >= 490 or ball.rect.y <= 10:
        ball.velocity[1] *= -1

    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.velocity[0] *= -1
        ball.velocity[1] = random.randint(-1, 3)

    #clear the screen to black
    screen.fill(BLACK)

    pygame.draw.line(screen, WHITE, [350, 0], [350, 500], 5)
    all_sprites_list.draw(screen)

    #pygame.draw.line(screen, WHITE, [20, 200], [20, 300], 10)
    #pygame.draw.line(screen, WHITE, [670, 200], [670, 300], 10)

    #font size of score and message
    font = pygame.font.Font(None, 25)

    #Display the score
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (200, 20))

    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (500, 20))

    if scoreA > 5 or scoreB > 5:
        gameOver = True
        ball.velocity = [0, 0]
        if scoreA > scoreB:
            message = "A won the game"
        else:
            message = "B won the game"

        text = font.render(message, 1, WHITE)
        screen.blit(text, (220, 250))

    #Update the screen
    pygame.display.flip()

    #Limit to 120 frames per second
    clock.tick(120)

pygame.quit()