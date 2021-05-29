##inicialização
import pygame
from pygame.constants import K_LEFT

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
    
    ##sistema de placar
    assets["score_font"] = pygame.font.Font('assets/font/PressStart2P.ttf', 28)
    assets['score'] = 0

    # Sons serelepes
    pygame.mixer.music.load('assets/musica.mp3')
    pygame.mixer.music.set_volume(0.2)
    assets['boom'] = pygame.mixer.Sound('assets/boom.wav')
    assets['hihat'] = pygame.mixer.Sound('assets/hihat.wav')

    return assets

assets = load_assets()

##definindo uma classe para cada uma das setas
class seta_left(pygame.sprite.Sprite):
    def __init__(self):
        #variável que vai ser usada para checar o tempo
        self.last = 0
        # Pega o tempo de agora
        self.now = pygame.time.get_ticks()
        self.state = 0

        #construtor da classe mãe (Sprite)
        pygame.sprite.Sprite.__init__(self)
        self.assets = assets
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
            
            self.speedx = 0
            self.last = pygame.time.get_ticks()
            # Se a diferença de tempo for menor que 1600 ticks, é válido.
            
            if self.last-self.now < 1600:
                self.state = True
              
            else:
                self.state = False
                self.kill()
                assets['boom'].play()

class seta_up(pygame.sprite.Sprite):
    def __init__(self):
        #variável que vai ser usada para checar o tempo
        self.last = 0
        # Pega o tempo de agora
        self.now = pygame.time.get_ticks()
        #construtor da classe mãe (Sprite)
        pygame.sprite.Sprite.__init__(self)

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
            self.speedy = 0
            self.last = pygame.time.get_ticks()
            # Se a diferença de tempo for menor que 1600 ticks, é válido.
            
            if self.last-self.now < 1600:
                self.state = True
    
            else:
                self.state = False
                self.kill()
                assets['boom'].play()

class seta_right(pygame.sprite.Sprite):
    def __init__(self):
        #variável que vai ser usada para checar o tempo
        self.last = 0
        # Pega o tempo de agora
        self.now = pygame.time.get_ticks()
        #construtor da classe mãe (Sprite)
        pygame.sprite.Sprite.__init__(self)

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
            self.speedx = 0
            self.last = pygame.time.get_ticks()
            # Se a diferença de tempo for menor que 1600 ticks, é válido.
            
            if self.last-self.now < 1600:
                self.state = True
      
            else:
                self.state = False
                self.kill()
                assets['boom'].play()

class seta_down(pygame.sprite.Sprite):
    def __init__(self):
        #variável que vai ser usada para checar o tempo
        self.last = 0
        # Pega o tempo de agora
        self.now = pygame.time.get_ticks()
        #construtor da classe mãe (Sprite)
        pygame.sprite.Sprite.__init__(self)

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
            self.speedy = 0
            self.last = pygame.time.get_ticks()
            # Se a diferença de tempo for menor que 1600 ticks, é válido.
            
            if self.last-self.now < 1600:
                self.state = True
         
            else:
                self.state = False
                self.kill()
                assets['boom'].play()
  

class seta_left_space(pygame.sprite.Sprite):
    def __init__(self):
        #construtor da classe mãe (Sprite)
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['left_space']
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2-button_width
        self.rect.centery = HEIGHT/2

class seta_up_space(pygame.sprite.Sprite):
    def __init__(self):
        #construtor da classe mãe (Sprite)
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['up_space']
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.centery = HEIGHT/2-button_height

class seta_down_space(pygame.sprite.Sprite):
    def __init__(self):
        #construtor da classe mãe (Sprite)
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['down_space']
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.centery = HEIGHT/2+button_height

class seta_right_space(pygame.sprite.Sprite):
    def __init__(self):
        #construtor da classe mãe (Sprite)
        pygame.sprite.Sprite.__init__(self)
        

        self.image = assets['right_space']
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2+button_width
        self.rect.centery = HEIGHT/2

game = True

clock = pygame.time.Clock()
FPS = 60

##definindo um grupo para todas as setas


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

##criando um grupo de setas e armazenando todas as setas nele
all_setas = pygame.sprite.Group()
all_setas.add(setaleft)
all_setas.add(setaright)
all_setas.add(setaup)
all_setas.add(setadown)

keys_down = {}

while game:

    tempo_musica = pygame.mixer.music.get_pos()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            keys_down[event.key] = True
            if event.key == pygame.K_LEFT:
                if setaleft.state == True:
                    assets['score']+=100
                    setaleft.state = 0
                    setaleft.kill()
                    assets['hihat'].play()
                    setaleft = seta_left()
                    all_setas.add(setaleft)
            if event.key == pygame.K_RIGHT:
                assets['hihat'].play()
            if event.key == pygame.K_UP:
                assets['hihat'].play()
            if event.key == pygame.K_DOWN:
                assets['hihat'].play()
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key in keys_down and keys_down[event.key]:
                if event.key == pygame.K_LEFT:
                    print('soltou')
                if event.key == pygame.K_RIGHT:
                    print('soltou')
    
    ##dando update nas classes de seta
    all_setas.update()

    window.fill((0, 0, 255))

    ##mostrando a imagem das setas vazias
    window.blit(setaleftspace.image, setaleftspace.rect)
    window.blit(setaupspace.image,setaupspace.rect)
    window.blit(setadownspace.image,setadownspace.rect)
    window.blit(setarightspace.image, setarightspace.rect)
    
    text_surface = assets['score_font'].render("{:08d}".format(assets['score']), True, (255, 255, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (WIDTH / 2,  10)
    window.blit(text_surface, text_rect)

    ##mostrando a imagem das setas
    all_setas.draw(window)

    #window.blit(right_img_small, (button_x,button_y))
    pygame.display.update()
pygame.quit()
