from mcpi.minecraft import Minecraft
from random import choice
import time 
time.sleep(5)
mc = Minecraft.create()
mineral = [14,15,16,56,73,129]
while True:
    time.sleep(1)
    r = choice(mineral)
    myID= mc.getPlayerEntityId("Coding_APE_002")
    x,y,z = mc.entity.getTilePos(myID)
    mc.setBlock(x,y,z,129)
