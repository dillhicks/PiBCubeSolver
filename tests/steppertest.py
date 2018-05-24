from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
from Adafruit_PWM_Servo_Driver
import time
import atexit



# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
        mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
	pwm.set_pwm(channel, 0, pulse)

#setting up servos 
servo = Adafruit_PCA9685.PCA9685()

servomin = 150
servo_max = 600

servo.set_pwm_freq(60)


#setting up stepper motors
step = Adafruit_MotorHAT(addr = 0x60)

rightStep = mh.getStepper(200, 1)
leftStep = mh.getStepper(200,2)

rightStep.setSpeed(60)
leftStep.setSpeed(60)

rightServo1 = 0
rightServo2 = 1

leftServo1 = 2
leftServo2 = 3




'''
EXAMPLES TO MOVE BACK AND FORTH

For a stepper: 
rightStep.step(100, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)
rightStep.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)

For a servo
pwm.set_pwm(0,0,servo_min)
pwm.set_pwm(0,0, servo_max)



'''

#TODO: CODE SOME SORT OF MOVEMENT





                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     