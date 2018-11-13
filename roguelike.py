import curses
import random
import math
import time
from curses import wrapper
from character import plyr
from equip import equip
from time import sleep
from map import map
def main(scr):
    curses.curs_set(0)
    pc = plyr(10, 10, 10, 10, 10, 10, scr)
    curses.use_default_colors()
    scr.clear()
    floor = map(scr)

    floor.defmap()
    
#######################################################################################
############# PLAYER CHARACTER FUNCTIONS ##############################################
#######################################################################################

    a = equip(1)
    b = equip(2)
    c = equip(3)
    d = equip(5)
    e = equip(6)
    f = equip(7)

    pc.addinv(a)
    pc.addinv(b)
    pc.addinv(c)
    pc.addinv(d)
    pc.addinv(e)
    pc.addinv(f)
#####################################################################################
#################### RUNTIME ########################################################
#####################################################################################
    
    while True:
        if pc.xp > (pc.lvl * pc.lvl + 10):
            pc.lvlup()
        floor.full.refresh(pc.cords[0] - 12, pc.cords[1] - 25, 1, 1, 25, 50,)
        pc.run(floor.hostile, floor.impass)
        floor.draw(pc)
        
wrapper(main)
