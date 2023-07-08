import pygame
pygame.init()

Width, Height = 700, 500
Window = pygame.display.set_mode((Width, Height))  # Size of window
pygame.display.set_caption("Ping Pong")  # Title of window
Fps = 60


def draw(window):
    window.fill((0, 0, 0))  # Passing the rgb value of colour white

    pygame.display.update()


def display():
    run = True
    clock = pygame.time.Clock()  # Regulates the frame rate of our game

    while run:
        clock.tick(Fps)
        draw(Window)
        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                run = False
                exit()

    pygame.quit()


if __name__ == '__main__':
    display()
