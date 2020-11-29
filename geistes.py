import pygame
import random
import time
from network import Network


class Geistes:
    def __init__(self):
        self.p1 = Player(1)
        self.p2 = Player(1)
        self.screenWidth = 1366
        self.screenHeight = 768
        self.net = Network()
        self.canvas = Canvas(self.screenWidth, self.screenHeight)

    def font(self, size):
        myFont = pygame.font.Font('freesansbold.ttf', size)
        return myFont

    """def mix(self):
        mix_carts = []
        for j in range(18):
            number = random.randint(1, 18)
            while number in mix_carts:
                number = random.randint(1, 18)
            mix_carts.append(number)
        return mix_carts"""

    def background_music(self):
        pygame.mixer.music.load('./music/Danny-Cocke-Afterdark.mp3')
        pygame.mixer.music.play(-1)

    def help_surface(self):
        self.canvas.get_screen().fill((52, 77, 105))

        fonts = self.font(25)
        description = pygame.image.load('./images/img/description.png')
        self.canvas.get_screen().blit(description, (160, 80))
        pygame.draw.rect(self.canvas.get_screen(), (178, 136, 178), (1000, 550, 250, 70), 0)
        help_txt = fonts.render("Press '3' to return", True, (165, 7, 31))
        self.canvas.get_screen().blit(help_txt, (1020, 572))

        pygame.display.update()

    def score_surface(self):
        self.canvas.get_screen().fill((36, 37, 81))

        fonts = self.font(25)
        pygame.draw.rect(self.canvas.get_screen(), (178, 136, 178), (1000, 600, 250, 70), 0)
        help_txt = fonts.render("Press '3' to return", True, (165, 7, 31))
        self.canvas.get_screen().blit(help_txt, (1020, 622))

        pygame.display.update()

    def show_obj(self):
        letter_font = self.font(30)
        self.canvas.get_screen().fill((141, 219, 205))
        flashlight = pygame.image.load('./images/objects/light.jpg')
        self.canvas.get_screen().blit(flashlight, (80, 150))
        pygame.draw.circle(self.canvas.get_screen(), (36, 37, 81), (80, 294), 20, 0)
        a = letter_font.render('a', True, (255, 255, 255))
        self.canvas.get_screen().blit(a, (71, 278))

        clock = pygame.image.load('./images/objects/time.jpg')
        self.canvas.get_screen().blit(clock, (280, 50))
        pygame.draw.circle(self.canvas.get_screen(), (36, 37, 81), (280, 218), 20, 0)
        b = letter_font.render('b', True, (255, 255, 255))
        self.canvas.get_screen().blit(b, (271, 204))

        hat = pygame.image.load('./images/objects/hatt.jpg')
        self.canvas.get_screen().blit(hat, (480, 50))
        pygame.draw.circle(self.canvas.get_screen(), (36, 37, 81), (480, 209), 20, 0)
        c = letter_font.render('c', True, (255, 255, 255))
        self.canvas.get_screen().blit(c, (471, 193))

        owl = pygame.image.load('./images/objects/owl.jpg')
        self.canvas.get_screen().blit(owl, (670, 150))
        pygame.draw.circle(self.canvas.get_screen(), (36, 37, 81), (670, 288), 20, 0)
        d = letter_font.render('d', True, (255, 255, 255))
        self.canvas.get_screen().blit(d, (659, 273))

        key = pygame.image.load('./images/objects/keyy.jpg')
        self.canvas.get_screen().blit(key, (650, 318))
        pygame.draw.circle(self.canvas.get_screen(), (36, 37, 81), (650, 464), 20, 0)
        e = letter_font.render('e', True, (255, 255, 255))
        self.canvas.get_screen().blit(e, (641, 448))

        bat = pygame.image.load('./images/objects/bat.jpg')
        self.canvas.get_screen().blit(bat, (100, 318))
        pygame.draw.circle(self.canvas.get_screen(), (36, 37, 81), (100, 472), 20, 0)
        i = letter_font.render('i', True, (255, 255, 255))
        self.canvas.get_screen().blit(i, (96, 458))

        cruse = pygame.image.load('./images/objects/kozee.JPG')
        self.canvas.get_screen().blit(cruse, (150, 502))
        pygame.draw.circle(self.canvas.get_screen(), (36, 37, 81), (150, 654), 20, 0)
        h = letter_font.render('h', True, (255, 255, 255))
        self.canvas.get_screen().blit(h, (141, 639))

        mirror = pygame.image.load('./images/objects/shadoww.jpg')
        self.canvas.get_screen().blit(mirror, (600, 502))
        pygame.draw.circle(self.canvas.get_screen(), (36, 37, 81), (600, 637), 20, 0)
        f = letter_font.render('f', True, (255, 255, 255))
        self.canvas.get_screen().blit(f, (594, 623))

        shadow = pygame.image.load('./images/objects/mirror.jpg')
        self.canvas.get_screen().blit(shadow, (370, 530))
        pygame.draw.circle(self.canvas.get_screen(), (36, 37, 81), (370, 675), 20, 0)
        g = letter_font.render('g', True, (255, 255, 255))
        self.canvas.get_screen().blit(g, (360, 657))

        fonts = self.font(25)
        yourID = fonts.render("Your ID is: "+self.net.id, True, (165, 7, 31))
        self.canvas.get_screen().blit(yourID, (900, 140))

    def run(self):
        clock = pygame.time.Clock()
        answers = ['e', 'c', 'i', 'b', 'd', 'f', 'a', 'd', 'f', 'a', 'a', 'c', 'c', 'd', 'h', 'f', 'g', 'd']
        cart_list = [5, 10, 13, 2, 14, 1, 17, 3, 6, 7, 4, 11, 16, 8, 9, 12, 15, 18]
        self.p1.win = False
        global response
        response = False
        run = True
        while run:
            if self.p1.cartID == 18:
                run = False
            response = False
            """cart_name = str(cart_list[self.p1.cartID]) + ".jpg"
            cart = pygame.image.load("./images/carts/small/"+cart_name)
            pygame.display.flip()
            self.screen.blit(cart, (350, 250))
            pygame.display.flip()"""
            time.sleep(1)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.p1.play('a')
                        if self.p1.move == answers[cart_list[self.p1.cartID] - 1]:
                            self.p1.win = True
                            self.p1.cartID += 1
                            self.p1.score += 1
                            response = True
                    if event.key == pygame.K_b:
                        self.p1.play('b')
                        if self.p1.move == answers[cart_list[self.p1.cartID] - 1]:
                            self.p1.win = True
                            self.p1.cartID += 1
                            self.p1.score += 1
                            response = True
                    if event.key == pygame.K_c:
                        self.p1.play('c')
                        if self.p1.move == answers[cart_list[self.p1.cartID] - 1]:
                            self.p1.win = True
                            self.p1.cartID += 1
                            self.p1.score += 1
                            response = True
                    if event.key == pygame.K_d:
                        self.p1.play('d')
                        if self.p1.move == answers[cart_list[self.p1.cartID] - 1]:
                            self.p1.win = True
                            self.p1.cartID += 1
                            self.p1.score += 1
                            response = True
                    if event.key == pygame.K_e:
                        self.p1.play('e')
                        if self.p1.move == answers[cart_list[self.p1.cartID] - 1]:
                            self.p1.win = True
                            self.p1.cartID += 1
                            self.p1.score += 1
                            response = True
                    if event.key == pygame.K_f:
                        self.p1.play('f')
                        if self.p1.move == answers[cart_list[self.p1.cartID] - 1]:
                            self.p1.win = True
                            self.p1.cartID += 1
                            self.p1.score += 1
                            response = True
                    if event.key == pygame.K_g:
                        self.p1.play('g')
                        if self.p1.move == answers[cart_list[self.p1.cartID] - 1]:
                            self.p1.win = True
                            self.p1.cartID += 1
                            self.p1.score += 1
                            response = True
                    if event.key == pygame.K_h:
                        self.p1.play('h')
                        if self.p1.move == answers[cart_list[self.p1.cartID] - 1]:
                            self.p1.win = True
                            self.p1.cartID += 1
                            self.p1.score += 1
                            response = True
                    if event.key == pygame.K_i:
                        self.p1.play('i')
                        if self.p1.move == answers[cart_list[self.p1.cartID] - 1]:
                            self.p1.win = True
                            self.p1.cartID += 1
                            self.p1.score += 1
                            response = True
            if response:
                self.show_answer_result(self.p1.win, self.net.id)
            self.p2.cartID = self.transfer_cartID(self.send_data())
            #self.p1.cartID = self.transfer_cartID(self.send_data())
            self.p1.draw(self.canvas.get_screen(), cart_list)
            self.p2.draw(self.canvas.get_screen(), cart_list)
            self.canvas.update()
            clock.tick(120)
        self.last_surface()

    def send_data(self):
        data = str(self.net.id) + ":" + str(self.p1.cartID) + ":" + str(self.p1.win)
        reply = self.net.send(data)
        return reply

    @staticmethod
    def transfer_cartID(data):
        try:
            reply = data.split(":")[1]
            return reply
        except:
            return 0

    def show_answer_result(self, win, id):
        Mfont = self.font(25)
        pygame.draw.rect(self.canvas.get_screen(), (141, 219, 205), (850, 130, 200, 45), 0)
        pygame.display.flip()
        if win:
            correct = Mfont.render('Correct Answer by ' + id, True, (0, 0, 255))
            self.canvas.get_screen().blit(correct, (860, 180))
        else:
            correct = Mfont.render('Wrong Answer by ' + id, True, (0, 0, 255))
            self.canvas.get_screen().blit(correct, (860, 140))

    def last_surface(self):
        self.canvas.get_screen().fill((36, 37, 81))
        fonts = self.font(25)
        P1score = self.p1.score
        P2score = self.p2.score
        Pname_txt = fonts.render(str(P1score), True, (229, 223, 69))
        self.canvas.get_screen().blit(Pname_txt, (890, 370))
        Pscore_txt = fonts.render(str(P2score), True, (229, 223, 69))
        self.canvas.get_screen().blit(Pscore_txt, (900, 370))
        help_txt = fonts.render("Press '3' to return", True, (165, 7, 31))
        self.canvas.get_screen().blit(help_txt, (1020, 572))

        pygame.display.update()

    def first_surface(self):
        game_over = False

        self.canvas.get_screen().fill((36, 37, 81))

        geistes_img = pygame.image.load('./images/img/Geistesblitz-5-vor-12(2).jpg')
        self.canvas.get_screen().blit(geistes_img, (0, 0))
        game_img = pygame.image.load('./images/img/71xM7BosVRL.jpg')
        self.canvas.get_screen().blit(game_img, (775, 0))

        fonts = self.font(25)
        pygame.draw.rect(self.canvas.get_screen(), (178, 136, 178), (780, 215, 250, 70), 0)
        help_txt = fonts.render("Press '1' for help", True, (165, 7, 31))
        self.canvas.get_screen().blit(help_txt, (800, 237))

        pygame.draw.rect(self.canvas.get_screen(), (178, 136, 178), (1040, 215, 300, 70), 0)
        high_score_txt = fonts.render("Press '2' for high score", True, (165, 7, 31))
        self.canvas.get_screen().blit(high_score_txt, (1050, 237))

        bigFont = self.font(35)
        name_txt = bigFont.render("Enter Your Name", True, (229, 223, 69))
        self.canvas.get_screen().blit(name_txt, (920, 370))
        text_name = ""
        input_active = True
        pygame.draw.rect(self.canvas.get_screen(), (255, 255, 255), (900, 430, 250, 50), 0)

        fonts1 = self.font(17)
        pygame.draw.rect(self.canvas.get_screen(), (178, 136, 178), (1180, 680, 150, 45), 0)
        exit_txt = fonts1.render("Press '5' to exit", True, (165, 7, 31))
        self.canvas.get_screen().blit(exit_txt, (1190, 695))

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    input_active = True
                    text_name = ""
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.help_surface()
                    elif event.key == pygame.K_2:
                        self.score_surface()
                    elif event.key == pygame.K_3:
                        self.first_surface()
                    elif event.key == pygame.K_5:
                        game_over = True
                    elif event.key == pygame.K_SPACE:
                        self.show_obj()
                        self.run()
                    if input_active:
                        if event.key == pygame.K_RETURN:
                            input_active = False
                        elif event.key == pygame.K_BACKSPACE:
                            text_name = text_name[:-1]
                        else:
                            text_name += event.unicode
                text_sur = fonts.render(text_name, True, (0, 0, 0))
                self.canvas.get_screen().blit(text_sur, (910, 440))
                pygame.display.flip()

            pygame.display.update()
        pygame.quit()
        quit()


