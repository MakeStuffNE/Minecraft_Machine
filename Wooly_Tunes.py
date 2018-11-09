import RPi.GPIO as GPIO
from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT)
pulse = GPIO.PWM(21,300)

x = mc.player.getPos().x
y = mc.player.getPos().y
z = mc.player.getPos().z

mc.setBlocks(x+1, y-1, z+1,x+6, y-1, z+6,1)
mc.setBlocks(x+1, y-1, z+7,x+6, y-1, z+13,3)
mc.setBlocks(x+1, y-1, z+14,x+6, y-1, z+20,4)
mc.setBlocks(x+1, y-1, z+21,x+6, y-1, z+27,7)
mc.setBlocks(x+1, y-1, z+27,x+6, y-1, z+33,24)
mc.setBlocks(x+1, y-1, z+33,x+6, y-1, z+39,41)
mc.setBlocks(x+1, y-1, z+40,x+6, y-1, z+46,42)
mc.setBlocks(x+1, y-1, z+47,x+6, y-1, z+53,48)

mc.postToChat("Hello Maker!")
sleep(3)
mc.postToChat("Buzzers covert electricity into sound.")
sleep(3)
mc.postToChat("This Buzzer is controlled by blocks!")
sleep(3)
mc.postToChat("When you walk on different blocks...")
sleep(3)
mc.postToChat("The buzzer will play different tones.")
sleep(3)
mc.postToChat("Good Luck!")

while True:
    x = mc.player.getPos().x
    y = mc.player.getPos().y-1
    z = mc.player.getPos().z
    block_under = mc.getBlock(x,y,z)
    if block_under == 1:
        pulse = GPIO.PWM(21,262)
        pulse.start(50)
        sleep(0.2)
        pulse.stop()
    elif block_under == 3:
        pulse = GPIO.PWM(21,294)
        pulse.start(50)
        sleep(0.2)
        pulse.stop()
    elif block_under == 4:
        pulse = GPIO.PWM(21,330)
        pulse.start(50)
        sleep(0.2)
        pulse.stop()
    elif mc.getBlock(x,y-1,z) == 7:
        pulse = GPIO.PWM(21,349)
        pulse.start(50)
        sleep(0.2)
        pulse.stop()
    elif mc.getBlock(x,y-1,z) == 24:
        pulse = GPIO.PWM(21,393)
        pulse.start(50)
        sleep(0.2)
        pulse.stop()
    elif mc.getBlock(x,y-1,z) == 41:
        pulse = GPIO.PWM(21,440)
        pulse.start(50)
        sleep(0.2)
        pulse.stop()
    elif mc.getBlock(x,y-1,z) == 42:
        pulse = GPIO.PWM(21,494)
        pulse.start(50)
        sleep(0.2)
        pulse.stop()
    elif mc.getBlock(x,y-1,z) == 48:
        pulse = GPIO.PWM(21,523)
        pulse.start(50)
        sleep(0.2)
        pulse.stop()
    else :
        pulse = GPIO.PWM(21,262)
        pulse.start(50)
        sleep(0.2)
        pulse.stop()
