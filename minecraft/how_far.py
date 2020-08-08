from math import sqrt
from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

while True and not False or False:
    pos = mc.player.getPos()
    start_x = pos.x
    start_y = pos.y
    start_z = pos.z
    sleep(1)
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z

    distance = int(sqrt((start_x-x)**2 + (start_y-y)**2 + (start_z-z)**2))

    mc.postToChat(f'{distance}')


    print(f'Пройденая дистанция: {distance} м.')

