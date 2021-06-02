##inicialização
import pygame
from música import * 

pygame.init()


#Gera a tela
WIDTH = 600   
HEIGHT = 600
CENTER = WIDTH/2
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Guitarzao')

#Assets
button_width = 64
button_height = 64
button_x = -button_width
button_y = 240-button_height/2

# Função que recebe o tempo da música que o a seta tem que ser apertada e devolve o tempo que a seta tem que ser criada
def Tempo(tempomusica):
    tempomusica = int(tempomusica)
    tempo = tempomusica-1585
    return tempo

def load_assets():
    assets = {}

    #Imagens
    assets['left'] = pygame.image.load('assets/img/left.png').convert_alpha()
    assets['left'] = pygame.transform.scale(assets['left'], (button_width, button_height))
    assets['right'] = pygame.image.load('assets/img/right.png').convert_alpha()
    assets['right'] = pygame.transform.scale(assets['right'], (button_width, button_height))
    assets['up'] = pygame.image.load('assets/img/up.png').convert_alpha()
    assets['up'] = pygame.transform.scale(assets['up'], (button_width, button_height))
    assets['down'] = pygame.image.load('assets/img/down.png').convert_alpha()
    assets['down'] = pygame.transform.scale(assets['down'], (button_width, button_height))
    assets['left_space'] = pygame.image.load('assets/img/left_space.png').convert_alpha()
    assets['left_space'] = pygame.transform.scale(assets['left_space'], (button_width, button_height))
    assets['right_space'] = pygame.image.load('assets/img/right_space.png').convert_alpha()
    assets['right_space'] = pygame.transform.scale(assets['right_space'], (button_width, button_height))
    assets['up_space'] = pygame.image.load('assets/img/up_space.png').convert_alpha()
    assets['up_space'] = pygame.transform.scale(assets['up_space'], (button_width, button_height))
    assets['down_space'] = pygame.image.load('assets/img/down_space.png').convert_alpha()
    assets['down_space'] = pygame.transform.scale(assets['down_space'], (button_width, button_height))
    assets['icy_night'] = pygame.image.load('assets/img/icy_night.png').convert_alpha()
    assets['icy_night'] = pygame.transform.scale(assets['icy_night'], (WIDTH, HEIGHT))
    
    
    # sistema de placar
    assets["score_font"] = pygame.font.Font('assets/font/PressStart2P.ttf', 28)
    assets['score'] = 0

    # Sons serelepes
    pygame.mixer.music.load('assets/snd/musica.mp3')
    pygame.mixer.music.set_volume(0.2)
    assets['boom'] = pygame.mixer.Sound('assets/snd/boom.wav')
    assets['hihat'] = pygame.mixer.Sound('assets/snd/hihat.wav')
    assets['button'] = pygame.mixer.Sound('assets/snd/button.wav')

    # Animações
    idle_anim = [] # animação de repouso
    for i in range(2):
        # Os arquivos de animação são numerados de 00 a 01
        filename = 'assets/anim/idle0{}.png'.format(i)
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (128, 128))
        idle_anim.append(img)
    assets["idle_anim"] = idle_anim

    right_anim = [] # animação do penguin para direita
    for i in range(5):
        # Os arquivos de animação são numerados de 00 a 04
        filename = 'assets/anim/right0{}.png'.format(i)
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (128, 128))
        right_anim.append(img)
    assets["right_anim"] = right_anim

    left_anim = [] # animação do penguin para esquerda
    for i in range(5):
        # Os arquivos de animação são numerados de 00 a 04
        filename = 'assets/anim/left0{}.png'.format(i)
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (128, 128))
        left_anim.append(img)
    assets["left_anim"] = left_anim
    
    up_anim = [] # animação do penguin para cima
    for i in range(5):
        # Os arquivos de animação são numerados de 00 a 04
        filename = 'assets/anim/up0{}.png'.format(i)
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (128, 128))
        up_anim.append(img)
    assets["up_anim"] = up_anim

    down_anim = [] # animação do penguin para baixo
    for i in range(5):
        # Os arquivos de animação são numerados de 00 a 04
        filename = 'assets/anim/down0{}.png'.format(i)
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (128, 128))
        down_anim.append(img)
    assets["down_anim"] = down_anim

    miss_anim = [] # animação do penguin para um erro
    for i in range(5):
        # Os arquivos de animação são numerados de 00 a 04
        filename = 'assets/anim/miss0{}.png'.format(i)
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (128, 128))
        miss_anim.append(img)
    assets["miss_anim"] = miss_anim

    return assets

