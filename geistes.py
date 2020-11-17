import pygame
import random
import time

pygame.init()
screenWidth = 1366
screenHeight = 768

screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.FULLSCREEN)
pygame.display.set_caption("GEISTES")


def font(size):
    myFont = pygame.font.Font('freesansbold.ttf', size)
    return myFont


def mix():
    mix_carts = []
    for j in range(18):
        number = random.randint(1, 18)
        while number in mix_carts:
            number = random.randint(1, 18)
        mix_carts.append(number)
    return mix_carts


def background_music():
    pygame.mixer.music.load('./music/Danny-Cocke-Afterdark.mp3')
    pygame.mixer.music.play(-1)


def help_surface():
    screen.fill((52, 77, 105))

    fonts = font(25)
    description = pygame.image.load('./images/img/description.png')
    screen.blit(description, (160, 80))
    pygame.draw.rect(screen, (178, 136, 178), (1000, 550, 250, 70), 0)
    help_txt = fonts.render("Press 'R' to return", True, (165, 7, 31))
    screen.blit(help_txt, (1020, 572))

    pygame.display.update()


def score_surface():
    screen.fill((36, 37, 81))

    fonts = font(25)
    pygame.draw.rect(screen, (178, 136, 178), (1000, 600, 250, 70), 0)
    help_txt = fonts.render("Press 'R' to return", True, (165, 7, 31))
    screen.blit(help_txt, (1020, 622))

    pygame.display.update()


def show_obj():
    letter_font = font(30)
    screen.fill((141, 219, 205))
    flashlight = pygame.image.load('./images/objects/light.jpg')
    screen.blit(flashlight, (80, 150))
    pygame.draw.circle(screen, (36, 37, 81), (80, 294), 20, 0)
    a = letter_font.render('a', True, (255, 255, 255))
    screen.blit(a, (71, 278))

    clock = pygame.image.load('./images/objects/time.jpg')
    screen.blit(clock, (280, 50))
    pygame.draw.circle(screen, (36, 37, 81), (280, 218), 20, 0)
    b = letter_font.render('b', True, (255, 255, 255))
    screen.blit(b, (271, 204))

    hat = pygame.image.load('./images/objects/hatt.jpg')
    screen.blit(hat, (480, 50))
    pygame.draw.circle(screen, (36, 37, 81), (480, 209), 20, 0)
    c = letter_font.render('c', True, (255, 255, 255))
    screen.blit(c, (471, 193))

    owl = pygame.image.load('./images/objects/owl.jpg')
    screen.blit(owl, (670, 150))
    pygame.draw.circle(screen, (36, 37, 81), (670, 288), 20, 0)
    d = letter_font.render('d', True, (255, 255, 255))
    screen.blit(d, (659, 273))

    key = pygame.image.load('./images/objects/keyy.jpg')
    screen.blit(key, (650, 318))
    pygame.draw.circle(screen, (36, 37, 81), (650, 464), 20, 0)
    e = letter_font.render('e', True, (255, 255, 255))
    screen.blit(e, (641, 448))

    bat = pygame.image.load('./images/objects/bat.jpg')
    screen.blit(bat, (100, 318))
    pygame.draw.circle(screen, (36, 37, 81), (100, 472), 20, 0)
    i = letter_font.render('i', True, (255, 255, 255))
    screen.blit(i, (96, 458))

    cruse = pygame.image.load('./images/objects/kozee.JPG')
    screen.blit(cruse, (150, 502))
    pygame.draw.circle(screen, (36, 37, 81), (150, 654), 20, 0)
    h = letter_font.render('h', True, (255, 255, 255))
    screen.blit(h, (141, 639))

    mirror = pygame.image.load('./images/objects/shadoww.jpg')
    screen.blit(mirror, (600, 502))
    pygame.draw.circle(screen, (36, 37, 81), (600, 637), 20, 0)
    f = letter_font.render('f', True, (255, 255, 255))
    screen.blit(f, (594, 623))

    shadow = pygame.image.load('./images/objects/mirror.jpg')
    screen.blit(shadow, (370, 530))
    pygame.draw.circle(screen, (36, 37, 81), (370, 675), 20, 0)
    g = letter_font.render('g', True, (255, 255, 255))
    screen.blit(g, (360, 657))


