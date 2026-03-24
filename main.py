import pygame

from scripts import settings, player, keyboard, ui, map

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
        # ui
        self.ui = ui.UI(self)
        # map
        self.map = map.Map()

    def _init_display(self):
        settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT = pygame.display.get_desktop_sizes()[0]
        settings.SCREEN_HEIGHT -= 80
        self.main_display = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        self.display = pygame.Surface((settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT // 2))
        pygame.display.set_caption("Sprout Valley")

    def run(self):
        while True:
            self.clock.tick(settings.FPS)
            self.display.fill("black")
            
            # map
            self.map.update()
            self.map.render(self.display, self.camera)

            # main player
            self.main_player.update()
            self.main_player.render(self.display, self.camera)

            # ui
            self.ui.display()

            # camera movement
            self.camera[0] += (self.main_player.pos[0] - settings.SCREEN_WIDTH // 4 - self.camera[0]) // 30
            self.camera[1] += (self.main_player.pos[1] - settings.SCREEN_HEIGHT // 4 - self.camera[1]) // 30


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
                    elif event.key == keyboard.KEY_BINDINGS['use_tool']:
                        self.main_player.use_tool()
                    elif event.key == keyboard.KEY_BINDINGS['switch_tool']:
                        self.main_player.switch_tool()
                    elif event.key == keyboard.KEY_BINDINGS['use_seed']:
                        self.main_player.use_seed()
                    elif event.key == keyboard.KEY_BINDINGS['switch_seed']:
                        self.main_player.switch_seed()
                    

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
