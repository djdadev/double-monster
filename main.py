import pygame,sys
pygame.init()


def boss_talk():
    global health_b
    if health_b <= 300 and health_b >= 200:
        text = font2.render("HA HA HA WELCOME TO YOUR END", True, (0,0,0))
        text_rect = text.get_rect(center = (110,80))
        text2 = font2.render("LET'S BEGIN...", True, (0,0,0))
        text_rect2 = text2.get_rect(center = (110,100))
        screen.blit(text,text_rect)
        screen.blit(text2,text_rect2)
    if health_b < 200 and health_b >= 100:
        text25 = font2.render("YOU THINK YOU CAN BEAT ME", True, (0,0,0))
        text_rect25 = text25.get_rect(center = (110,80))
        text3 = font2.render("AS I GUESSED", True, (0,0,0))
        text_rect3 = text3.get_rect(center = (110,100))
        screen.blit(text25,text_rect25)
        screen.blit(text3,text_rect3)
    if health_b < 100:
        text35 = font2.render("NO NO STOP", True, (0,0,0))
        text_rect35 = text35.get_rect(center = (110,80))
        screen.blit(text35,text_rect35)
        text350 = font2.render("I AM GONA COME BACK WARRIOR COOKIE", True, (0, 0, 0))
        text_rect350 = text350.get_rect(center=(110, 100))
        screen.blit(text350, text_rect350)

# font
font = pygame.font.Font("04B_19.TTF",20)
font2 = pygame.font.Font("04B_19.TTF",10)
font25 = pygame.font.Font("04B_19.TTF",15)
# rects
# player
player = pygame.image.load("3.png")
player_Rect = player.get_rect(center = (250,250))

# player_attack
p_attack = pygame.image.load("attack cookie2.png")
p_rect = p_attack.get_rect(center = (250,450))
# boss
boss = pygame.image.load("boss.png")
boss_Rect = boss.get_rect(center = (260,150))
# konuşma şeysi
text_stuff = pygame.image.load("text box3.png")
text_stuff_rect = text_stuff.get_rect(center = (110,100))
# attack1
skeleton_image = pygame.image.load("skeleton43.png")
attack = skeleton_image.get_rect(center = (0 - 50, player_Rect.y + 30))
# attack2
skeleton_image2 = pygame.image.load("skeleton43.png")
attack2 = skeleton_image2.get_rect(center = (player_Rect.x, 0 - 50 + 30))
# attack3
skeleton_image3 = pygame.image.load("skeleton43.png")
attack3 = skeleton_image3.get_rect(center = (0 - 50, player_Rect.y + 30))
# attack4
skeleton_image4 = pygame.image.load("skeleton43.png")
attack4 = skeleton_image4.get_rect(center = (player_Rect.x, 70))
# attack 5 side
side_rect = pygame.Rect(0 - 100, player_Rect.y,50,50)

# arrow stuff
s_rect = pygame.Rect(-10,150,550,200)
arc_rect1 = pygame.Rect(250,220,100,50)
arrow_image = pygame.image.load("arrow.png")
arrow_rect = arrow_image.get_rect(center = (390,240))
# rect border
final_Rect = pygame.Rect(100,250,300,250)
final_Rect.left = 100
final_Rect.right = 400

def player_attack_func():
    screen.blit(p_attack,p_rect)

def start_rect_func():
    pygame.draw.rect(screen, (255,255,255), s_rect, 5)
def arrow():
    pygame.draw.rect(screen, (255,255,255), arc_rect1)
    screen.blit(arrow_image,arrow_rect)

def text_stuff_func():
        screen.blit(text_stuff, text_stuff_rect)
def finalrect_func():
    pygame.draw.rect(screen, (255,255,255), final_Rect, 5)

def boss_func():
    screen.blit(boss,boss_Rect)
def player_func():
    global speed,speed_y,game_state,health_p,health_starting,game_start
    player_Rect.x += speed
    player_Rect.y += speed_y
    if game_start == True:
        if player_Rect.top <= s_rect.top:
            player_Rect.top = s_rect.top
        if player_Rect.bottom >= s_rect.bottom:
            player_Rect.bottom = s_rect.bottom
        if player_Rect.right >= 500:
            game_start = False
            player_Rect.center = 250,450
    if game_start == False:
        if player_Rect.right >= final_Rect.right:
            player_Rect.right = final_Rect.right
        if player_Rect.left <= final_Rect.left:
            player_Rect.left = final_Rect.left
        if player_Rect.top <= final_Rect.top:
            player_Rect.top = final_Rect.top
        if player_Rect.bottom >= final_Rect.bottom:
            player_Rect.bottom = final_Rect.bottom

    #pygame.draw.rect(screen, (255,255,255), player)
    screen.blit(player,player_Rect)

