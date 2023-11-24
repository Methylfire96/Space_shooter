import pygame, sys, time, random
pygame.font.init()
pygame.mixer.init()

# name
pygame.display.set_caption("Final Project Space shooter")

# window
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# bg
BG = pygame.image.load("stars.jpg")
BG = pygame.transform.scale(BG, (WINDOW_WIDTH, WINDOW_HEIGHT))
bg_music = pygame.mixer.Sound("bg_music.mp3")
victory_sound = pygame.mixer.Sound("victory.mp3")
game_over_sound = pygame.mixer.Sound("game_over.mp3")
bg = 0

# player
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 70
PLAYER_MOVE = 15
P1 = pygame.image.load("Raumschiff_py2.png")
P1 = pygame.transform.scale(P1, (90,60))

# ufo
UFO_WIDTH = 80
UFO_HEIGHT = 60
UFO_MOVE = 10
UFO1 = pygame.image.load("ufo1.gif")
UFO2 = pygame.image.load("ufo2.gif")
UFO3 = pygame.image.load("ufo3.gif")
UFO1 = pygame.transform.scale(UFO1, (UFO_WIDTH, UFO_HEIGHT))
UFO2 = pygame.transform.scale(UFO2, (UFO_WIDTH, UFO_HEIGHT))
UFO3 = pygame.transform.scale(UFO3, (UFO_WIDTH, UFO_HEIGHT))
ufos = []

# collisions
COUNTER = 10
FONT = pygame.font.Font(None, 30)
LIFE_BAR = pygame.Rect(20, WINDOW_HEIGHT- 40, 30, 30)

# bullets
POINTS = 0
BTIME = pygame.time.get_ticks()
SCORE_BAR = pygame.Rect(WINDOW_WIDTH - 100, WINDOW_HEIGHT - 40, 30, 30)
BULLET = pygame.image.load("bullet.gif")
BULLET = pygame.transform.scale(BULLET, (15, 40))
bullet_sound = pygame.mixer.Sound("blaster.mp3")
bullets = []

# winner /game over
WINNER = pygame.image.load("winner.gif")
WINNER = pygame.transform.scale(WINNER, (WINDOW_WIDTH, WINDOW_HEIGHT))
GAME_OVER = pygame.image.load("game_over.gif")
GAME_OVER = pygame.transform.scale(GAME_OVER, (WINDOW_WIDTH, WINDOW_HEIGHT))




# draw/ show --------------------------------------------------------------------------------
def update(player):
    WINDOW.blit(BG, (0, bg))
    WINDOW.blit(BG, (0, bg - WINDOW_HEIGHT))
    WINDOW.blit(P1, player)
    
    # ufo
    for ufo in ufos:
        random_UFO = random.choice([UFO1, UFO2, UFO3])
        WINDOW.blit(random_UFO, ufo)
        
    # update collision player with ufo (Life- COUNTER)
    LIFE = FONT.render(f"Hull power: {COUNTER}", True, "orange")
    WINDOW.blit(LIFE, LIFE_BAR)
    
    # update Score
    SCORE = FONT.render(f"Score: {POINTS}", True, "orange")
    WINDOW.blit(SCORE, SCORE_BAR)
    
    # bullets
    for bullet in bullets:
        WINDOW.blit(BULLET, bullet)
    
    # always last call of def update()
    pygame.display.update()
    
# main ---------------------------------------------------------------------------------------
def main():
    run = True
    clock = pygame.time.Clock()
    player = pygame.Rect(WINDOW_WIDTH/2, WINDOW_HEIGHT - PLAYER_HEIGHT*2, PLAYER_WIDTH, PLAYER_HEIGHT)
    global bg, COUNTER, POINTS, BTIME, bullets
    bg_music.play(-1)
    
    while run:
        clock.tick(60)
        ctime = pygame.time.get_ticks()
        
        bg += 4
        if bg >= WINDOW_HEIGHT:
            bg = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        # player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - PLAYER_MOVE >= 0:
            player.x -= PLAYER_MOVE
            
        if keys[pygame.K_d] and player.x + PLAYER_MOVE + PLAYER_WIDTH*2 <= WINDOW_WIDTH:
            player.x += PLAYER_MOVE
            
        if keys[pygame.K_w] and player.y - PLAYER_HEIGHT - PLAYER_MOVE >= 0:
            player.y -= PLAYER_MOVE
        
        if keys[pygame.K_s] and player.y + PLAYER_HEIGHT + PLAYER_MOVE <= WINDOW_HEIGHT :
            player.y += PLAYER_MOVE
        
        if keys[pygame.K_SPACE] and ctime - BTIME >= 300:
            bullet = pygame.Rect(player.x + PLAYER_WIDTH//2 - 5, player.y, 10, 20)
            bullets.append(bullet)
            bullet_sound.play()
            BTIME = ctime
        
        
        # ufos movement
        if random.randint(0, 100)<2:
            ufo = pygame.Rect(random.randint(0, WINDOW_WIDTH - UFO_WIDTH), 0, UFO_WIDTH, UFO_HEIGHT)
            ufos.append(ufo)
        
        for ufo in ufos:
            ufo.y += UFO_MOVE
            if ufo.y > WINDOW_HEIGHT:
                ufos.remove(ufo)
            
        # collisions
        for ufo in ufos:
            if player.colliderect(ufo):
                COUNTER -= 1
                print(f"Collided! hull is now {COUNTER}")
                ufos.remove(ufo)
                if COUNTER <= 0:
                    print("---------------Game Over!-----------------")
                    pygame.mixer.pause()
                    WINDOW.blit(GAME_OVER, (0, 0))
                    pygame.display.update()
                    game_over_sound.play()
                    pygame.time.wait(8000)
                    pygame.quit()
        
        # bullets
        new_bullets = []
        for bullet in bullets:
            bullet.y -= 20
            if bullet.y > 0:
                new_bullets.append(bullet)
        bullets = new_bullets
                
        for bullet in bullets:
            for ufo in ufos:
                if bullet.colliderect(ufo):
                    POINTS += 1
                    print(f"You hit an Ufo {POINTS}")
                    ufos.remove(ufo)
                    bullets.remove(bullet)
                    if POINTS == 2001:
                        print("---------------You Win!-----------------")
                        pygame.mixer.pause()
                        WINDOW.blit(WINNER, (0, 0))
                        pygame.display.update()
                        victory_sound.play()
                        pygame.time.wait(8000)
                        pygame.quit()
        
                
        
        
        # update the def update while run -----------------------------------------------------
        update(player)
        
    pygame.quit()    

if __name__ == "__main__":
    main()