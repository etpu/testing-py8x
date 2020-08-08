from mcpi.minecraft import Minecraft
import time

x = 4
y = 78  # Высота
z = 6
block_type = 0

mc = Minecraft.create()

# mc.player.setTilePos(x, y, z)
while True:
    mc.player.setTilePos(28, 74, 161)
    time.sleep(5)
    mc.player.setTilePos(56, 74, 208)
    time.sleep(5)
    mc.player.setTilePos(110, 89, 81)
    time.sleep(5)


# for i in range(20):
#     #time.sleep(1)
#     mc.setBlock(x, y:=y+1, z, block_type)
#
#
#
# while True:
#     xyz = mc.player.getTilePos()
#     # time.sleep(1)
#     print(xyz)
#     #a = f"{int(xyz.x)}, {int(xyz.y)}, {int(xyz.z)}"
#     #mc.postToChat(a)

