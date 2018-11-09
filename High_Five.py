from gpiozero import DistanceSensor
from mcpi.minecraft import Minecraft
from time import sleep

ultrasonic = DistanceSensor(echo=19, trigger=13)
mc = Minecraft.create()

mc.postToChat("Hello Maker!")
sleep(3)
mc.postToChat("Place your hand close to the distance sensor")
sleep(3)
mc.postToChat("Move it up and down.")
sleep(3)
mc.postToChat("I will tell you how far away it is.")
sleep(3)
mc.postToChat("And build a tower of the same height close to you.")
sleep(3)
mc.postToChat("Good Luck!")
         
while True:
    x = mc.player.getPos().x
    y = mc.player.getPos().y-1
    z = mc.player.getPos().z
    howFar = int(ultrasonic.distance * 100)
    print(howFar)
    for i in range(howFar):
        mc.setBlock(x+1, y+i, z+1, 13)
    mc.postToChat("Your hand is " + str(howFar) + " cm away")
    sleep(1)
    for i in range(howFar):
        mc.setBlock(x+1, y+i, z+1, 00)
    sleep(1)
