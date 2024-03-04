import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Game")

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Nave espacial
class Ship(pygame.sprite.Sprite):  # Heredar de pygame.sprite.Sprite
    def __init__(self):
        super().__init__()  # Llamar al constructor de la clase base
        self.image = pygame.Surface((50, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 20
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Mantener la nave dentro de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

# Asteroide
class Asteroid(pygame.sprite.Sprite):  # Heredar de pygame.sprite.Sprite
    def __init__(self):
        super().__init__()  # Llamar al constructor de la clase base
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

# Grupos de sprites
all_sprites = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

# Crear la nave
ship = Ship()
all_sprites.add(ship)

# Crear asteroides
for i in range(8):
    asteroid = Asteroid()
    all_sprites.add(asteroid)
    asteroids.add(asteroid)

# Reloj
clock = pygame.time.Clock()

# Loop del juego
running = True
while running:
    # Control de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar
    all_sprites.update()

    # Colisiones
    hits = pygame.sprite.spritecollide(ship, asteroids, False)
    if hits:
        running = False

    # Dibujar / Renderizar
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

    # Controlar la velocidad del juego
    clock.tick(60)

pygame.quit()
