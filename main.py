import pygame
import random
pygame.init()

Width, Height = 700, 500
Window = pygame.display.set_mode((Width, Height))  # Size of window
pygame.display.set_caption("Ping Pong")  # Title of window
Fps = 60
paddle_width, paddle_heigth = 20, 100


class Paddle:

    colour = ((255, 255, 255))  # rgb of white
    mov_ment = 4

    def __init__(self, x, y, width, height):

        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, window):
        pygame.draw.rect(window, self.colour,
                         (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up == True:
            self.y -= self.mov_ment
        else:
            self.y += self.mov_ment


class ball:
    # Initial velocity of the ball when game starts
    def velocity(self):
        vel = random.randint(0, 5)

        if vel == 1 or vel == 3:
            return -5  # First ball will move to the left side
        else:
            return 5  # First ball will move to the right side

    def __init__(self, x, y, r):  # r-Radius
        self.x = x
        self.y = y
        self.r = r

        # Deciding velocity of the ball
        self.x_vel = self.velocity()
        self.y_vel = 0  # Ball will move from the middle

    def draw(self, window):
        pygame.draw.circle(window, (0, 255, 0), (self.x, self.y), self.r)

    # Moving the ball
    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel


def paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y-left_paddle.mov_ment >= 0:
        left_paddle.move(up=True)

    elif keys[pygame.K_s] and left_paddle.y+left_paddle.mov_ment+left_paddle.height <= Height:
        left_paddle.move(up=False)

    elif keys[pygame.K_UP] and right_paddle.y-right_paddle.mov_ment >= 0:
        right_paddle.move(up=True)

    elif keys[pygame.K_DOWN] and right_paddle.y+right_paddle.mov_ment+right_paddle.height <= Height:
        right_paddle.move(up=False)


def draw(window, paddles, ball):
    window.fill((0, 0, 0))  # Passing the rgb value of colour black

    for p in paddles:
        p.draw(window)
# Creating a middle line

    for i in range(10, Height, Height//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(Window, (255, 255, 255),
                         ((Width//2)-5, i, 10, Height//20))

    ball.draw(window)
    pygame.display.update()


def display():
    run = True
    clock = pygame.time.Clock()  # Regulates the frame rate of our game

    left_paddle = Paddle(10, Height//2-paddle_heigth //
                         2, paddle_width, paddle_heigth)
    right_paddle = Paddle(Width-10-paddle_width, Height //
                          2-paddle_heigth//2, paddle_width, paddle_heigth)

    pong_ball = ball(Width//2, Height//2, 7)

    while run:
        clock.tick(Fps)
        draw(Window, [left_paddle, right_paddle], pong_ball)
        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                run = False
                exit()

        keys = pygame.key.get_pressed()
        paddle_movement(keys, left_paddle, right_paddle)
        pong_ball.move()
    pygame.quit()


if __name__ == '__main__':
    display()
