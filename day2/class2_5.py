from mcpi.minecraft import Minecraft as mc
import time
mcs = mc.create()
x,y,z=mcs.player.getTilePos()
a = mcs.getBlock(x+1,y-1,z)
b = mcs.getBlock(x-1,y-1,z)
c = mcs.getBlock(x,y-1,z+1)
d = mcs.getBlock(x,y-1,z-1)
if a == 8 or a == 9 or b == 8 or b == 9 \
    or c == 8 or c == 9 or d == 8 or d == 9:
    mcs.setBlocks(x+1,y-1,z+1,x-1,y-1,z-1,20)