def play():
    answers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    InvTime = 10
    #noResponse = True
    Tfont = font(70)
    Mfont = font(25)
    cart_list = mix()
    pygame.draw.rect(screen, (141, 219, 205), (880, 50, 100, 150), 0)
    timer = Tfont.render(str(InvTime), True, (255, 0, 0))
    screen.blit(timer, (900, 50))
    pygame.display.flip()
    for i in range(len(cart_list)):
        if i == 0:
            InvTime = 10
        else:
            InvTime = 11
        noResponse = True
        cart_name = str(cart_list[i]) + ".jpg"
        cart = pygame.image.load("./images/carts/small/"+cart_name)
        pygame.display.flip()
        screen.blit(cart, (350, 250))
        pygame.display.flip()
        while InvTime != 0 and noResponse:
            time.sleep(1)
            InvTime -= 1
            pygame.draw.rect(screen, (141, 219, 205), (880, 50, 100, 70), 0)
            pygame.display.flip()
            timer2 = Tfont.render(str(InvTime), True, (255, 0, 0))
            screen.blit(timer2, (900, 50))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        response = 'a'
                        if response == answers[cart_list[i] - 1]:
                            InvTime = 10
                            noResponse = False
                            pygame.draw.rect(screen, (141, 219, 205), (850, 140, 100, 70), 0)
                            pygame.display.flip()
                            correct = Mfont.render('Correct Answer', True, (0, 0, 255))
                            screen.blit(correct, (860, 140))
                        else:
                            pygame.draw.rect(screen, (141, 219, 205), (850, 140, 100, 70), 0)
                            pygame.display.flip()
                            correct = Mfont.render('Wrong Answer', True, (0, 0, 255))
                            screen.blit(correct, (860, 140))
                    if event.key == pygame.K_b:
                        response = 'b'
                        if response == answers[cart_list[i] - 1]:
                            InvTime = 10
                            noResponse = False
                            pygame.draw.rect(screen, (141, 219, 205), (850, 140, 100, 70), 0)
                            pygame.display.flip()
                            correct = Mfont.render('Correct Answer', True, (0, 0, 255))
                            screen.blit(correct, (860, 140))
                        else:
                            pygame.draw.rect(screen, (141, 219, 205), (850, 140, 100, 70), 0)
                            pygame.display.flip()
                            correct = Mfont.render('Wrong Answer', True, (0, 0, 255))
                            screen.blit(correct, (860, 140))
                    if event.key == pygame.K_c:
                        response = 'c'
                        if response == answers[cart_list[i] - 1]:
                            InvTime = 10
                            noResponse = False
                            pygame.draw.rect(screen, (141, 219, 205), (850, 140, 100, 70), 0)
                            pygame.display.flip()
                            correct = Mfont.render('Correct Answer', True, (0, 0, 255))
                            screen.blit(correct, (860, 140))
                        else:
                            pygame.draw.rect(screen, (141, 219, 205), (850, 140, 100, 70), 0)
                            pygame.display.flip()
                            correct = Mfont.render('Wrong Answer', True, (0, 0, 255))
                            screen.blit(correct, (860, 140))
                    if event.key == pygame.K_d:
                        response = 'd'
                        if response == answers[cart_list[i] - 1]:
                            InvTime = 10
                            noResponse = False
                            pygame.draw.rect(screen, (141, 219, 205), (850, 140, 100, 70), 0)
                            pygame.display.flip()
                            correct = Mfont.render('Correct Answer', True, (0, 0, 255))
                            screen.blit(correct, (860, 140))
                        else:
                            pygame.draw.rect(screen, (141, 219, 205), (850, 140, 100, 70), 0)
                            pygame.display.flip()
                            correct = Mfont.render('Wrong Answer', True, (0, 0, 255))
                            screen.blit(correct, (860, 140))
                    if event.key == pygame.K_e:
                        response = 'e'
                        if response == answers[cart_list[i] - 1]:
                            InvTime = 10
                            noResponse = False
                            pygame.draw.rect(screen, (141, 219, 205), (850, 140, 100, 70), 0)
                            pygame.display.flip()
                            correct = Mfont.render('Correct Answer', True, (0, 0, 255))
                            screen.blit(correct, (860, 140))
                        else:
                            pygame.draw.rect(screen, (141, 219, 205), (850, 140, 100, 70), 0)
                            pygame.display.flip()
                            correct = Mfont.render('Wrong Answer', True, (0, 0, 255))
                            screen.blit(correct, (860, 140))
                    if event.key == pygame.K_f:
                        response = 'f'
                        if response == answers[cart_list[i] - 1]:
                            InvTime = 10
                            noResponse = False
                            pygame.draw.rect(screen, (141, 219, 205), (850, 140, 100, 70), 0)
                            pygame.display.flip()
                            correct = Mfont.render('Correct Answer', True, (0, 0, 255))
                            screen.blit(correct, (860, 140))
                        else:
                            pygame.draw.rect(screen, (141, 219, 205), (850, 140, 100, 70), 0)
                            pygame.display.flip()
                            correct = Mfont.render('Wrong Answer', True, (0, 0, 255))
                            screen.blit(correct, (860, 140))
                    if event.key == pygame.K_g:
                        response = 'g'
                        if response == answers[cart_list[i] - 1]:
                            InvTime = 10
                            noResponse = False
                            pygame.draw.rect(screen, (141, 219, 205), (850, 140, 100, 70), 0)
                            pygame.display.flip()
                            correct = Mfont.render('Correct Answer', True, (0, 0, 255))
                            screen.blit(correct, (860, 140))
                        else:
                            pygame.draw.rect(screen, (141, 219, 205), (850, 140, 100, 70), 0)
                            pygame.display.flip()
                            correct = Mfont.render('Wrong Answer', True, (0, 0, 255))
                            screen.blit(correct, (860, 140))
                    if event.key == pygame.K_h:
                        response = 'h'
                        if response == answers[cart_list[i] - 1]:
                            InvTime = 10
                            noResponse = False
                            pygame.draw.rect(screen, (141, 219, 205), (850, 140, 100, 70), 0)
                            pygame.display.flip()
                            correct = Mfont.render('Correct Answer', True, (0, 0, 255))
                            screen.blit(correct, (860, 140))
                        else:
                            pygame.draw.rect(screen, (141, 219, 205), (850, 140, 100, 70), 0)
                            pygame.display.flip()
                            correct = Mfont.render('Wrong Answer', True, (0, 0, 255))
                            screen.blit(correct, (860, 140))
                    if event.key == pygame.K_i:
                        response = 'i'
                        if response == answers[cart_list[i] - 1]:
                            InvTime = 10
                            noResponse = False
                            pygame.draw.rect(screen, (141, 219, 205), (850, 140, 100, 70), 0)
                            pygame.display.flip()
                            correct = Mfont.render('Correct Answer', True, (0, 0, 255))
                            screen.blit(correct, (860, 140))
                        else:
                            pygame.draw.rect(screen, (141, 219, 205), (850, 140, 100, 70), 0)
                            pygame.display.flip()
                            correct = Mfont.render('Wrong Answer', True, (0, 0, 255))
                            screen.blit(correct, (860, 140))


