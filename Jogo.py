##inicialização
import pygame
from música import dict, dic
from config import WIDTH, HEIGHT, FPS
from assets import load_assets
from sprites import seta_left, seta_down, seta_up, seta_right, seta_down_space, seta_left_space, seta_right_space, seta_up_space, Idle, Miss, Up, Down, Left, Right

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

keys_down = {}
animation = Idle(assets)
animations.add(animation)




# Loop principal---------------------------------------------------------------------------------------
game = True
clock = pygame.time.Clock()

while game:
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

            if event.key == pygame.K_SPACE:
                pygame.mixer.music.play()
                dic = dict()
                assets['score']=0
        
                    
    
    ##dando update nas classes de seta
    all_sprites.update(assets, animation)
    animations.update()

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
    animations.draw(window)

    
    pygame.display.update()
pygame.quit()
