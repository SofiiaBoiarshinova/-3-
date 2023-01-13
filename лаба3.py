import pygame
import random
import math

pygame.init()

display = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()
FPS = 100


def choose_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


class Circles():
    def __init__(self, r, x, y):
        self.color = choose_random_color()
        self.radius = r
        self.x = x
        self.y = y
        angle = random.uniform(-60, 360)                        # угол
        velocity_mag = random.uniform(.3, 4)                    # радиус разброса
        self.vx = velocity_mag * math.cos(math.radians(angle))  # velocity x
        self.vy = -velocity_mag * math.sin(math.radians(angle)) # velocity y
        self.timer = 0
        self.ended = False

    def area(self):
        return self.radius**2*3.14

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.timer += 1
        if self.timer >= 60:                                    # вермя действия частиц
            self.ended = True

    def draw(self):
        red = (200, 0, 0)
        circleX = 100
        circleY = 100
        radius = 10
        active = True

        while active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    active = False

            pygame.draw.circle(display, red, (circleX, circleY), radius)


class Streak():
    def __init__(self, x, y):
        self.color = choose_random_color()
        self.x = x
        self.y = y
        angle = random.uniform(-60, 360)                        # угол
        velocity_mag = random.uniform(.3, 4)                    # радиус разброса
        self.vx = velocity_mag * math.cos(math.radians(angle))  # velocity x
        self.vy = -velocity_mag * math.sin(math.radians(angle)) # velocity y
        self.timer = 0
        self.ended = False

    def get_angle(self):
        return math.atan2(-self.vy, self.vx)

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.timer += 1
        if self.timer >= 60:                        # вермя действия частиц
            self.ended = True

    def draw(self):
        angle = self.get_angle()
        length = 1
        dx = length * math.cos(angle)
        dy = length * math.sin(angle)
        a = [int(self.x + dy), int(self.y - dx)]
        b = [int(self.x - dy), int(self.y + dx)]
        pygame.draw.line(display, self.color, a, b, 1)


class Firework():
    def __init__(self):
        self.x = random.randint(0, 1000)
        self.y = 600
        self.velocity = random.uniform(3.5, 7)    # скорость
        self.end_y = random.uniform(10, 300)      # высота полёта
        self.ended = False

    def move(self):
        self.y -= self.velocity
        if self.y <= self.end_y:
            self.ended = True

    def draw(self):
        a = [self.x, int(self.y + 15)]            # длина феерверка
        b = [self.x, int(self.y - 15)]
        
#        pygame.draw.line(display, (128, 128, 128), a, b, 4)
       
        color = [random.randint(0, 255) for _ in range(3)]             # +++
        pygame.draw.ellipse(display, color, [a[0], a[1], 15, 15], 2)   # +++

def game():
    fireworks = [Firework()]
    streaks = []
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        if random.uniform(0, 1) <= 1 / 60:
            fireworks.append(Firework())
        display.fill((0, 0, 0))

        for firework in fireworks:
            firework.move()
            firework.draw()
            if firework.ended:
                streaks += [Streak(firework.x, firework.y) for i in range(random.randint(20, 700))]#количество частиц
                fireworks.remove(firework)
        
        for streak in streaks:
            streak.move()
            streak.draw()
            if streak.ended:
                streaks.remove(streak)

        pygame.display.update()
        clock.tick(FPS)


game()
pygame.quit()