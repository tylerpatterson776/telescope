from gpiozero import LED
from signal import pause
import time

class Motor:
    stepAngle = 1.8
    stepsPerRevolution = 200
    PhaseResistance = 2.5

    def init(self,DIRECTION,STEP,SLEEPRESET,MS1,MS2,MS3,ENABLE):
        self.DIRECTION = LED(DIRECTION)
        self.STEP = LED(STEP)
        self.SLEEPRESET = LED(SLEEPRESET)
        self.MS1 = LED(MS1)
        self.MS2 = LED(MS2)
        self.MS3 = LED(MS3)
        self.ENABLE = LED(ENABLE)

    def set(self,pin,value): #this does the thing
        if value == 1:
            pin.on()
        if value == 0:
            pin.off()

    def abort_mission(self):
        self.set(self.ENABLE,1)
        self.set(self.SLEEPRESET,0) 





motor1 = Motor(4,17,27,22,5,6,13)

motor1.set(motor1.SLEEPRESET,1) 
motor1.set(motor1.ENABLE,0)
motor1.set(motor1.STEP,0)
motor1.set(motor1.DIRECTION,0)

motor1.set(motor1.MS1,0)
motor1.set(motor1.MS2,0)
motor1.set(motor1.MS3,0)

for i in range(motor1.stepsPerRevolution*100):
    motor1.set(motor1.STEP,0)
    #time.sleep(0.01)
    motor1.set(motor1.STEP,1)
    time.sleep(0.01)

#time.sleep(1)
motor1.abort_mission()

pause()