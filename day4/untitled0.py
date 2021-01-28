from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
mc.setBlocks(x,y-1,z,x+100,y-1,z+100,1)