def attack_func():
    global attack_speed
    attack.x += attack_speed
    if attack.right >= 550:
        attack.center = 0 - 50,player_Rect.y + 30
    #pygame.draw.rect(screen, (255,0,0), attack)
    screen.blit(skeleton_image,attack)
def attack_func2():
    global attack_speed
    attack2.y += attack_speed
    if attack2.bottom >= 550:
        attack2.center = player_Rect.x, 0 - 50 + 30
    #pygame.draw.rect(screen, (255,0,0), attack)
    screen.blit(skeleton_image2,attack2)
def attack_func3():
    global attack_speed25,loop
    loop -= 5
    if loop <= 0:
        attack3.x += attack_speed25
        if attack3.right >= 550:
            attack3.center = 0 - 50,player_Rect.y + 30
            loop = 1000
    #pygame.draw.rect(screen, (255,0,0), attack)
    screen.blit(skeleton_image3,attack3)
def attack_func4():
    global attack_speed25,loop2
    loop2 -= 5
    if loop2 <= 0:
        attack4.y += attack_speed25
        if attack4.bottom >= 550:
            attack4.center = player_Rect.x, 70
            loop2 = 1000
    #pygame.draw.rect(screen, (255,0,0), attack)
    screen.blit(skeleton_image4,attack4)

def attack_side():
    global attack_speed
    side_rect.x += attack_speed
    if side_rect.right >= 600:
        side_rect.center = 0 - 100, player_Rect.y
    pygame.draw.rect(screen, (255, 255, 255), side_rect)

def over_func():
    text = font.render("GAME OVER", True, (255,255,255))
    text_rect = text.get_rect(center = (250,250))
    screen.blit(text,text_rect)
def finish_func():
    text = font25.render("WELL DONE WARRIOR YOU DEFEAT THE KURABIYE CANAVARI ", True, (255, 255, 255))
    text_rect = text.get_rect(center=(250, 250))
    screen.blit(text, text_rect)

def collision_detection():
    global health_p,health_starting,health_b,health_starting2,shoot_state
    # collisons
    if player_Rect.colliderect(attack):
        attack.center = 0 - 50,player_Rect.y + 30
        health_p -= 10
        health_starting += 10
        if health_p > 0:
            return True
        else:
            return False

    if player_Rect.colliderect(attack2):
        attack2.center = player_Rect.x, 0 - 50 + 30
        health_p -= 10
        health_starting += 10
        if health_p > 0:
            return True
        else:
            return False

    if player_Rect.colliderect(attack3):
        attack3.center = 0 - 50,player_Rect.y + 30
        health_p -= 10
        health_starting += 10
        if health_p > 0:
            return True
        else:
            return False

    if player_Rect.colliderect(attack4):
        attack4.center = player_Rect.x, 0 - 50 + 30
        health_p -= 10
        health_starting += 10
        if health_p > 0:
            return True
        else:
            return False


    return True
def collision_detection2():
    global health_b,health_starting2,shoot_state
    if p_rect.colliderect(boss_Rect):
        p_rect.center = player_Rect.x,player_Rect.y
        shoot_state = "ready"
        health_b -= 5
        health_starting2 += 5
        if health_b <= 0:
            return True
        else:
            return False

    return False

def health_player():
    global health_p,health_starting
    if health_p <= 200:
        pygame.draw.rect(screen, (0,255,0), (470,health_starting,20,health_p))
        pygame.draw.rect(screen, (255,255,255), (470,299 + 50,20,200 - 50), 5)
    if health_p <= 100:
        pygame.draw.rect(screen, (255,255,0), (470,health_starting,20,health_p))
        pygame.draw.rect(screen, (255,255,255), (470,299 + 50,20,200 - 50), 5)
    if health_p <= 50:
        pygame.draw.rect(screen, (255,0,0), (470,health_starting,20,health_p))
        pygame.draw.rect(screen, (255,255,255), (470,299 + 50,20,200 - 50), 5)
