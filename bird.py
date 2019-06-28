import pygame

class Bird (pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("yellowbird-midflap.png")
        self.image = pygame.transform.scale(self.image,(40,40))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = pygame.math.Vector2(0,7)
    def update(self):
        self.speed[1] += 0.5
        self.rect.move_ip(self.speed)
    def reset(self,pos):
        self.rect.center = pos
        self.speed = pygame.math.Vector2(0, 7)