def first_surface():
    game_over = False

    screen.fill((36, 37, 81))

    geistes_img = pygame.image.load('./images/img/Geistesblitz-5-vor-12(2).jpg')
    screen.blit(geistes_img, (0, 0))
    game_img = pygame.image.load('./images/img/71xM7BosVRL.jpg')
    screen.blit(game_img, (775, 0))

    fonts = font(25)
    pygame.draw.rect(screen, (178, 136, 178), (800, 265, 250, 70), 0)
    help_txt = fonts.render("Press 'H' for help", True, (165, 7, 31))
    screen.blit(help_txt, (820, 287))

    pygame.draw.rect(screen, (178, 136, 178), (1040, 350, 300, 70), 0)
    high_score_txt = fonts.render("Press 'S' for high score", True, (165, 7, 31))
    screen.blit(high_score_txt, (1050, 372))

    bigFont = font(35)
    play_txt = bigFont.render("Do You Want To Play?", True, (229, 223, 69))
    screen.blit(play_txt, (850, 490))

    name_txt = bigFont.render("Enter Your Name", True, (229, 223, 69))
    screen.blit(name_txt, (890, 540))
    pygame.draw.rect(screen, (255, 255, 255), (915, 590, 250, 50), 0)

    fonts1 = font(17)
    pygame.draw.rect(screen, (178, 136, 178), (1180, 680, 150, 45), 0)
    exit_txt = fonts1.render("Press 'E' to exit", True, (165, 7, 31))
    screen.blit(exit_txt, (1190, 695))

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    help_surface()
                elif event.key == pygame.K_s:
                    score_surface()
                elif event.key == pygame.K_r:
                    first_surface()
                elif event.key == pygame.K_e:
                    game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                show_obj()
                play()

        pygame.display.update()
    pygame.quit()
    quit()

# ----------------------------------------------------------------------


background_music()
first_surface()
