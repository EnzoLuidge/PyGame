##inicialização
import pygame

pygame.init()



WIDTH = 480
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Guitarzao')


button_width = 50
button_height = 38
button_img = pygame.image.load('assets/azul.png').convert_alpha()
button_img_small = pygame.transform.scale(button_img, (button_width, button_height))

button_x = 10
button_y = 0
button_yspeed = 3

game = True

clock = pygame.time.Clock()
FPS = 60

while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            game = False

    button_y +=button_yspeed

    window.fill((0, 0, 255))
    window.blit(button_img_small, (button_x,button_y))
    pygame.display.update()
pygame.quit()