assets = load_assets()

# definindo uma classe para cada uma das setas
class seta_left(pygame.sprite.Sprite):
    def __init__(self):
        #variável que vai ser usada para checar o tempo
        self.last = 0
        # Pega o tempo de agora
        self.now = pygame.time.get_ticks()
        self.state = False

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

        # chegando perto, já é apertável
        if self.rect.centerx >= WIDTH/2-1.12*button_width:
            self.state = True
        
        # no momento, a seta para
        if self.rect.centerx >= WIDTH/2-1.02*button_width:
            
            self.speedx = 0
            self.last = pygame.time.get_ticks()

            # Se a diferença de tempo for maior que 1600 ticks, perdeu.
            if self.last-self.now > 1600:
                self.state = False
                self.kill()
                assets['boom'].play()
                assets['score'] -= 100
                animation.frame = -2

class seta_up(pygame.sprite.Sprite):
    def __init__(self):
        #variável que vai ser usada para checar o tempo
        self.last = 0
        # Pega o tempo de agora
        self.now = pygame.time.get_ticks()
        self.state = False

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

        # chegando perto, já é apertável
        if self.rect.centery >= HEIGHT/2-1.12*button_height:
            self.state = True

        # no momento, a seta para
        if self.rect.centery >= HEIGHT/2-1.02*button_height:
            self.speedy = 0
            self.last = pygame.time.get_ticks()

            # Se a diferença de tempo for maior que 1600 ticks, perdeu.
            if self.last-self.now > 1600:
                self.state = False
                self.kill()
                assets['boom'].play()
                assets['score'] -= 100
                animation.frame = -2

class seta_right(pygame.sprite.Sprite):
    def __init__(self):
        #variável que vai ser usada para checar o tempo
        self.last = 0
        # Pega o tempo de agora
        self.now = pygame.time.get_ticks()
        self.state = False

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

        # chegando perto, já é apertável
        if self.rect.centerx <= WIDTH/2+1.12*button_width:
            self.state = True

        # no momento, a seta para
        if self.rect.centerx <= WIDTH/2+1.02*button_width:
            self.speedx = 0
            self.last = pygame.time.get_ticks()

            # Se a diferença de tempo for maior que 1600 ticks, perdeu.
            if self.last-self.now > 1600:
                self.state = False
                self.kill()
                assets['boom'].play()
                assets['score'] -= 100
                animation.frame = -2

class seta_down(pygame.sprite.Sprite):
    def __init__(self):
        #variável que vai ser usada para checar o tempo
        self.last = 0
        # Pega o tempo de agora
        self.now = pygame.time.get_ticks()
        self.state = False

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

        # chegando perto, já é apertável
        if self.rect.centery <= HEIGHT/2+1.12*button_height:
            self.state = True

        # no momento, a seta para
        if self.rect.centery <= HEIGHT/2+1.02*button_height:
            self.speedy = 0
            self.last = pygame.time.get_ticks()

            # Se a diferença de tempo for maior que 1600 ticks, perdeu.
            if self.last-self.now > 1600:
                self.state = False
                self.kill()
                assets['boom'].play()
                assets['score'] -= 100
                animation.frame = -2
  
# Classe dos espaços de setas
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

