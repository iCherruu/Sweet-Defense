import pygame

class Customer:
    imgs = []
    
    def __init__(self, x, y):
        self.width = 48
        self.height = 48
        self.imgs = []
        self.animation_count = 0
        self.hp = 1
        self.speed = 3
        self.path = [(15, 686), (210, 657), (379, 643), (935, 641), (1071, 530), (1155, 423), (1168, 245), (1069, 160), (1007, 133), (813, 138), (702, 171), (601, 237), (531, 377), (536, 459), (618, 526), (678, 516), (743, 454), (748, 365), (678, 234), (551, 157), (418, 129), (310, 134), (177, 176), (118, 253), (109, 383), (164, 471), (290, 593), (422, 642), (976, 646), (1140, 671), (1275, 687)]
        self.pos = 0
        self.img = None
        self.move = 0
        self.trav_dis = 0
        self.dis = 0
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        

    def draw(self, win):
        self.animation_count += 1
        self.img = self.imgs[self.animation_count]
        
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0
            
        window.blit(self.img, (self.x, self.y))
        self.move()

    def collide(self, x, y):
        if x <= self.x + self.width and x >= self.x:
            if y <= self.y + self.height and y >= self.y:
                return True
        return False

    def move(self):
        x1, y1 = self.path(self.pos)
        if self.pos + 1 >= len(self.path):
            x2, y2 = (1400, 687)
        else:
            x2, y2 = self.path(self.pos + 1)

            distance = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
        # May need more math
        self.move += 1
        direction = (x2-x1, y2-y1)

        x_move, y_move = (self.x + direction[0] * self.move, self.y + direction[1] * self.move)
        self.dis += (((x_move-x1)**2 + (y_move-y1)**2)**(1/2))

        if self.trav_dis >= distance:
            self.trav_dis = 0
            self.move = 0
            self.pos += 1

        self.x = x_move
        self.y = y_move

    def hit(self):
        self.health -= 1
        if self.health <= 0:
            return True
    
