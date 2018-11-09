from gpiozero import Button
from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

mc.postToChat("Hello Maker!")
sleep(3)
mc.postToChat("Switches can either be on or off...")
sleep(3)
mc.postToChat("One or Zero....")
sleep(3)
mc.postToChat("When you flick this switch...")
sleep(3)
mc.postToChat("You will create a block of TNT!")
sleep(3)
mc.postToChat("Good Luck!")


button = Button(2)
while True:
    x = mc.player.getPos().x
    y = mc.player.getPos().y
    z = mc.player.getPos().z
    button.wait_for_press()
    print("You Pushed Me")
    mc.setBlocks(x+1, y+1, z+1,x+6, y+6, z+6,46,1)
