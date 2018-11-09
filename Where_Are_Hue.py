from gpiozero import PWMLED
from mcpi.minecraft import Minecraft
import random
from time import sleep
mc = Minecraft.create()

red = PWMLED(12)
green = PWMLED(16)
blue = PWMLED(20)

mc.postToChat("Hello Maker!")
sleep(3)
mc.postToChat("RGB LED's can create different coloured light")
sleep(3)
mc.postToChat("Get ready for a journey!")
sleep(3)
mc.postToChat("Steve is going to teleport to random positions in this world")
sleep(3)
mc.postToChat("When he gets there...")
sleep(3)
mc.postToChat("His position will control the colour of the LED.")
sleep(3)
mc.postToChat("Enjoy!")

while True:

    xred = random.randint(0,100)
    ygreen = random.randint(0,100)
    zblue = random.randint(0,100)
    
    mc.player.setPos(xred, ygreen, zblue)

    red.value = xred/100
    green.value = ygreen/100
    blue.value = zblue/100

    mc.postToChat("New Place, New Hue!!")

    sleep(5)
    
