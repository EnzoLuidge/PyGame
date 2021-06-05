##inicialização
import pygame
import os
from música import dict, dic
from config import WIDTH, HEIGHT, FPS, QUIT, INIT, PLAYING, SCORING, SND_DIR
from assets import load_assets
from sprites import PressSpace, seta_left, seta_down, seta_up, seta_right, seta_down_space, seta_left_space, seta_right_space, seta_up_space, Idle, Big_Idle, Miss, Up, Down, Left, Right, Transition

# Começa 
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Guitarzao')

# Função que recebe o tempo da música que o a seta tem que ser apertada e devolve o tempo que a seta tem que ser criada
def Tempo(tempomusica):
    tempomusica = int(tempomusica)
    tempo = tempomusica-1585
    return tempo 

# Carrega os assets
assets = load_assets()

##puxando as classes de espaços das setas
setaleftspace = seta_left_space(assets)
setaupspace = seta_up_space(assets)
setarightspace = seta_right_space(assets)
setadownspace = seta_down_space(assets)

##criando um grupo de setas e armazenando todas e um de todos os sprites
lefts = pygame.sprite.Group()
rights = pygame.sprite.Group()
ups = pygame.sprite.Group()
downs = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()
animations = pygame.sprite.Group()
transitions = pygame.sprite.Group()

keys_down = {}
animation = Big_Idle(assets)
animations.add(animation)
transition = Transition(assets)
transitions.add(transition)
press_space = PressSpace(assets)
animations.add(press_space)

# Música da intro
pygame.mixer.music.play(-1)

# Loop principal---------------------------------------------------------------------------------------
game = INIT
clock = pygame.time.Clock()

while game != QUIT:

    if game == INIT:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = QUIT

            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True

                if event.key == pygame.K_SPACE:
                    if transition.done == -1:
                        transition.done = 0
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load(os.path.join(SND_DIR, 'musica.mp3'))
                        pygame.mixer.music.set_volume(0.2)
                        assets['transition_sound'].play()
                    
        if transition.done == 1:
            game = PLAYING
            animation.kill()
            press_space.kill()
            animation = Idle(assets)
            animations.add(animation)
        
        clock.tick(FPS)
        ##dando update nas classes
        all_sprites.update(assets, animation)
        animations.update()
        transitions.update()

        window.fill((0, 0, 255))
        window.blit(assets['icy_show'], (0, 0))
        window.blit(assets['title'], (WIDTH/5+10, -60))

        ##mostrando a imagem das setas
        all_sprites.draw(window)
        animations.draw(window)
        transitions.draw(window)

    elif game == PLAYING:
        # TRANSIÇÃO
        # Se a transição acabou, começa a música
        if transition.done == 2:
            transition.done = -1
            pygame.mixer.music.play()
            dic = dict()
            assets['score']=0
            
        
        # JOGO
        # Se tiver um erro, toca a animação de erro
        if animation.frame == -2:
            animation.kill()
            animation = Miss(assets)
            animations.add(animation)

        # Se a animação acabar, volta para a de idle
        elif animation.frame == -1:
            animation.kill()
            animation = Idle(assets)
            animations.add(animation)
            

        # Pega o tempo da música
        tempo_musica = pygame.mixer.music.get_pos()

        # Para cada nota no dicionário de notas
        for letra in dic:
            tempo = Tempo(letra)
            # Se chegar a hora, faz a seta
            if tempo_musica >= tempo:
                if dic[letra] == 'left':
                    setaleft = seta_left(assets)
                    all_sprites.add(setaleft)
                    lefts.add(setaleft)
                
                elif dic[letra] == 'right':
                    setaright = seta_right(assets)
                    all_sprites.add(setaright)
                    rights.add(setaright)

                elif dic[letra] == 'up':
                    setaup = seta_up(assets)
                    all_sprites.add(setaup)
                    ups.add(setaup)

                elif dic[letra] == 'down': 
                    setadown = seta_down(assets)
                    all_sprites.add(setadown) 
                    downs.add(setadown)

                # Previne de criar notas repetidas
                dic[letra] = 'já foi'
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = QUIT

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
                            animations.add(animation)
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
                            animations.add(animation)
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
                            animations.add(animation)
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
                            animations.add(animation)
                            seta_valida = True
                        
                        #código que penaliza ficar spammando o botão
                        elif seta_valida == False:
                            assets['score']-=10
                            assets['button'].play()
        ##quando a música acabar
        if tempo_musica == -1:
            transition.done = 0
            transition.update()
            if transition.done == 2:
                game = 4
                ##gameover                                
        
        ##dando update nas classes de seta
        all_sprites.update(assets, animation)
        animations.update()
        transitions.update()

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

        text_surface = assets['score_font'].render("{:05d}".format(assets['score']), True, (255, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)

        ##mostrando a imagem das setas
        all_sprites.draw(window)
        animations.draw(window)
        transitions.draw(window)

    elif game == 4:#gameover
        if transition.done == 2:
            transition.done = -1

        window.blit(assets['telafinal'], (0,0))

        texto = assets['ice_font'].render('Seu score', True, (0,0,255))
        texto2 = assets['ice_font'].render('foi de', True, (0,0,255))
        texto3 = assets['ice_font'] .render("Logo a sua", True, (0,0,255))
        texto4 = assets['ice_font'].render("nota foi...", True, (0,0,255))
        texto5 = assets['ice2_font'].render("pressione espaco", True, (0,0,255))
        if assets['score'] == 17900:
            nota = assets['ice3_font'].render('S+', True, (153,204,50))

        elif assets['score'] >= 15000 and assets['score'] <= 17900:
            nota = assets['ice3_font'].render('S', True, (255,255,0))

        elif assets['score'] >= 12000 and assets['score'] <= 14999:
            nota = assets['ice3_font'].render('A', True, (0,255,0))
        
        elif assets['score'] >= 9000 and assets['score'] <= 11999:
            nota = assets['ice3_font'].render('B', True, (0,0,255))
        
        elif assets['score'] >= 5000 and assets['score'] <= 9000:
            nota = assets['ice3_font'].render('C', True, (255,0,0))
        
        else:
            nota = assets['ice3_font'].render('D', True, (0,0,0))

        text_surface = assets['ice_font'].render("{:05d}".format(assets['score']), True, (0,0,255))
        text_rect = text_surface.get_rect()
 

        text_rect.midtop = (300, 350)
        window.blit(text_surface, text_rect)
        window.blit(texto, (50,170))
        window.blit(texto2, (140,230))

        window.blit(texto5,(130,500)) 
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = QUIT
            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True
                if event.key == pygame.K_SPACE:
                    game = 5##gameover2
                    window.blit(assets['telafinal'],(0,0))

                    
    elif game == 5:
        if event.type == pygame.QUIT:
            game = QUIT
        window.blit(texto3,(30,170))
        window.blit(texto4,(60,230))
        window.blit(texto5,(130,500))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game = 6
                    window.blit(assets['telafinal'],(0,0))

    
    elif game == 6:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game = INIT
        if nota == 'S+':
            window.blit(texto5,(130,500))
            window.blit(nota,(120,180))
        else:
            window.blit(texto5,(130,500))
            window.blit(nota,(210,180))
        pygame.display.update()
                    
    pygame.display.update()
pygame.quit() 
