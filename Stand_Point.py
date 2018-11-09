from gpiozero import Servo
from mcpi.minecraft import Minecraft
from time import sleep


mc = Minecraft.create()
servo = Servo(14)

mc.postToChat("Hello Maker!")
sleep(3)
mc.postToChat("Servo's can point in different positions")
sleep(3)
mc.postToChat("Where Steve is controls our servo.")
sleep(3)
mc.postToChat("If he is on Dirt, it points one way...")
sleep(3)
mc.postToChat("if he is on Air, it points another way...")
sleep(3)
mc.postToChat("for any other block it will point a third way.")
sleep(3)
mc.postToChat("Have a try!")

while True:
     x = mc.player.getPos().x
     y = mc.player.getPos().y-1
     z = mc.player.getPos().z
     block_under = mc.getBlock(x,y-1,z)
     if mc.getBlock(x,y-1,z) == 0:
        servo.mid()
        print(block_under)
        print("air")
        sleep(0.5)
     elif mc.getBlock(x,y-1,z) == 3:
        servo.min()
        print(block_under)
        print("Dirt")
        sleep(0.5)
     else:
        servo.max()
        print(block_under)
        print("Neither Grass nor Air")
        sleep(0.5)