# Classe da animação idle
class Idle(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Armazena a animação de idle
        self.idle_anim = assets['idle_anim']

        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.idle_anim[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        self.rect.centery = HEIGHT/2  # Posiciona o centro da imagem
        self.rect.centerx = WIDTH/2

        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
        # próxima imagem da animação será mostrada
        self.frame_ticks = 450

    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            if self.frame == 0:
                self.frame = 1
            else:
                self.frame = 0

            center = self.rect.center
            self.image = self.idle_anim[self.frame]
            self.rect = self.image.get_rect()
            self.rect.center = center

# Classe da animação do penguin para a direita
class Right(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Armazena a animação de idle
        self.right_anim = assets['right_anim']

        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.right_anim[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        self.rect.centery = HEIGHT/2  # Posiciona o centro da imagem
        self.rect.centerx = WIDTH/2

        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
        # próxima imagem da animação será mostrada
        self.frame_ticks = 80

    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Verifica se já chegou no final da animação.
            if self.frame == len(self.right_anim):
                # Se sim, deixa o frame como -1 para poder chamar a animação idle em seguida
                self.frame = -1
            
            else:
                # Se ainda não chegou ao fim da animação, troca de imagem.
                center = self.rect.center
                self.image = self.right_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

# Classe da animação para a esquerda do penguim
class Left(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Armazena a animação de idle
        self.left_anim = assets['left_anim']

        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.left_anim[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        self.rect.centery = HEIGHT/2  # Posiciona o centro da imagem
        self.rect.centerx = WIDTH/2

        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
        # próxima imagem da animação será mostrada
        self.frame_ticks = 80

    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Verifica se já chegou no final da animação.
            if self.frame == len(self.left_anim):
                # Se sim, deixa o frame como -1 para poder chamar a animação idle em seguida
                self.frame = -1
            
            else:
                # Se ainda não chegou ao fim da animação, troca de imagem.
                center = self.rect.center
                self.image = self.left_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

# Classe da animação do penguin para cima
class Up(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Armazena a animação de idle
        self.up_anim = assets['up_anim']

        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.up_anim[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        self.rect.centery = HEIGHT/2  # Posiciona o centro da imagem
        self.rect.centerx = WIDTH/2

        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
        # próxima imagem da animação será mostrada
        self.frame_ticks = 80

    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Verifica se já chegou no final da animação.
            if self.frame == len(self.up_anim):
                # Se sim, deixa o frame como -1 para poder chamar a animação idle em seguida
                self.frame = -1
            
            else:
                # Se ainda não chegou ao fim da animação, troca de imagem.
                center = self.rect.center
                self.image = self.up_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

# Classe da animação do penguin para baixo
class Down(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Armazena a animação de idle
        self.down_anim = assets['down_anim']

        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.down_anim[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        self.rect.centery = HEIGHT/2  # Posiciona o centro da imagem
        self.rect.centerx = WIDTH/2

        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
        # próxima imagem da animação será mostrada
        self.frame_ticks = 80

    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Verifica se já chegou no final da animação.
            if self.frame == len(self.down_anim):
                # Se sim, deixa o frame como -1 para poder chamar a animação idle em seguida
                self.frame = -1
            
            else:
                # Se ainda não chegou ao fim da animação, troca de imagem.
                center = self.rect.center
                self.image = self.down_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

# Classe da animação do penguin para um erro
class Miss(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Armazena a animação de idle
        self.miss_anim = assets['miss_anim']

        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.miss_anim[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        self.rect.centery = HEIGHT/2  # Posiciona o centro da imagem
        self.rect.centerx = WIDTH/2

        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
        # próxima imagem da animação será mostrada
        self.frame_ticks = 80

    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Verifica se já chegou no final da animação.
            if self.frame == len(self.miss_anim):
                # Se sim, deixa o frame como -1 para poder chamar a animação idle em seguida
                self.frame = -1
            
            else:
                # Se ainda não chegou ao fim da animação, troca de imagem.
                center = self.rect.center
                self.image = self.miss_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

##puxando as classes de espaços das setas
setaleftspace = seta_left_space()
setaupspace = seta_up_space()
setarightspace = seta_right_space()
setadownspace = seta_down_space()

##criando um grupo de setas e armazenando todas em um grupo de grupo de setas
lefts = pygame.sprite.Group()
rights = pygame.sprite.Group()
ups = pygame.sprite.Group()
downs = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()

keys_down = {}
animation = Idle(assets)
all_sprites.add(animation)




# Loop principal---------------------------------------------------------------------------------------
assets = load_assets()
game = True
clock = pygame.time.Clock()
FPS = 60

while game:
    # Se tiver um erro, toca a animação de erro
    if animation.frame == -2:
        animation.kill()
        animation = Miss(assets)
        all_sprites.add(animation)

    # Se a animação acabar, volta para a de idle
    elif animation.frame == -1:
        animation.kill()
        animation = Idle(assets)
        all_sprites.add(animation)

    # Pega o tempo da música
    tempo_musica = pygame.mixer.music.get_pos()

    # Para cada nota no dicionário de notas
    for letra in dic:
        tempo = Tempo(letra)
        # Se chegar a hora, faz a seta
        if tempo_musica >= tempo:
            if dic[letra] == 'left':
                setaleft = seta_left()
                all_sprites.add(setaleft)
                lefts.add(setaleft)
            
            elif dic[letra] == 'right':
                setaright = seta_right()
                all_sprites.add(setaright)
                rights.add(setaright)

            elif dic[letra] == 'up':
                setaup = seta_up()
                all_sprites.add(setaup)
                ups.add(setaup)

            elif dic[letra] == 'down': 
                setadown = seta_down()
                all_sprites.add(setadown) 
                downs.add(setadown)

            # Previne de criar notas repetidas
            dic[letra] = 'já foi'
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            keys_down[event.key] = True
            if event.key == pygame.K_LEFT:

                #iteração (gambiarra do pygame para verificar cada seta)
                lefts_iter = iter(lefts)
                seta_valida = False #variável para checar se alguma seta é válida (no caso de múltiplas setas do mesmo tipo)
                for i in range(len(lefts)):
                    left = next(lefts_iter)
 
                    if left.state == True:
                        assets['score']+=100
                        left.state = False
                        left.kill()
                        assets['hihat'].play()
                        animation.kill()
                        animation = Left(assets)
                        all_sprites.add(animation)
                        seta_valida = True
                    
                    #código que penaliza ficar spammando o botão
                    elif seta_valida == False:
                        assets['score']-=10
                        assets['button'].play()

                        
            if event.key == pygame.K_RIGHT:

                #iteração (gambiarra do pygame para verificar cada seta)
                rights_iter = iter(rights)
                seta_valida = False #variável para checar se alguma seta é válida (no caso de múltiplas setas do mesmo tipo)
                for i in range(len(rights)):
                    right = next(rights_iter)

                    if right.state == True:
                        assets['score']+=100
                        right.state = False
                        right.kill()
                        assets['hihat'].play()
                        animation.kill()
                        animation = Right(assets)
                        all_sprites.add(animation)
                        seta_valida = True
                    
                    #código que penaliza ficar spammando o botão
                    elif seta_valida == False:
                        assets['score']-=10
                        assets['button'].play()

            if event.key == pygame.K_UP:

                #iteração (gambiarra do pygame para verificar cada seta)
                ups_iter = iter(ups)
                seta_valida = False #variável para checar se alguma seta é válida (no caso de múltiplas setas do mesmo tipo)
                for i in range(len(ups)):
                    up = next(ups_iter)

                    if up.state == True:
                        assets['score']+=100
                        up.state = False
                        up.kill()
                        assets['hihat'].play()
                        animation.kill()
                        animation = Up(assets)
                        all_sprites.add(animation)
                        seta_valida = True
                    
                    #código que penaliza ficar spammando o botão
                    elif seta_valida == False:
                        assets['score']-=10
                        assets['button'].play()

            if event.key == pygame.K_DOWN:

                #iteração (gambiarra do pygame para verificar cada seta)
                downs_iter = iter(downs)
                seta_valida = False #variável para checar se alguma seta é válida (no caso de múltiplas setas do mesmo tipo)
                for i in range(len(downs)):
                    down = next(downs_iter)

                    if down.state == True:
                        assets['score']+=100
                        down.state = False
                        down.kill()
                        assets['hihat'].play()
                        animation.kill()
                        animation = Down(assets)
                        all_sprites.add(animation)
                        seta_valida = True
                    
                    #código que penaliza ficar spammando o botão
                    elif seta_valida == False:
                        assets['score']-=10
                        assets['button'].play()

            if event.key == pygame.K_SPACE:
                pygame.mixer.music.play()
                dic = dict()
                assets['score']=0
        
                    
    
    ##dando update nas classes de seta
    all_sprites.update()

    window.fill((0, 0, 255))
    window.blit(assets['icy_night'], (0, 0))

    ##mostrando a imagem das setas vazias
    window.blit(setaleftspace.image, setaleftspace.rect)
    window.blit(setaupspace.image,setaupspace.rect)
    window.blit(setadownspace.image,setadownspace.rect)
    window.blit(setarightspace.image, setarightspace.rect)
    
    # Previne o score de ser negativo
    if assets['score']<0:
        assets['score']=0

    text_surface = assets['score_font'].render("{:08d}".format(assets['score']), True, (255, 255, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (WIDTH / 2,  10)
    window.blit(text_surface, text_rect)

    ##mostrando a imagem das setas
    all_sprites.draw(window)

    #window.blit(right_img_small, (button_x,button_y))
    pygame.display.update()
pygame.quit()
