from mcpi.minecraft import Minecraft as mc
mcs = mc.create()
position = mcs.player.getTilePos()
x = position.x
print(x)
x,y,z = mcs.player.getPos()
print(x,y,z)
y=y-10
mcs.player.setPos(x,y,z)
