##inicialização
import pygame

pygame.init()


#Gera a tela
WIDTH = 720   
HEIGHT = 480
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Guitarzao')

#Assets
button_width = 64
button_height = 64

def load_assets():
    assets = {}

    #Imagens
    assets['left'] = pygame.image.load('assets/left.png').convert_alpha()
    assets['left'] = pygame.transform.scale(assets['left'], (button_width, button_height))
    assets['right'] = pygame.image.load('assets/right.png').convert_alpha()
    assets['right'] = pygame.transform.scale(assets['right'], (button_width, button_height))
    assets['up'] = pygame.image.load('assets/up.png').convert_alpha()
    assets['up'] = pygame.transform.scale(assets['up'], (button_width, button_height))
    assets['down'] = pygame.image.load('assets/down.png').convert_alpha()
    assets['down'] = pygame.transform.scale(assets['down'], (button_width, button_height))
    assets['left_space'] = pygame.image.load('assets/left_space.png').convert_alpha()
    assets['left_space'] = pygame.transform.scale(assets['left_space'], (button_width, button_height))
    assets['right_space'] = pygame.image.load('assets/right_space.png').convert_alpha()
    assets['right_space'] = pygame.transform.scale(assets['right_space'], (button_width, button_height))
    assets['up_space'] = pygame.image.load('assets/up_space.png').convert_alpha()
    assets['up_space'] = pygame.transform.scale(assets['up_space'], (button_width, button_height))
    assets['down_space'] = pygame.image.load('assets/down_space.png').convert_alpha()
    assets['down_space'] = pygame.transform.scale(assets['down_space'], (button_width, button_height))

    #Sons
    pygame.mixer.music.load('assets/musica.mp3')
    pygame.mixer.music.set_volume(0.2)

    return assets


button_x = -button_width
button_y = 240-button_height/2
button_yspeed = 3
button_xspeed = 5


game = True

clock = pygame.time.Clock()
FPS = 60

#Loop principal
assets = load_assets()
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
    window.blit(assets['left_space'], (325-button_width,button_y))
    window.blit(assets['up_space'], (360-button_width/2,button_y-button_width))
    window.blit(assets['down_space'], (360-button_width/2,button_y+button_width))
    window.blit(assets['right_space'], (370+button_width/2,button_y))
    window.blit(assets['left'], (button_x,button_y))
    #window.blit(right_img_small, (button_x,button_y))
    pygame.display.update()
pygame.quit()
