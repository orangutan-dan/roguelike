import random
import math

class equip:
    def __init__(self, lvl):
        self.equipable = True
        guns = [['machine gun', 12, -5, -2], ['shotgun', 5, -2, -2], ['revolver', 3, 5, -5], ['sniper rifle', 2, 5, -4], ['anti-material rifle', 1, 8, -5]]
        melee = [['knife', 4, 3, 2], ['baseball bat', 6, 3, 6], ['longsword', 3, 5, 4], ['katana', 2, 8, 3], ['chainsword', 8, 5, 8]]
        energy = [['laser repeater', 5, 2, -5], ['plasma rifle', 2, 4, -4], ['beam-laser', 6, -6, 1], ['plasma caster', 10, -6, 1], ['KRZ-320', 1, 8, -5]]
        unnarmed = [['hand wraps', 3, 3, 3], ['boxing gloves',4, -1, 10], ['brass knuckles', 2, 6, 5], ['power fist', 1, 3, 5], ['"handsaw"', 10, 5, 8]]
        head = [['ballcap', 0, 2], ['balaclava', 1, 1], ['helmet', 3, -1], ['power helm', 6, -2], ['digi-tech facemask', 4, 4]]
        body = [['t-shirt', 0, 2], ['lite-armor', 6, 1], ['riot gear', 10, -3], ['sneaking suit', 4, 4], ['power armor', 13, -4]]
        arms = [['arm wraps', 0, 2], ['lite armgaurds', 3, 1], ['nanocloth sleeves', 2, 2], ['power-pauldrons', 5, -2], ['power-glove', 2, 3]]
        legs = [['jeans', 0, 2], ['kneepads', 3, 1], ['nanocloth leggings', 2, 3], ['power legs', 5, -2], ['rave pants', 2, 4]]
        feet = [['converse', 0, 2], ['combat boots', 1, 2], ['nanocloth boots', 2, 2], ['yeezy boosts', 2, 4], ['power boots', 4, 0]]
        weapons = [guns, melee, energy, unnarmed]
        gear = [head, body, arms, legs, feet]
        all = [weapons, gear]
        materials = {
                'Paper' : [-4, -2, 0],
                'Cloth' : [-3, 0, 1],
                'Plasticine' : [-1, 0, 3],
                'Glass' : [-3, 0, 1],
                'Leather' : [-2, 0, 2],
                'Alluminum' : [-1, 1, 1],
                'Iron' : [-1, 3, -5],
                'Steel' : [0, 5, -3],
                'Digitized' : [4, 3, 4],
                'Carbon Fibre' : [2, 5, 0],
                'Nu-Alloy' : [3, 3, 3],
                'Adamantium' : [4, 9, -4],
                'Uranium-Plate' : [3, 7, -5],
                'Diamondoid' : [3, 7, -4]
                }
        
        self.mat = random.choice(list(materials))
        self.clas = random.choice(random.choice(random.choice(all)))

        ########defining lvl, important variable for other calcs

        self.lvl = int(round(lvl + materials[self.mat][0] + random.randrange(-(math.ceil(lvl / 2)), math.ceil(lvl / 2))))
        if self.lvl < 1:
            self.lvl = 1
        ########defining attribs for weapons

        if (((self.clas in guns) or (self.clas in energy)) or ((self.clas in melee) or (self.clas in unnarmed))):
            
            self.super = 'weapon'

            #dice choosin'

            self.amt = self.clas[1]
            self.sides =  int(math.ceil((self.lvl * (self.lvl / 2)) / (int(math.ceil(self.clas[1] / 2)) * int(math.ceil(self.lvl / 2)))))
            
            if self.sides < 1:
                self.sides = 1
            
            #modifyer choosin

            self.hit = self.clas[3] + materials[self.mat][2] + random.randrange(-3, int(round(self.lvl / 5)))
            self.dm = self.clas[2] + materials[self.mat][1] + random.randrange(-3, int(round(self.lvl / 5)))
            
            #definin the name

            self.name =  self.mat + ' ' + self.clas[0] + ' ' + str(self.amt) + 'd' + str(self.sides) + ' [' + str(self.dm) + ', ' +  str(self.hit) + ']'
            
            
            if (self.clas in guns) or (self.clas in energy):
                self.type = 'ranged'
            else:
                self.type = 'close'
        
        else:
            self.super = 'armor'
            
            if self.clas in head:
                self.type = 'head'
            elif self.clas in body:
                self.type = 'body'
            elif self.clas in arms:
                self.type = 'arms'
            elif self.clas in legs:
                self.type = 'legs'
            elif self.clas in feet:
                self.type = 'feet'

            self.deff = self.clas[1] + materials[self.mat][1] + random.randrange(-3, int(round(self.lvl / 5)))
            self.dodg = self.clas[2] + materials[self.mat][2] + random.randrange(-3, int(round(self.lvl / 5)))
            
            self.name =  self.mat + ' ' + self.clas[0] + ' [' + str(self.deff) + ', ' +  str(self.dodg) + ']'
                
            #returnin a damage amount
    def damage(self):
        full = 0
        for i in range(self.amt):
            full += random.randrange(1, (self.sides + 1))
        full += self.dm
        return full
                

                
