import pygame
import os
from config import IMG_DIR, SND_DIR, FNT_DIR, ANIM_DIR, WIDTH, HEIGHT, button_width, button_height

def load_assets():
    assets = {}

    #Imagens
    assets['left'] = pygame.image.load(os.path.join(IMG_DIR, 'left.png')).convert_alpha()
    assets['left'] = pygame.transform.scale(assets['left'], (button_width, button_height))
    assets['right'] = pygame.image.load(os.path.join(IMG_DIR, 'right.png')).convert_alpha()
    assets['right'] = pygame.transform.scale(assets['right'], (button_width, button_height))
    assets['up'] = pygame.image.load(os.path.join(IMG_DIR, 'up.png')).convert_alpha()
    assets['up'] = pygame.transform.scale(assets['up'], (button_width, button_height))
    assets['down'] = pygame.image.load(os.path.join(IMG_DIR, 'down.png')).convert_alpha()
    assets['down'] = pygame.transform.scale(assets['down'], (button_width, button_height))
    assets['left_space'] = pygame.image.load(os.path.join(IMG_DIR, 'left_space.png')).convert_alpha()
    assets['left_space'] = pygame.transform.scale(assets['left_space'], (button_width, button_height))
    assets['right_space'] = pygame.image.load(os.path.join(IMG_DIR, 'right_space.png')).convert_alpha()
    assets['right_space'] = pygame.transform.scale(assets['right_space'], (button_width, button_height))
    assets['up_space'] = pygame.image.load(os.path.join(IMG_DIR, 'up_space.png')).convert_alpha()
    assets['up_space'] = pygame.transform.scale(assets['up_space'], (button_width, button_height))
    assets['down_space'] = pygame.image.load(os.path.join(IMG_DIR, 'down_space.png')).convert_alpha()
    assets['down_space'] = pygame.transform.scale(assets['down_space'], (button_width, button_height))
    assets['icy_night'] = pygame.image.load(os.path.join(IMG_DIR, 'icy_night.png')).convert_alpha()
    assets['icy_night'] = pygame.transform.scale(assets['icy_night'], (WIDTH, HEIGHT))
    assets['icy_show'] = pygame.image.load(os.path.join(IMG_DIR, 'icy_show.png')).convert_alpha()
    assets['icy_show'] = pygame.transform.scale(assets['icy_show'], (WIDTH, HEIGHT))
    assets['transition'] = pygame.image.load(os.path.join(IMG_DIR, 'transition.png')).convert_alpha()
    assets['transition'] = pygame.transform.scale(assets['transition'], (600, 1700))
    assets['title'] = pygame.image.load(os.path.join(IMG_DIR, 'title.png')).convert_alpha()
    assets['title'] = pygame.transform.scale(assets['title'], (350, 350))
    assets['telafinal'] = pygame.image.load(os.path.join(IMG_DIR, 'telafinal.png')).convert_alpha()
    assets['telafinal'] = pygame.transform.scale(assets['telafinal'], (600, 600))
    
    
    
    # sistema de placar
    assets["score_font"] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28)
    assets['score'] = 0
    assets['ice_font'] = pygame.font.Font(os.path.join(FNT_DIR, 'FROZBITE.ttf'), 60)
    assets['ice2_font'] = pygame.font.Font(os.path.join(FNT_DIR, 'FROZBITE.ttf'), 28)
    assets['ice3_font'] = pygame.font.Font(os.path.join(FNT_DIR, 'FROZBITE.ttf'), 220)

    # Sons serelepes
    pygame.mixer.music.load(os.path.join(SND_DIR, 'BeepBox_intro.wav'))
    pygame.mixer.music.set_volume(0.5)
    assets['boom'] = pygame.mixer.Sound(os.path.join(SND_DIR, 'boom.wav'))
    assets['transition_sound'] = pygame.mixer.Sound(os.path.join(SND_DIR, 'transition_sound.wav'))
    assets['hihat'] = pygame.mixer.Sound(os.path.join(SND_DIR, 'hihat.wav'))
    assets['button'] = pygame.mixer.Sound(os.path.join(SND_DIR, 'button.wav'))

    # Anima????es
    idle_anim = [] # anima????o de repouso
    for i in range(2):
        # Os arquivos de anima????o s??o numerados de 00 a 01
        filename = os.path.join(ANIM_DIR, 'idle0{}.png'.format(i))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (128, 128))
        idle_anim.append(img)
    assets["idle_anim"] = idle_anim

    big_idle_anim = [] # anima????o de repouso
    for i in range(2):
        # Os arquivos de anima????o s??o numerados de 00 a 01
        filename = os.path.join(ANIM_DIR, 'idle0{}.png'.format(i))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (500, 500))
        big_idle_anim.append(img)
    assets["big_idle_anim"] = big_idle_anim

    right_anim = [] # anima????o do penguin para direita
    for i in range(5):
        # Os arquivos de anima????o s??o numerados de 00 a 04
        filename = os.path.join(ANIM_DIR, 'right0{}.png'.format(i))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (128, 128))
        right_anim.append(img)
    assets["right_anim"] = right_anim

    left_anim = [] # anima????o do penguin para esquerda
    for i in range(5):
        # Os arquivos de anima????o s??o numerados de 00 a 04
        filename = os.path.join(ANIM_DIR, 'left0{}.png'.format(i))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (128, 128))
        left_anim.append(img)
    assets["left_anim"] = left_anim
    
    up_anim = [] # anima????o do penguin para cima
    for i in range(5):
        # Os arquivos de anima????o s??o numerados de 00 a 04
        filename = os.path.join(ANIM_DIR, 'up0{}.png'.format(i))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (128, 128))
        up_anim.append(img)
    assets["up_anim"] = up_anim

    down_anim = [] # anima????o do penguin para baixo
    for i in range(5):
        # Os arquivos de anima????o s??o numerados de 00 a 04
        filename = os.path.join(ANIM_DIR, 'down0{}.png'.format(i))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (128, 128))
        down_anim.append(img)
    assets["down_anim"] = down_anim

    miss_anim = [] # anima????o do penguin para um erro
    for i in range(5):
        # Os arquivos de anima????o s??o numerados de 00 a 04
        filename = os.path.join(ANIM_DIR, 'miss0{}.png'.format(i))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (128, 128))
        miss_anim.append(img)
    assets["miss_anim"] = miss_anim

    return assets