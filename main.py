import pygame


if __name__ == "__main__":
    pygame.init()

    #create screen
    screen = pygame.display.set_mode((500,500))

    #game loop
    running = True
    while running:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((0,0,0))
        pygame.display.update()