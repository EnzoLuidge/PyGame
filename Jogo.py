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
pygame.display.set_caption('Icy Rhythm Penguin Hero')

# Função que recebe o tempo da música que o a seta tem que ser apertada e devolve o tempo que a seta tem que ser criada
def Tempo(tempomusica):
    tempomusica = int(tempomusica)
    tempo = tempomusica-1585
    return tempo 

# Loop principal---------------------------------------------------------------------------------------
game = INIT

while game != QUIT:
    
    if game == INIT:
        clock = pygame.time.Clock()
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

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = QUIT
                    running = False

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
                running = False
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

            pygame.display.update()  # Mostra o novo frame para o jogador

    elif game == PLAYING: #---------------------------------------------------------------------------------
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
        if tempo_musica == -1 and dic[2300]=='já foi':
            transition.done = 0
            transition.update()
            if transition.done == 1:
                game = SCORING
                state = 1
                dic = dict()
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

    elif game == SCORING: # Dando o score
        clock.tick(FPS)
        if transition.done == 2: 
            state = 1
            transition.done = -1
        
        # Textos das telas de score
        texto1 = assets['ice_font'].render('Your', True, (0,0,255))
        texto1_rect = texto1.get_rect()
        texto1_rect.y = 170
        texto1_rect.centerx = WIDTH/2

        texto2 = assets['ice_font'].render('score was', True, (0,0,255))
        texto2_rect = texto2.get_rect()
        texto2_rect.y = 230
        texto2_rect.centerx = WIDTH/2

        texto3 = assets['ice_font'].render("Therefore", True, (0,0,255))
        texto3_rect = texto3.get_rect()
        texto3_rect.y = 170
        texto3_rect.centerx = WIDTH/2

        texto4 = assets['ice_font'].render("you got...", True, (0,0,255))
        texto4_rect = texto4.get_rect()
        texto4_rect.y = 230
        texto4_rect.centerx = WIDTH/2

        texto5 = assets['ice2_font'].render("press space", True, (0,0,255))
        texto5_rect = texto5.get_rect()
        texto5_rect.y = 500
        texto5_rect.centerx = WIDTH/2

        # calcula a nota final
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
        
        elif assets['score'] == 0:
            nota = assets['ice3_font'].render('F', True, (0,0,0))

        else:
            nota = assets['ice3_font'].render('D', True, (0,0,0))
        nota_rect = nota.get_rect()
        nota_rect.y = 180
        nota_rect.centerx = WIDTH/2
        while state == 1: # "Your score was [score]"
            window.blit(assets['telafinal'], (0,0))

            text_surface = assets['ice_font'].render("{:05d}".format(assets['score']), True, (0,0,255))
            text_rect = text_surface.get_rect()

            text_rect.midtop = (300, 350)
            window.blit(text_surface, text_rect)
            window.blit(texto1, texto1_rect)
            window.blit(texto2, texto2_rect)

            window.blit(texto5, texto5_rect) 
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = QUIT
                    state = False
                if event.type == pygame.KEYDOWN:
                    keys_down[event.key] = True
                    if event.key == pygame.K_SPACE:
                        transition.done = 0
                        state = 2##gameover2
                        window.blit(assets['telafinal'],(0,0))   
            pygame.display.update()

        while state == 2: #"Therefore you got..."
            
            window.blit(texto3,texto3_rect)
            window.blit(texto4,texto4_rect)
            window.blit(texto5,texto5_rect)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = QUIT
                    state = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        state = 3
                        window.blit(assets['telafinal'],(0,0))
            pygame.display.update()

            

        while state == 3: # mostra a nota final
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = QUIT
                    state = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game = INIT
                        state = False

            if nota == 'S+':
                window.blit(texto5,texto5_rect)
                window.blit(nota,nota_rect)
            else:
                window.blit(texto5,texto5_rect)
                window.blit(nota,nota_rect)
            pygame.display.update()
                    
    pygame.display.update()
pygame.quit() 
