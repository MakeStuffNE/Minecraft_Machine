from gpiozero import LightSensor
from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()
ldr = LightSensor(26)  

mc.postToChat("Hello Maker!")
sleep(3)
mc.postToChat("Cover the Light Sensor with you hand...")
sleep(3)
mc.postToChat("This will make Steve's world dark.")
sleep(3)
mc.postToChat("Have a try!")

while True:
    x = mc.player.getPos().x
    y = mc.player.getPos().y
    z = mc.player.getPos().z
    print(ldr.value)

    if ldr.value == 0.0:
        mc.setBlocks(x-3, y-3, z-3,x+3, y+3, z+3,1)
        mc.setBlocks(x-2, y-2, z-2,x+2, y+2, z+2,0)
        mc.postToChat("Whoah....It's Dark!!!")
        sleep(1)
    else:

        mc.setBlocks(x-3, y-3, z-3,x+3, y+3, z+3,0)
        mc.postToChat("Bright Light!")
        sleep(1)
