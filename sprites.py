import pygame
from config import WIDTH, HEIGHT, button_width, button_height



# definindo uma classe para cada uma das setas
class seta_left(pygame.sprite.Sprite):
    def __init__(self, assets):
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


    def update(self, assets, animation):
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
    def __init__(self, assets):
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

    def update(self, assets, animation):
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
    def __init__(self,assets):
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

    def update(self, assets, animation):
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
    def __init__(self, assets):
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

    def update(self, assets, animation):
        
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
    def __init__(self, assets):
        #construtor da classe mãe (Sprite)
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['left_space']
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2-button_width
        self.rect.centery = HEIGHT/2

class seta_up_space(pygame.sprite.Sprite):
    def __init__(self, assets):
        #construtor da classe mãe (Sprite)
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['up_space']
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.centery = HEIGHT/2-button_height

class seta_down_space(pygame.sprite.Sprite):
    def __init__(self, assets):
        #construtor da classe mãe (Sprite)
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['down_space']
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.centery = HEIGHT/2+button_height

class seta_right_space(pygame.sprite.Sprite):
    def __init__(self, assets):
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