from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    hits = mc.events.pollBlockHits() # Used to Sword
    if len(hits) > 0 :
        print(hits)
        print(len(hits))
        print(type(hits))
        #hit = hits[0]
        #x,y,z = hit.pos.x,hit.pos.y,hit.pos.z
        #block = mc.getBlock(x,y,z)
        #print(block)"""