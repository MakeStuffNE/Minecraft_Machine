from gpiozero import MCP3008
from mcpi.minecraft import Minecraft
from time import sleep

pot = MCP3008(channel=1)
mc = Minecraft.create()

mc.postToChat("Hello Maker!")
sleep(3)
mc.postToChat("Potentiometers vary electrical resistance")
sleep(3)
mc.postToChat("They are like a volume control.")
sleep(3)
mc.postToChat("This one will control Steve's height.")
sleep(3)
mc.postToChat("Good Luck!")



while True:
    x = mc.player.getPos().x
    y = mc.player.getPos().y
    z = mc.player.getPos().z
    height = int(pot.value * 125)
    print (height)
    mc.player.setPos(x,height,z)
    sleep(2)
