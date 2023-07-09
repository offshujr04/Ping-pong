import pygame
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


def paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y-left_paddle.mov_ment >= 0:
        left_paddle.move(up=True)

    elif keys[pygame.K_s] and left_paddle.y+left_paddle.mov_ment+left_paddle.height <= Height:
        left_paddle.move(up=False)

    elif keys[pygame.K_UP] and right_paddle.y-right_paddle.mov_ment >= 0:
        right_paddle.move(up=True)

    elif keys[pygame.K_DOWN] and right_paddle.y+right_paddle.mov_ment+right_paddle.height <= Height:
        right_paddle.move(up=False)


def draw(window, paddles):
    window.fill((0, 0, 0))  # Passing the rgb value of colour black

    for p in paddles:
        p.draw(window)

    pygame.display.update()


def display():
    run = True
    clock = pygame.time.Clock()  # Regulates the frame rate of our game

    left_paddle = Paddle(10, Height//2-paddle_heigth //
                         2, paddle_width, paddle_heigth)
    right_paddle = Paddle(Width-10-paddle_width, Height //
                          2-paddle_heigth//2, paddle_width, paddle_heigth)

    while run:
        clock.tick(Fps)
        draw(Window, [left_paddle, right_paddle])
        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                run = False
                exit()

        keys = pygame.key.get_pressed()
        paddle_movement(keys, left_paddle, right_paddle)

    pygame.quit()


if __name__ == '__main__':
    display()
