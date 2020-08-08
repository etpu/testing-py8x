from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

block_type = 5
air = 0

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

mc.setBlocks(x - 20, y - 1, z - 5, x - 2, y + 6, z + 5, block_type)
mc.setBlocks(x - 19, y , z - 4, x - 3, y + 5, z + 4, air)
mc.setBlock(x-2, y, z, air)
mc.setBlock(x-2, y+1, z, air)
# mc.setBlocks(x - 2, y, z - 2, x + 2, y + 3, z + 2, air)