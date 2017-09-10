##################################
# The SpyRover class is a child to the RRB3 class.
# The RRB3 class was created by Simon Monk and can be downloaded at the link below:
# https://github.com/simonmonk/raspirobotboard3/blob/master/python/rrb3.py
#
# This class supports the functionality of the SpyRoverGUI support module.
#
# Author- Aaron Safran
##################################

from rrb3 import*


class SpyRover(RRB3):

    canMove = False
    LED_state = False
    motor_speed = 0.4
    half_speed = motor_speed/2
    
    def __init__(self):
        RRB3.__init__(self)
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18,GPIO.OUT)

    def getcanMove(self):
        return self.canMove

    def setcanMove(self, canMove):
        self.canMove = canMove

    def getMotor_speed(self):
        return self.motor_speed

    def setMotor_speed(self, motor_speed):
        self.motor_speed = motor_speed
        self.half_speed = motor_speed/2

    def getHalf_speed(self):
        return self.half_speed

    def getLED_State(self):
        return self.LED_state

    # LED must be properly connected to RasPi pin 18 for setLEDState() to turn it on and off
    # !!! Make sure to use a resistor when powering LED with RasPi !!!
    # Go to this link for tutorial: https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins
    def setLED_State(self, LED_state):
        if (LED_state == True):
            self.LED_state = LED_state
            GPIO.output(18,GPIO.HIGH)
        else:
            self.LED_state = LED_state
            GPIO.output(18,GPIO.LOW)
            
