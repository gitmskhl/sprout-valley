import pygame

from scripts import settings, player, keyboard

class App:
    def __init__(self):
        pygame.init()
        self._init_display()
        self.clock = pygame.time.Clock()
        # key bindings
        keyboard.init_key_bindings()
        # camera
        self.camera = [0, 0]
        # main player
        self.main_player = player.Player((100, 100), (3, 3))

    def _init_display(self):
        settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT = pygame.display.get_desktop_sizes()[0]
        self.main_display = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        self.display = pygame.Surface((settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT // 2))
        pygame.display.set_caption("Sprout Valley")

    def run(self):
        while True:
            self.clock.tick(settings.FPS)
            self.display.fill("black")
            
            self.main_player.update()
            self.main_player.render(self.display, self.camera)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == keyboard.KEY_BINDINGS['up']:
                        self.main_player.move[0] = True
                    elif event.key == keyboard.KEY_BINDINGS['right']:
                        self.main_player.move[1] = True
                    elif event.key == keyboard.KEY_BINDINGS['down']:
                        self.main_player.move[2] = True
                    elif event.key == keyboard.KEY_BINDINGS['left']:
                        self.main_player.move[3] = True

                elif event.type == pygame.KEYUP:
                    if event.key == keyboard.KEY_BINDINGS['up']:
                        self.main_player.move[0] = False
                    elif event.key == keyboard.KEY_BINDINGS['right']:
                        self.main_player.move[1] = False
                    elif event.key == keyboard.KEY_BINDINGS['down']:
                        self.main_player.move[2] = False
                    elif event.key == keyboard.KEY_BINDINGS['left']:
                        self.main_player.move[3] = False

            scaled_display = pygame.transform.scale(self.display, (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
            self.main_display.blit(scaled_display, (0, 0))
            pygame.display.update()


if __name__ == "__main__":
    app = App()
    app.run()
