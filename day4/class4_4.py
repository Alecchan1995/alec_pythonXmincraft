from mcpi.minecraft import *
import time
mc = Minecraft.create()
while True:
   time.sleep(0.5)
   mc.executeCommand("time add 100")