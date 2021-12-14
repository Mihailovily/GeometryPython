import actions


class Loading:
    def __init__(self):
        self.bg = actions.load_image("bg.png")

    def show(self, screen):
        screen.blit(self.bg, (0, 0))