def boss_health():
    global health_b,health_starting2
    #if health_p <= 200:
        #pygame.draw.rect(screen, (0,255,0), (health_starting2,10,health_b,20))
        #pygame.draw.rect(screen, (255,255,255), (health_starting2,10,health_b,20), 5)
    #if health_p <= 100:
        #pygame.draw.rect(screen, (255,255,0), (health_starting2,10,health_b,20))
        #pygame.draw.rect(screen, (255,255,255), (health_starting2,10,health_b,20), 5)
    if health_p <= 300:
        pygame.draw.rect(screen, (255,0,0), (health_starting2,10,health_b,20))
        pygame.draw.rect(screen, (255,255,255), (199,10,300,20), 5)

class Attack1:
    def __init__(self):
        global image
        global rect
        self.image = pygame.image.load("skeleton43.png")
        self.rect = self.image.get_rect(center = (0 - 50, player_Rect.y + 30))

    def shooting_mech1(self):
        global attack_speed
        self.rect.x += attack_speed
        if self.rect.right >= 550:
            self.rect.center = 0 - 50, player_Rect.y + 30
        # pygame.draw.rect(screen, (255,0,0), attack)
        screen.blit(self.image, self.rect)
class Attack_up:
    def __init__(self):
        self.image = pygame.image.load("skeleton43.png")
        self.rect = self.image.get_rect(center = (0 - 50, player_Rect.y + 30))

    def shooting_mech1(self):
        global attack_speed
        self.rect.x += attack_speed
        if self.rect.right >= 550:
            self.rect.center = player_Rect.x, 0 - 50
        # pygame.draw.rect(screen, (255,0,0), attack)
        screen.blit(self.image, self.rect)



# screen
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500,500))
caption = pygame.display.set_caption("Double Monster")
# game varibles
speed = 0
speed_y = 0
attack_speed = 5
attack_speed25 = 5
attack_speed2 = -10
game_state = True
game_start = True
game_finish = False
health_p = 200 - 50
health_starting = 299 + 50
health_b = 300
health_starting2 = 199
n = 0
shoot_state = "ready"
loop = 1000
loop2 = 1000

def cycle():
    global game_state,health_p,health_starting,shoot_state,game_finish,health_b,health_starting2,game_start
    if game_start == True:
        arrow()
        start_rect_func()
        player_func()
    if game_state == True and game_start == False:
        finalrect_func()
        player_func()
        health_player()
        boss_health()
        # attack player states
        if shoot_state == "fire":
            player_attack_func()
            p_rect.y += attack_speed2
            if p_rect.y <= 0:
                shoot_state = "ready"

        game_state = collision_detection()
        game_finish = collision_detection2()
        text_stuff_func()
        boss_talk()
        if health_b <= 299:
            attack_func()
            attack_func2()

        if health_b <= 150:
            attack_func3()
            attack_func4()

        boss_func()
    if game_state == False and game_finish == False:
        game_start = False
        health_p = 200 - 50
        health_starting = 299 + 50
        health_b = 300
        health_starting2 = 199
        attack.center = 0 - 50,player_Rect.y + 40
        attack2.center = player_Rect.x, 0 - 50 + 30
        player_Rect.center = 250,250
        over_func()

    if game_finish == True:
        game_state = False
        attack2.center = player_Rect.x, 0 - 50 + 30
        attack.center = 0 - 50, player_Rect.y + 40
        player_Rect.center = 250, 250
        finish_func()


    pygame.display.update()
    clock.tick(60)

while True:
    #screen.blit(background, (0,0))
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed_y = -5
            if event.key == pygame.K_e:
                #health_p += 10
                #health_starting -= 10
                health_b -= 10
                health_starting2 += 10
            if event.key == pygame.K_DOWN:
                speed_y = 5
            if event.key == pygame.K_LEFT:
                speed = -5
            if event.key == pygame.K_RIGHT:
                speed = 5
            if event.key == pygame.K_SPACE:
                if game_state == True:
                    if shoot_state == "ready":
                        p_rect.center = player_Rect.x + 30,player_Rect.y
                        shoot_state = "fire"

            if event.key == pygame.K_h:
                if game_state == False:
                    game_start = True
                    game_state = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                speed_y = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                speed = 0
            #if event.key == pygame.K_SPACE:
                #speed_y = 15

    cycle()
