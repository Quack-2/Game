import pygame as pyg

class Manager(object):
    def __init__(self):
        pyg.init()
        self.width = 960
        self.length = 600
        self.screen = pyg.display.set_mode((self.width,self.length))
        self.run = True
        self.clock = pyg.time.Clock()
        self.font = pyg.font.SysFont('Ariel',30)
        self.counter = 10
        self.text = '10'.rjust(3)
        pyg.time.set_timer(pyg.USEREVENT,1000)
        self.green_grass_1 = pyg.image.load('Picture/Green_grass_1.png')
        self.red_player_front = pyg.image.load('Picture/Red_player_front.png')
        self.red_player_back = pyg.image.load('Picture/Red_player_back.png')
        #player position
        self.red_x = 0
        self.red_y = 0
        self.status_list = ['Down','Up','Left','Right']
        self.status = 'Down'

    def mainscreen(self):
        self.background()
        if self.status == self.status_list[0]:
            self.screen.blit(self.red_player_front, (self.red_x, self.red_y))
        if self.status == self.status_list[1]:
            self.screen.blit(self.red_player_back, (self.red_x, self.red_y))

    def timer(self):
        self.screen.blit(self.font.render(self.text, True, (0, 0, 0)), (32, 48))

    def background(self):
        for i in range(48):
            for j in range(30):
                self.screen.blit(self.green_grass_1,(i*20,j*20))

    def main(self):
        while self.run == True:
            self.mainscreen()
            pyg.display.update()
            self.clock.tick(60)
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    self.run = False
                if event.type == pyg.USEREVENT:
                    self.counter -= 1
                    self.text = str(self.counter).rjust(3)
                if event.type == pyg.KEYDOWN:
                    if event.key == pyg.K_DOWN:
                        if self.red_y + 10 <= 560:
                            self.red_y += 10
                            self.status = 'Down'
                    if event.key == pyg.K_UP:
                        if self.red_y - 10 >= 0:
                            self.red_y -=10
                            self.status = 'Up'
                    if event.key == pyg.K_RIGHT:
                        if self.red_x + 10 <= 560:
                            self.red_x += 10
                            self.status = 'Right'
                    if event.key == pyg.K_LEFT:
                        if self.red_x - 10 >= 0:
                            self.red_x -=10
                            self.status = 'Left'


Manager1 = Manager()
Manager1.main()