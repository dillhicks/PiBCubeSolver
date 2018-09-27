from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import time

address = Adafruit_MotorHAT(addr = 0x60)

leftStepper = mh.getStepper(200, 1)
leftStepper.setSpeed(125)

rightStepper = mh.getStepper(200, 2)
rightStepper.setSpeed(125)

def leftClockwise():
	leftStepper.step(50, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)

def leftCounterClockwise():
	leftStepper.step(50, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)

def rightClockwise():
	rightStepper.step(50,Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)

def rightCounterClockwise():
	rightStepper.step(50,Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)

