import curses
import random
class map:
    def __init__(self, scr):
    
        self.scr = scr
        self.hostile = []
        self.tiles = []
        self.impass = []
        self.poi = []
        self.full = curses.newpad(101, 101)
    def defmap(self):
        for x in range(100):
            for y in range(100):
                if x == 0:
                    self.tiles.append([y, x, '#'])
                    self.impass.append([y, x])
                elif y == 0:
                    self.tiles.append([y, x, '#'])
                    self.impass.append([y, x])
                elif x == 99:
                    self.tiles.append([y, x, '#'])
                    self.impass.append([y, x])
                elif y == 99:
                    self.tiles.append([y, x, '#'])
                    self.impass.append([y, x])
                else:
                    o = random.choice([' ', "'", ' ', ' ', ' ', ' ', ' ', ',', '.'])
                    self.tiles.append([y, x, o])

    def draw(self, pc):
        for i in range(len(self.tiles)):
            self.full.addch(self.tiles[i][0], self.tiles[i][1], self.tiles[i][2])
        self.full.addch(pc.cords[0], pc.cords[1], '@', curses.A_BOLD)
        for x in range(52):
            for y in range(27):
                if x == 0 and y == 0:
                    self.scr.addch(y, x, '+')
                elif x == 0 and y == 26:
                    self.scr.addch(y, x, '+')
                elif x == 51 and y == 0:
                    self.scr.addch(y, x, '+')
                elif x == 51 and y == 26:
                    self.scr.addch(y, x, '+')
                elif x == 0 or x == 51:
                    self.scr.addch(y, x, '|')
                elif y == 0 or y == 26:
                    self.scr.addch(y, x, '-')
        self.scr.refresh()
        self.full.refresh(pc.cords[0] - 12, pc.cords[1] - 25, 1, 1, 25, 50,)
        curses.doupdate()
