from mcpi.minecraft import Minecraft
mc = Minecraft.create()
myID = mc.getPlayerEntityId("Coding_APE_002")
#mc.postToTitle(myID,"Hello")
print( mc.entity.getTilePos(myID))

