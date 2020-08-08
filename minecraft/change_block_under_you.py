from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

block_type = 5
air = 0

while True:
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    #print(x, y, z)
    #sleep(1)
    #mc.postToChat(pos)
    # mc.setBlock(x, y-1, z, block_type)
    mc.setBlocks(x - 2, y - 1, z - 2, x + 2, y - 1, z + 2, block_type)
    mc.setBlocks(x - 2, y, z - 2, x + 2, y + 3, z + 2, air)
