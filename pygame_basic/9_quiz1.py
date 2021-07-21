import pygame
from random import *

#####################################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init() 

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("똥 피하기")

# FPS
clock = pygame.time.Clock()
#####################################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
background = pygame.image.load("C:/Users/lsh76/chocolaWorkspace/python_module/pygame_basic/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/lsh76/chocolaWorkspace/python_module/pygame_basic/character.png")
character_size = character.get_rect().size  # 이미지의 크기를 구해옴
character_width = character_size[0]     # 캐릭터의 가로 크기
character_height = character_size[1]    # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2)    # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height              # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 이동할 좌표
to_x = 0

# 이동 속도
character_speed = 0.6

# 똥 만들기
enemy = pygame.image.load("C:/Users/lsh76/chocolaWorkspace/python_module/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 0.3

running = True

while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:    # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:   # 캐릭터를 오른쪽으로
                to_x += character_speed
        
        if event.type == pygame.KEYUP:   # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed * dt

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0 # 초기값
        enemy_x_pos = randint(0, screen_width - enemy_width)

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    screen.blit(background, (0, 0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))  # 적 그리기

    # 5. 화면에 그리기
    pygame.display.update()

pygame.quit()