import pygame
from customer_enemies.White_cap import White_cap

# Music
pygame.mixer.pre_init(frequency=48000, size=-16, channels=1, buffer=512)
pygame.mixer.init()
pygame.mixer.music.load('assets/Paradise.wav')
pygame.mixer.music.set_volume(0.1)

class Game:
    def __init__(self):
        self.width, self.height = 1280, 720
        self.window = pygame.display.set_mode((self.width, self.height))
        self.caption = pygame.display.set_caption('Sweet Defense')
        self.customer_enemies = [White_cap()]
        self.pastrytowers = []
        self.hearts = 3
        self.coins = 100
        self.bg_img = pygame.image.load('map_bg.png')
        self.bg = pygame.transform.scale(self.bg_img, (self.width, self.height))

    def run(self):
        pygame.mixer.music.play(-1)
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

            self.draw()

        pygame.quit()

    def draw(self):
        self.window.fill((0, 0, 0))
        self.window.blit(self.bg, (0, 0))

        for people in self.customer_enemies:
            people.draw(self.window)
        pygame.display.update()


g = Game()
g.run()