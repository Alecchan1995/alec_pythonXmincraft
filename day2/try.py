from mcpi.minecraft import Minecraft as mc
mcs = mc.create()
x,y,z=mcs.player.getPos()
mcs.setSign(x,y,z,68,0,'hihi')