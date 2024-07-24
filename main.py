# THE CONTROL FOR PLAYER 1 ( RIGHT SIDE ) IS KEY_UP FOR GO UP, AND KEY_DOWN FOR GO DOWN
# AND FOR THE PLAYER 2 ( LEFT SIDE ) IS W FOR GO UP, AND S FOR GO DOWN


import pygame, sys, random

# Animasi bola
def ball_animation():
    global ball_speed_x, ball_speed_y, player1_score, player2_score, score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    if ball.top <= 0 or ball.bottom >= screen_height:
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_y *= -1
        
    # Player Score
    if ball.left <= 0:
        pygame.mixer.Sound.play(score_sound)
        player1_score += 1
        score_time = pygame.time.get_ticks()
        
    # Computer Score
    if ball.right >= screen_width:
        pygame.mixer.Sound.play(score_sound)
        player2_score += 1
        score_time = pygame.time.get_ticks()
        
    if ball.colliderect(player1) and ball_speed_x > 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.right - player1.left) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - player1.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - player1.bottom) < 10 and ball_speed_y < 10:
            ball_speed_y *= -1
        
    if ball.colliderect(player2) and ball_speed_x < 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.left - player2.right) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - player2.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - player2.bottom) < 10 and ball_speed_y < 10:
            ball_speed_y *= -1

# Animaasi player
def player1_animation():
    player1.y += player1_speed
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= screen_height:
        player1.bottom = screen_height

# Animasi Computer
def player2_animation():
    player2.y += player2_speed
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= screen_height:
        player2.bottom = screen_height

def ball_start():
    global ball_speed_x, ball_speed_y, current_time, score_time, number_three
    
    current_time = pygame.time.get_ticks()
    ball.center = (screen_width/2, screen_height/2)
    
    if current_time - score_time < 700:
        number_three = game_font.render("3", False, light_grey)
        screen.blit(number_three,(screen_width/2 - 10, screen_height/2 + 20))
        
    if 700 < current_time - score_time < 1400:
        number_two = game_font.render("2", False, light_grey)
        screen.blit(number_two,(screen_width/2 - 10, screen_height/2 + 20))
    
    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render("1", False, light_grey)
        screen.blit(number_one,(screen_width/2 - 10, screen_height/2 + 20))
    
    if current_time - score_time <2100:
        ball_speed_x, ball_speed_y = 0, 0
    else:
        ball_speed_y = 7 * random.choice((1, -1))
        ball_speed_x = 7 * random.choice((1, -1))
        score_time = None
    
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

# Setup
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
clock = pygame.time.Clock()

# display
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Tampilan bola, player, dan computer
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 20, 20)
player1 = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 90)
player2 = pygame.Rect(10, screen_height/2 - 70, 10, 90)

# Warna
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

# Speed
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player1_speed = 0
player2_speed = 0

# Score teks
player1_score = 0
player2_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 30)

score_time = True

# Sound
pong_sound = pygame.mixer.Sound("StoneDropping.mp3")
score_sound = pygame.mixer.Sound("ScoreUp.mp3")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Thanks For Playing!")
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player1_speed += 7
            if event.key == pygame.K_UP:
                player1_speed -= 7
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player1_speed -= 7
            if event.key == pygame.K_UP:
                player1_speed += 7
                
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player2_speed += 6
            if event.key == pygame.K_w:
                player2_speed -= 6
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                player2_speed -= 6
            if event.key == pygame.K_w:
                player2_speed += 6
            
    ball_animation()
    player1_animation()
    player2_animation()
       
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player1)
    pygame.draw.rect(screen, light_grey, player2)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))
    
    if score_time:
        ball_start()
    
    player1_text = game_font.render(f"Player 1 = {player1_score}", False, light_grey)
    screen.blit(player1_text, (660,470))
    
    player2_text = game_font.render(f"Player 2 = {player2_score}", False, light_grey)
    screen.blit(player2_text, (160,470))
    
    if player1_score | player2_score >= 10:
        print("Game Finished!")
        print("Player 1 Score : " + str(player1_score))
        print("Player 2 Score : " + str(player2_score))
        print("Thanks For Playing!")
        pygame.quit()
        sys.exit()
    
    
    pygame.display.flip()
    clock.tick(60)