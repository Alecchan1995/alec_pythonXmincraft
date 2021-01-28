while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        hit = hits[0]
        block = mc.getBlockWithData(hit.pos)
        data = block.data
        if data == com:
            mc.postToChat("You are good")
            break
        else:
            mc.postToChat("Try again")