##inicialização
import pygame

pygame.init()


#Gera a tela
WIDTH = 600   
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Guitarzao')

#Assets
button_width = 64
button_height = 64
button_x = -button_width
button_y = 240-button_height/2

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

##definindo uma classe para cada uma das setas
class seta_left(pygame.sprite.Sprite):
    def __init__(self):
        self.image = assets['left']
        self.rect = self.image.get_rect()
        self.rect.x = -button_width
        self.rect.centery = HEIGHT/2
        self.speedx = 3
        self.speedy = 3

    def update(self):
        # Atualizando a posição da seta
        self.rect.x += self.speedx
        if self.rect.centerx >= WIDTH/2-button_width:
            self.rect.x = -button_width

class seta_up(pygame.sprite.Sprite):
    def __init__(self):
        self.image = assets['up']
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.y = -button_height
        self.speedx = 3
        self.speedy = 3

    def update(self):
        # Atualizando a posição da seta
        self.rect.y += self.speedy
        if self.rect.centery >= HEIGHT/2-button_height:
            self.rect.y = -button_width

class seta_right(pygame.sprite.Sprite):
    def __init__(self):
        self.image = assets['right']
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.centery = WIDTH/2
        self.speedx = 3
        self.speedy = 3

    def update(self):
        # Atualizando a posição da seta
        self.rect.x -= self.speedx
        if self.rect.centerx <= WIDTH/2+button_width:
            self.rect.x = WIDTH

class seta_down(pygame.sprite.Sprite):
    def __init__(self):
        self.image = assets['down']
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.y = HEIGHT
        self.speedx = 3
        self.speedy = 3

    def update(self):
        # Atualizando a posição da seta
        self.rect.y -= self.speedy
        if self.rect.centery <= HEIGHT/2+button_height:
            self.rect.y = HEIGHT

class seta_left_space(pygame.sprite.Sprite):
    def __init__(self):
        self.image = assets['left_space']
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2-button_width
        self.rect.centery = HEIGHT/2

class seta_up_space(pygame.sprite.Sprite):
    def __init__(self):
        self.image = assets['up_space']
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.centery = HEIGHT/2-button_height

class seta_down_space(pygame.sprite.Sprite):
    def __init__(self):
        self.image = assets['down_space']
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.centery = HEIGHT/2+button_height

class seta_right_space(pygame.sprite.Sprite):
    def __init__(self):
        self.image = assets['right_space']
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2+button_width
        self.rect.centery = HEIGHT/2

game = True

clock = pygame.time.Clock()
FPS = 60

#Loop principal
assets = load_assets()
pygame.mixer.music.play(loops=-1)

##puxando as classes de seta
setaleft = seta_left()
setadown = seta_down()
setaright = seta_right()
setaup = seta_up()
setaleftspace = seta_left_space()
setaupspace = seta_up_space()
setarightspace = seta_right_space()
setadownspace = seta_down_space()


while game:

    tempo_musica = pygame.mixer.music.get_pos()


    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    ##dando update nas classes de seta
    setaleft.update()
    setaup.update()
    setaright.update()
    setadown.update()

    window.fill((0, 0, 255))

    ##mostrando a imagem das setas
    window.blit(setaleft.image, setaleft.rect)
    window.blit(setaup.image,setaup.rect)
    window.blit(setaright.image,setaright.rect)
    window.blit(setadown.image,setadown.rect)

    ##mostrando a imagem das setas vazias
    window.blit(setaleftspace.image, setaleftspace.rect)
    window.blit(setaupspace.image,setaupspace.rect)
    window.blit(setadownspace.image,setadownspace.rect)
    window.blit(setarightspace.image, setarightspace.rect)
    
    

    #window.blit(right_img_small, (button_x,button_y))
    pygame.display.update()
pygame.quit()
