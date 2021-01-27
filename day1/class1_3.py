from mcpi.minecraft import Minecraft as mc
mcs = mc.create()
print(mcs.player.getTilePos())
x,y,z = mcs.player.getPos()
print(x,y,z)