class Player:
    def __init__(self, ID_cart):
        self.cartID = ID_cart
        self.win = False
        self.move = ''
        self.score = 0

    def play(self, pressed_key):
        if pressed_key == 'a':
            self.move = 'a'
        elif pressed_key == 'b':
            self.move = 'b'
        elif pressed_key == 'c':
            self.move = 'c'
        elif pressed_key == 'd':
            self.move = 'd'
        elif pressed_key == 'e':
            self.move = 'e'
        elif pressed_key == 'f':
            self.move = 'f'
        elif pressed_key == 'g':
            self.move = 'g'
        elif pressed_key == 'h':
            self.move = 'h'
        elif pressed_key == 'i':
            self.move = 'i'

    def draw(self, screen, cart_list,):
        cart_name = str(cart_list[int(self.cartID)]) + ".jpg"
        cart = pygame.image.load("./images/carts/small/" + cart_name)
        pygame.display.flip()
        screen.blit(cart, (350, 250))


class Canvas:
    def __init__(self, screenWidth, screenHeight):
        pygame.init()
        self.screen = pygame.display.set_mode((screenWidth, screenHeight))
        pygame.display.set_caption("GEISTES")

    @staticmethod
    def update():
        pygame.display.update()

    def get_screen(self):
        return self.screen

