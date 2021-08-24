# Python Game

## 1. 환경설정 & 프레임
```
    - pip install pygame
    - 1_create_frame.py file 생성
```
<pre>
<code>
# 1_create_frame.py
import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Chocolat Game") # 게임 이름

# 이벤트 루프
running = True # 게임이 진행중인가?

while running:
    for event in pygame.event.get():    # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님.

# pygame 종료
pygame.quit()
</code>
</pre>

## 2. 배경
```
    - 2_background.py file 생성
    - background = pygame.image.load("path") # 배경 이미지 불러오기
    - screen.blit(background, (0, 0)) # 배경 그리기
    - pygame.display.update() # 게임화면을 다시 그리기
```

## 3. 캐릭터
```
    - 3_main_sprite.py
```

## 4. 키보드 이벤트
```
    - 4_keyboard_event.py
```
<pre>
<code>
# 이동할 좌표
to_x = 0
to_y = 0

# 이벤트 루프
running = True # 게임이 진행중인가?

while running:
    for event in pygame.event.get():    # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님.

        if event.type == pygame.KEYDOWN:    # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                to_x -= 0.5
            elif event.key == pygame.K_RIGHT:   # 캐릭터를 오른쪽으로
                to_x += 0.5
            elif event.key == pygame.K_UP:  # 캐릭터를 위로
                to_y -= 0.5
            elif event.key == pygame.K_DOWN:    # 캐릭터를 아래로
                to_y += 0.5

        if event.type == pygame.KEYUP:   # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
        
    character_x_pos += to_x
    character_y_pos += to_y

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
</code>
</pre>

## 5. FPS
```
    - 5_frame_per_second.py
```
<pre>
<code>
# FPS
clock = pygame.time.Clock()

# 이동 속도
character_speed = 0.6

while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정
    print("fps : " + str(clock.get_fps()))

    # 캐릭터가 100만큼 이동을 해야함
    # 10 fps : 1초 동안에 10번 동작 -> 1번에 몇 만큼 이동? 10만큼! 10 * 10 = 100
    # 20 fps : 1초 동안에 20번 동작 -> 1번에 5만큼! 20 * 5 = 100
    ...
        
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
</code>
</pre>

## 6. 충돌 처리
```
    - 6_collision.py
    - colliderect
```
<pre>
<code>
    # 충돌 처리를 위한 rect 정보 업데이트
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
</code>
</pre>

## 7. 텍스트
```
    - 7_text.py
```
<pre>
<code>
# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트 객체 생성 (폰트, 크기)

# 총 시간
total_time = 10

# 시작 시간
start_ticks = pygame.time.get_ticks()   # 시작 tick을 받아옴

...
    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000   # 경과 시간(ms)을 1000으로 나누어서 초(s) 단위로 표시

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255)) # 출력할 글자, True, 글자 색상
    screen.blit(timer, (10, 10))    # 텍스트 표시

    # 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False

    pygame.display.update() # 게임화면을 다시 그리기!

# 잠시 대기
pygame.time.delay(2000) # 2초 정도 대기 (ms)
</code>
</pre>

## 8. 게임 개발 프레임
```
    - 8_frame.py
    - 기본 골격
```

## 9. Quiz : 하늘에서 떨어지는 똥 피하기 게임을 만드시오
```
    [게임 조건] 
    - 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
    - 똥은 화면 가장 위에서 떨어짐. X 좌표는 매번 랜덤으로 설정
    - 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
    - 캐릭터가 똥과 충돌하면 게임 종료
    - FPS는 30으로 고정

    [게임 이미지]
    - 배경 : 640 * 480 (세로 가로) - background.png
    - 캐릭터 : 70 * 70 - characer.png
    - 똥 : 70 * 70 - enemy.png
```

## 10. Project : 오락실 Pang 게임 만들기
```
    [게임 조건]
    1. 캐릭터는 화면 아래에 위치, 좌우로만 이동 가능
    2. 스페이스를 누르면 무기를 쏘아 올림
    3. 큰 공 1개가 나타나서 바운스
    4. 무기에 닿으면 공은 작은 크기 2개로 분할, 가장 작은 크기의 공은 사라짐
    5. 모든 공을 없애면 게임 종료 (성공)
    6. 캐릭터는 공에 닿으면 게임 종료 (실패)
    7. 시간 제한 99초 초과 시 게임 종료 (실패)
    8. FPS는 30으로 고정 (필요시 speed 값을 조정)

    [게임 이미지]
    1. 배경 : 640 * 480(가로 * 세로) - background.png
    2. 무대 : 640 * 50 - stage.png
    3. 캐릭터 : 33 * 60 - character.png
    4. 무기  20 * 430 - weapon.png
    5. 공 : 160 * 160, 80 * 80, 40 * 40, 20 * 20 - balloon1.png ~ balloon4.png
```

## 11. Project(Pang 게임) : 무기와 키보드 이벤트
```
    - 2_weapon_keyevent.py
```

## 12. Project(Pang 게임) : 공 만들기, 튀기기
```
    - 3_ball_movement.py
```

## 13. Project(Pang 게임) : 충돌 처리
```
    - 4_collision.py
    - 공, 캐릭터 충돌처리
    - 공, 무기 충돌처리
```

## 14. Project(Pang 게임) : 공 쪼개기
```
    - 5_ball_division.py
```

## 15. Project(Pang 게임) : 게임 오버
```
    - 6_gameover.py
    1. 모든 공을 없애면 게임 종료 (성공)
    2. 캐릭터는 공에 닿으면 게임 종료 (실패)
    3. 시간 제한 99초 초과 시 게임 종료 (실패)
```
