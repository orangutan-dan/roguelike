import curses
from curses import wrapper

class plyr:
    def __init__(self, a, b, c, d, e, f, scr):
        self.lvl = 1
        self.strn = a
        self.end = b
        self.dex = c
        self.intl = d
        self.per = e
        self.luck = f
        
        self.inv = []

        self.xp = 0

        self.skills = {
                'guns' : int(round((self.dex + self.per) / 2)),
                'melee' : int(round((self.strn + self.dex) / 2)),
                'energy' : int(round((self.per + self.intl) / 2)),
                'unnarmed' : int(round((self.strn + self.end) / 2)),
                'sneak' : int(round((self.dex + self.per) / 2)),
                'tech' : int(round((self.intl + self.luck) / 2)),
                'mech' : int(round((self.per + self.intl) / 2)),
                'medicine' : int(round((self.intl + self.end) / 2))
                }
        
        self.cords = [30, 30]
        
        self.equipment = ["nothin'", "nothin'", "nothin'", "nothin'", "nothin'", "nothin'", "nothin'"]
        
        self.scr = scr

    def lvldrw(self):
        j = 0
        for i in range(30):
            for l in range(42):
                self.scr.addch(0 + i, 52 + l, ' ')
        for key, val in self.skills.items():
            j += 1
            self.scr.addstr(2 + j, 52, '[' + str(j) + '] ' + key + ': ' + str(val))
        self.scr.addstr(0, 52, 'LEVEL UP!')
        self.scr.addstr(1, 52,'press the number to increase your skills!')

    def lvlup(self):
        j = 0
        if self.xp > (self.lvl * self.lvl + 10):
            self.lvldrw()
            self.lvl += 1
            skillp = (10 + int(round(self.intl / 2)))
            self.scr.addstr(12, 52, 'points left: ' + str(skillp))
            for i in range(skillp):
                curses.flushinp()
                inp = self.scr.getch()
                if inp == ord('1'):
                    self.skills['guns'] += 1
                elif inp == ord('2'):
                    self.skills['melee'] += 1
                elif inp == ord('3'):
                    self.skills['energy'] += 1
                elif inp == ord('4'):
                    self.skills['unnarmed'] += 1
                elif inp == ord('5'):
                    self.skills['sneak'] += 1
                elif inp == ord('6'):
                    self.skills['tech'] += 1
                elif inp == ord('7'):
                    self.skills['mech'] += 1
                elif inp == ord('8'):
                    self.skills['medicine'] += 1
                self.lvldrw()
                self.scr.addstr(12, 52, 'points left: ' + str(skillp - (i + 1)))


        self.hp = self.lvl * self.end
        self.xp = 0
        for i in range(30):
            for l in range(42):
                self.scr.addch(0 + i, 52 + l, ' ')

    def getxp(self, x):
        self.xp += x
    
    def addinv(self, item):
        if len(self.inv) < 40:
            self.inv.append(item)
            return True
        else:
            self.scr.addstr(45, 52, "you're carrying too much!, drop something!")

    def invopen(self):
        org = 0
        nex = 0
        while True:
            for i in range(50):
                for l in range(55):
                    self.scr.addch(i, 52 + l, ' ')
            if len(self.inv) > 0:
                for i in range(len(self.inv)):
                    self.scr.addstr(i, 52, self.inv[i].name)
                self.scr.addstr(org, 52, self.inv[org].name, curses.A_BOLD)
                inp = self.scr.getch()
                if inp == ord('w'):
                    if org != 0:
                        org -= 1
                if inp == ord('s'):
                    if org != (len(self.inv) - 1):
                        org += 1
                if inp == ord('e'):
                    if self.inv[org].equipable == True:
                        if self.equip(self.inv[org]) == True:
                            self.inv.pop(org)
                        org = 0
                    else:
                        self.scr.addstr(org, 52, "can't equip that!", curses.A_BOLD)
                if inp == ord('u'):
                    if self.inv[org].usable == True:
                        self.use(self.inv[org])
                    else:
                        self.scr.addstr(org, 52, "can't use that!", curses.A_BOLD)
                if inp == ord('r'):
                    self.drop(self.inv[org])
                if inp == ord('d'):
                    nex = 1
                    break
                if inp == ord('x'):
                    for i in range(30):
                        for l in range(52):
                            self.scr.addch(0 + i, 52 + l, ' ')
                    break
            else:
                inp = self.scr.getch()
                self.scr.addstr(0, 52, 'well shoot, looks like your inventory is empty!')
                if inp == ord('d'):
                    nex = 1
                    break
                if inp == ord('x'):
                    for i in range(50):
                        for l in range(42):
                            self.scr.addch(0 + i, 52 + l, ' ')
                    break

        if nex == 1:
            self.eqopen()

    def eqopen(self):
        org = 0
        prev = 0
        asd = ['Head:   ', 'Body:   ', 'Arms:   ', 'Legs:   ', 'Feet:   ', 'Melee:  ', 'Ranged: ']
        while True:
            for i in range(50):
                for l in range(60):
                    self.scr.addch(i, 52 + l, ' ')
            for i in range(len(self.equipment)):
                if self.equipment[i] == "nothin'":
                    self.scr.addstr(i, 52, (asd[i] + self.equipment[i]))
                else:
                    self.scr.addstr(i, 52, (asd[i] + self.equipment[i].name))
            self.scr.addstr(8, 52, ('Armor Value: [' + str(self.armorval()) + ', ' + str(self.dodgeval()) + ']'))
            if self.equipment[org] == "nothin'":
                self.scr.addstr(org, 52, (asd[org] + self.equipment[org]), curses.A_BOLD)
            else:
                self.scr.addstr(org, 52, (asd[org] + self.equipment[org].name), curses.A_BOLD)
            inp = self.scr.getch()
            if inp == ord('w'):
                if org != 0:
                    org -= 1
            if inp == ord('s'):
                if org != (len(self.equipment) - 1):
                    org += 1
            if inp == ord('a'):
                prev = 1
                break
            if inp == ord('e'):
                if self.equipment[org] == "nothin'":
                    self.scr.addstr(org, 52, "can't unequip what isn't there!", curses.A_BOLD)
                else:
                    if self.addinv(self.equipment[org]) == True:
                        self.equipment[org] = "nothin'"
            if inp == ord('x'):
                for i in range(50):
                    for l in range(65):
                        self.scr.addch(i, 52 + l, ' ')
                break
        if prev == 1:
            self.invopen()

    def equip(self, a):
        if a.type == 'head':
            if self.equipment[0] == "nothin'":
                self.equipment[0] = a
                return True
            else:
                self.scr.addstr(45, 52, "you've got something equiped there already!")
        
        elif a.type == 'body':
            if self.equipment[1] == "nothin'":
                self.equipment[1] = a
                return True
            else:
                self.scr.addstr(45, 52, "you've got something equiped there already!")
        
        elif a.type == 'arms':
            if self.equipment[2] == "nothin'":
                self.equipment[2] = a
                return True
            else:
                self.scr.addstr(45, 52, "you've got something equiped there already!")
        
        elif a.type == 'legs':
            if self.equipment[3] == "nothin'":
                self.equipment[3] = a
                return True
            else:
                self.scr.addstr(45, 52, "you've got something equiped there already!")
        
        elif a.type == 'feet':
            if self.equipment[4] == "nothin'":
                self.equipment[4] = a
                return True
            else:
                self.scr.addstr(45, 52, "you've got something equiped there already!")
        
        elif a.type == 'close':
            if self.equipment[5] == "nothin'":
                self.equipment[5] = a
                return True
            else:
                self.scr.addstr(45, 52, "you've got something equiped there already!")
        
        elif a.type == 'ranged':
            if self.equipment[6] == "nothin'":
                self.equipment[6] = a
                return True
            else:
                self.scr.addstr(45, 52, "you've got something equiped there already!")

    def armorval(self):
        x = 0
        for i in self.equipment:
            if i != "nothin'":
                if i.super == 'armor':
                    x += i.deff
        return x

    def dodgeval(self):
        x = 0
        for i in self.equipment:
            if i != "nothin'":
                if i.super == 'armor':
                    x += i.dodg
        return x
    

    def run(self, h, i):
        old = [self.cords[0], self.cords[1]]
        curses.flushinp()
        inp = self.scr.getch()
        if inp == ord('w'):
            self.cords[0] -= 1
        elif inp == ord('d'):
            self.cords[1] += 1
        elif inp == ord('s'):
            self.cords[0] += 1
        elif inp == ord('a'):
            self.cords[1] -= 1
        elif inp == ord('i'):
            self.invopen()
        elif inp == ord('e'):
            self.eqopen()

        if self.cords in h:
            self.cords = old
            
        if self.cords in i:
            self.cords = old
        

        

