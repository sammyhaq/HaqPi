"""
LED.py
Code by Sammy Haq
https://github.com/sammyhaq

Simple class for using a LED with Raspberry Pi GPIO pins.
LEDs are unidirectional, meaning it matters which way the pins
go in the breadboard/whatever you're circuiting to. No resistor needed.

"""

import RPi.GPIO as GPIO
from time import sleep
from enum import Enum


class LED:

    # Constructor.
    def __init__(self, pin):

        self.pin = pin;
        GPIO.setmode(GPIO.BCM);

        GPIO.setup(self.pin, GPIO.OUT);
        GPIO.output(self.pin, GPIO.LOW);

        self.pulse = GPIO.PWM(self.pin, 1000);
        self.pulse.start(0);


    # Turns the LED on or off.
    #  ON: switchVar -> GPIO.HIGH
    #  OFF: switchVar -> GPIO.LOW
    def toggle(self, switchVar):
        if (switchVar == GPIO.HIGH):
            GPIO.output(self.pin, GPIO.HIGH);
        else:
            GPIO.output(self.pin, GPIO.LOW);

    # In some cases, it might be more useful to have hardcoded functions for
    # turning the LEDon or off. That is the purpose of the following two
    # functions:
    def toggleOn(self):
        GPIO.output(self.pin, GPIO.HIGH);

    def toggleOff(self):
        GPIO.output(self.pin, GPIO.LOW);

    # Slowly pulses the LED. Displays how PWM can be used in essentially
    # any BCM pin.
    def breathe(self, duration):

        if (duration == 0):
            return;
        
        else:
            delay = duration / (100/4) / 2;
            
            for dutyCycle in range(0, 101, 4):
                self.pulse.ChangeDutyCycle(dutyCycle);
                sleep(delay);
            for dutyCycle in reversed(range(-1, 100, 4)):
                self.pulse.ChangeDutyCycle(dutyCycle);
                sleep(delay);


    def destroy(self):
        pulse.stop();
        GPIO.output(self.pin, GPIO.HIGH);
        GPIO.cleanup();
