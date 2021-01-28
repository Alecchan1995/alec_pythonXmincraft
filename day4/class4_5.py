from mcpi.minecraft import Minecraft
from random import randint
import time
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
com = randint(0,15)
chance = 5
for i in range(20):
    for j in range(20):
        color = randint(0,15)
        mc.setBlock(x+i,y-1,z+j,35,color)
while chance != 0 :
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        hit = hits[0]
        block = mc.getBlockWithData(hit.pos)
        data = block.data
        if data == com:
            mc.postToChat("You are Win")
            break
        else:
            chance = chance - 1
            mc.postToChat("You have "+str(chance)+". Please try again")
            if chance == 0:
                mc.postToChat("You are Loser")