##inicialização
import pygame

pygame.init()



WIDTH = 1280    
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Guitarzao')


button_width = 150
button_height = 120
button_img = pygame.image.load('assets/azul.png').convert_alpha()
button_img_small = pygame.transform.scale(button_img, (button_width, button_height))

firstsong = pygame.mixer.Sound('assets/musica.mp3')


button_x = 0
button_y = 300
button_yspeed = 3
button_xspeed = 3


game = True

clock = pygame.time.Clock()
FPS = 60

while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            game = False
    button_x +=button_xspeed
    if button_x >=400:
        button_x = 0
    window.fill((0, 0, 255))
    window.blit(button_img_small, (button_x,button_y))
    pygame.display.update()
pygame.quit()
