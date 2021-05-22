##inicialização
import pygame

pygame.init()


#Gera a tela
WIDTH = 720   
HEIGHT = 480
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Guitarzao')

#Imagens Botão
button_width = 65
button_height = 52
button_img = pygame.image.load('assets/azul.png').convert_alpha()
button_img_small = pygame.transform.scale(button_img, (button_width, button_height))


button_x = -button_width
button_y = 240
button_yspeed = 3
button_xspeed = 5

#MSons
firstsong = pygame.mixer.Sound('assets/musica.mp3')
pygame.mixer.music.load('assets/musica.mp3')
pygame.mixer.music.set_volume(0.2)

game = True

clock = pygame.time.Clock()
FPS = 60

#Loop principal
pygame.mixer.music.play(loops=-1)
while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            game = False
    button_x +=button_xspeed
    if button_x >=360-button_width:
        button_x = -button_width
    window.fill((0, 0, 255))
    window.blit(button_img_small, (button_x,button_y))
    pygame.display.update()
pygame.quit()
