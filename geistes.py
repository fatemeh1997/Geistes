import pygame
import random
import time
from network import Network


class Geistes:
    def __init__(self):
        pygame.init()
        self.screenWidth = 1366
        self.screenHeight = 768
        self.high_scores = {}
        self.high_score_index = 0
        self.net = Network()
        self.response = ''
        self.win = False

        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        pygame.display.set_caption("GEISTES")

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
        self.screen.fill((52, 77, 105))

        fonts = self.font(25)
        description = pygame.image.load('./images/img/description.png')
        self.screen.blit(description, (160, 80))
        pygame.draw.rect(self.screen, (178, 136, 178), (1000, 550, 250, 70), 0)
        help_txt = fonts.render("Press '3' to return", True, (165, 7, 31))
        self.screen.blit(help_txt, (1020, 572))

        pygame.display.update()

    def score_surface(self):
        self.screen.fill((36, 37, 81))

        fonts = self.font(25)
        pygame.draw.rect(self.screen, (178, 136, 178), (1000, 600, 250, 70), 0)
        help_txt = fonts.render("Press '3' to return", True, (165, 7, 31))
        self.screen.blit(help_txt, (1020, 622))

        pygame.display.update()

    def show_obj(self):
        letter_font = self.font(30)
        self.screen.fill((141, 219, 205))
        flashlight = pygame.image.load('./images/objects/light.jpg')
        self.screen.blit(flashlight, (80, 150))
        pygame.draw.circle(self.screen, (36, 37, 81), (80, 294), 20, 0)
        a = letter_font.render('a', True, (255, 255, 255))
        self.screen.blit(a, (71, 278))

        clock = pygame.image.load('./images/objects/time.jpg')
        self.screen.blit(clock, (280, 50))
        pygame.draw.circle(self.screen, (36, 37, 81), (280, 218), 20, 0)
        b = letter_font.render('b', True, (255, 255, 255))
        self.screen.blit(b, (271, 204))

        hat = pygame.image.load('./images/objects/hatt.jpg')
        self.screen.blit(hat, (480, 50))
        pygame.draw.circle(self.screen, (36, 37, 81), (480, 209), 20, 0)
        c = letter_font.render('c', True, (255, 255, 255))
        self.screen.blit(c, (471, 193))

        owl = pygame.image.load('./images/objects/owl.jpg')
        self.screen.blit(owl, (670, 150))
        pygame.draw.circle(self.screen, (36, 37, 81), (670, 288), 20, 0)
        d = letter_font.render('d', True, (255, 255, 255))
        self.screen.blit(d, (659, 273))

        key = pygame.image.load('./images/objects/keyy.jpg')
        self.screen.blit(key, (650, 318))
        pygame.draw.circle(self.screen, (36, 37, 81), (650, 464), 20, 0)
        e = letter_font.render('e', True, (255, 255, 255))
        self.screen.blit(e, (641, 448))

        bat = pygame.image.load('./images/objects/bat.jpg')
        self.screen.blit(bat, (100, 318))
        pygame.draw.circle(self.screen, (36, 37, 81), (100, 472), 20, 0)
        i = letter_font.render('i', True, (255, 255, 255))
        self.screen.blit(i, (96, 458))

        cruse = pygame.image.load('./images/objects/kozee.JPG')
        self.screen.blit(cruse, (150, 502))
        pygame.draw.circle(self.screen, (36, 37, 81), (150, 654), 20, 0)
        h = letter_font.render('h', True, (255, 255, 255))
        self.screen.blit(h, (141, 639))

        mirror = pygame.image.load('./images/objects/shadoww.jpg')
        self.screen.blit(mirror, (600, 502))
        pygame.draw.circle(self.screen, (36, 37, 81), (600, 637), 20, 0)
        f = letter_font.render('f', True, (255, 255, 255))
        self.screen.blit(f, (594, 623))

        shadow = pygame.image.load('./images/objects/mirror.jpg')
        self.screen.blit(shadow, (370, 530))
        pygame.draw.circle(self.screen, (36, 37, 81), (370, 675), 20, 0)
        g = letter_font.render('g', True, (255, 255, 255))
        self.screen.blit(g, (360, 657))

    def play(self):
        answers = ['e', 'c', 'i', 'b', 'd', 'f', 'a', 'd', 'f', 'a', 'a', 'c', 'c', 'd', 'h', 'f', 'g', 'd']
        cart_list = [5, 10, 13, 2, 14, 1, 17, 3, 6, 7, 4, 11, 16, 8, 9, 12, 15, 18]
        #InvTime = 10
        Tfont = self.font(70)
        #cart_list = self.mix()
        """pygame.draw.rect(self.screen, (141, 219, 205), (880, 50, 100, 150), 0)
        timer = Tfont.render(str(InvTime), True, (255, 0, 0))
        self.screen.blit(timer, (900, 50))
        pygame.display.flip()"""
        for i in range(len(cart_list)):
            """pygame.draw.rect(self.screen, (141, 219, 205), (850, 130, 200, 45), 0)
            pygame.display.flip()
            if i == 0:
                InvTime = 10
            else:
                InvTime = 11"""
            noResponse = True
            cart_name = str(cart_list[i]) + ".jpg"
            cart = pygame.image.load("./images/carts/small/"+cart_name)
            pygame.display.flip()
            self.screen.blit(cart, (350, 250))
            pygame.display.flip()
            while noResponse:
                time.sleep(1)
                """InvTime -= 1
                pygame.draw.rect(self.screen, (141, 219, 205), (880, 50, 100, 70), 0)
                pygame.display.flip()
                timer2 = Tfont.render(str(InvTime), True, (255, 0, 0))
                self.screen.blit(timer2, (900, 50))
                pygame.display.flip()"""
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            self.response = 'a'
                            if self.response == answers[cart_list[i] - 1]:
                                self.win = True
                                #InvTime = 10
                                noResponse = False
                                self.show_answer_result(True)
                            else:
                                self.show_answer_result(False)
                        if event.key == pygame.K_b:
                            self.response = 'b'
                            if self.response == answers[cart_list[i] - 1]:
                                self.win = True
                                #InvTime = 10
                                noResponse = False
                                self.show_answer_result(True)
                            else:
                                self.show_answer_result(False)
                        if event.key == pygame.K_c:
                            self.response = 'c'
                            if self.response == answers[cart_list[i] - 1]:
                                self.win = True
                                #InvTime = 10
                                noResponse = False
                                self.show_answer_result(True)
                            else:
                                self.show_answer_result(False)
                        if event.key == pygame.K_d:
                            self.response = 'd'
                            if self.response == answers[cart_list[i] - 1]:
                                self.win = True
                                #InvTime = 10
                                noResponse = False
                                self.show_answer_result(True)
                            else:
                                self.show_answer_result(False)
                        if event.key == pygame.K_e:
                            self.response = 'e'
                            if self.response == answers[cart_list[i] - 1]:
                                self.win = True
                                #InvTime = 10
                                noResponse = False
                                self.show_answer_result(True)
                            else:
                                self.show_answer_result(False)
                        if event.key == pygame.K_f:
                            self.response = 'f'
                            if self.response == answers[cart_list[i] - 1]:
                                self.win = True
                                #InvTime = 10
                                noResponse = False
                                self.show_answer_result(True)
                            else:
                                self.show_answer_result(False)
                        if event.key == pygame.K_g:
                            self.response = 'g'
                            if self.response == answers[cart_list[i] - 1]:
                                self.win = True
                                #InvTime = 10
                                noResponse = False
                                self.show_answer_result(True)
                            else:
                                self.show_answer_result(False)
                        if event.key == pygame.K_h:
                            self.response = 'h'
                            if self.response == answers[cart_list[i] - 1]:
                                self.win = True
                                #InvTime = 10
                                noResponse = False
                                self.show_answer_result(True)
                            else:
                                self.show_answer_result(False)
                        if event.key == pygame.K_i:
                            self.response = 'i'
                            if self.response == answers[cart_list[i] - 1]:
                                self.win = True
                                #InvTime = 10
                                noResponse = False
                                self.show_answer_result(True)
                            else:
                                self.show_answer_result(False)
        self.last_surface()

    def send_data(self):
        data = str(self.net.id) + ":" + self.response + ":" + str(self.win)
        self.net.send(data)
        self.win = False

    def show_answer_result(self, answer):
        Mfont = self.font(25)
        pygame.draw.rect(self.screen, (141, 219, 205), (850, 130, 200, 45), 0)
        pygame.display.flip()
        if answer:
            correct = Mfont.render('Correct Answer', True, (0, 0, 255))
        else:
            correct = Mfont.render('Wrong Answer', True, (0, 0, 255))
        self.screen.blit(correct, (860, 140))

    def last_surface(self):
        self.screen.fill((36, 37, 81))
        fonts = self.font(25)
        while self.high_score_index < len(self.high_scores):
            Pname = self.high_scores[self.high_score_index]
            Pscore = self.high_scores[self.high_score_index+1]
            Pname_txt = fonts.render(Pname, True, (229, 223, 69))
            self.screen.blit(Pname_txt, (890, 370))
            Pscore_txt = fonts.render(Pscore, True, (229, 223, 69))
            self.screen.blit(Pscore_txt, (900, 370))
        help_txt = fonts.render("Press '3' to return", True, (165, 7, 31))
        self.screen.blit(help_txt, (1020, 572))

        pygame.display.update()

    def first_surface(self):
        game_over = False

        self.screen.fill((36, 37, 81))

        geistes_img = pygame.image.load('./images/img/Geistesblitz-5-vor-12(2).jpg')
        self.screen.blit(geistes_img, (0, 0))
        game_img = pygame.image.load('./images/img/71xM7BosVRL.jpg')
        self.screen.blit(game_img, (775, 0))

        fonts = self.font(25)
        pygame.draw.rect(self.screen, (178, 136, 178), (780, 215, 250, 70), 0)
        help_txt = fonts.render("Press '1' for help", True, (165, 7, 31))
        self.screen.blit(help_txt, (800, 237))

        pygame.draw.rect(self.screen, (178, 136, 178), (1040, 215, 300, 70), 0)
        high_score_txt = fonts.render("Press '2' for high score", True, (165, 7, 31))
        self.screen.blit(high_score_txt, (1050, 237))

        bigFont = self.font(35)
        name_txt = bigFont.render("Enter Your Name", True, (229, 223, 69))
        self.screen.blit(name_txt, (890, 370))
        text_name = ""
        input_active = True
        pygame.draw.rect(self.screen, (255, 255, 255), (900, 430, 250, 50), 0)

        fonts1 = self.font(17)
        pygame.draw.rect(self.screen, (178, 136, 178), (1180, 680, 150, 45), 0)
        exit_txt = fonts1.render("Press '5' to exit", True, (165, 7, 31))
        self.screen.blit(exit_txt, (1190, 695))

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
                        self.play()
                    if input_active:
                        if event.key == pygame.K_RETURN:
                            input_active = False
                        elif event.key == pygame.K_BACKSPACE:
                            text_name = text_name[:-1]
                        else:
                            text_name += event.unicode
                """else:
                    name_txt = fonts.render("This name exists...", True, (229, 223, 69))
                    screen.blit(name_txt, (890, 370))
                    pygame.draw.rect(screen, (255, 255, 255), (900, 430, 250, 50), 0)"""
                text_sur = fonts.render(text_name, True, (0, 0, 0))
                self.screen.blit(text_sur, (910, 440))
                pygame.display.flip()

            pygame.display.update()
        pygame.quit()
        quit()

