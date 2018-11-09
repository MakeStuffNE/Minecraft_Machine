from gpiozero import LED
from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()
bulb = LED(7)

bulb.off()
sleep(1)

mc.postToChat("Hello Maker!")
sleep(3)
mc.postToChat("Bulb's turn electricity into light.")
sleep(3)
mc.postToChat("But this bulb is controlled by Steve's position.")
sleep(3)
mc.postToChat("Find your way to 0 on the x axis to switch it on!")
sleep(3)
mc.postToChat("Your position on the x axis is the number in the top left ;-)")
sleep(3)
mc.postToChat("Good Luck!")

while True:
    x = mc.player.getPos().x
    y = mc.player.getPos().y
    z = mc.player.getPos().z
    if -1 < x < 1:
        bulb.on()
    else :
        bulb.off()
