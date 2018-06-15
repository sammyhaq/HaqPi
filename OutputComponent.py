"""
OutputComponent.py
Code by Sammy Haq
https://github.com/sammyhaq

Class for using any output device with Raspberry Pi GPIO pins.
Contains PWM stuff. Used for buttons, lasers, LEDs, haptics,
you name it.

"""

import RPi.GPIO as GPIO
import time

class OutputComponent:


    # Constructor.
    def __init__(self, pin):

        self.pin = pin;

        GPIO.setmode(GPIO.BCM);
        GPIO.setup(self.pin, GPIO.OUT);

#        self.pulse = GPIO.PWM(self.pin, 1000);
#        self.pulse.start(0);



    # In some cases, it might be more useful to have hardcoded functions for
    # turning the LED on or off. That is the purpose of the following two
    # functions:
    def toggleOn(self):
        GPIO.output(self.pin, GPIO.HIGH);

    def toggleOff(self):
        GPIO.output(self.pin, GPIO.LOW);

    # Vibrates/Sounds the device for a length of time (sec).
    def step(self, duration):
        GPIO.output(self.pin, GPIO.HIGH);
        time.sleep(duration);
        GPIO.output(self.pin, GPIO.LOW);
        time.sleep(duration);
    
    # Vibrates/Sounds the device for a certain length of time continuously. Delay
    # between the vibrations/sounds are set via the delay variable.
    def metronome(self, delay, duration):

        timerEnd = time.time() + duration;

        while (time.time() < timerEnd):
            self.step(delay);


    # DONT USE THIS UNLESS YOU ENABLE THE PWM OPTION IN INIT
    def breathe(self, duration):

        if (duration == 0):
            return;

        while True:

            delay = duration / (100/4) / 2;

            for dutyCycle in range(0, 101, 4):
                self.pulse.ChangeDutyCycle(dutyCycle);
                sleep(delay);
            for dutyCycle in reversed(range(0, 101, 4)):
                self.pulse.ChangeDutyCycle(dutyCycle);
                sleep(delay);


    # Safely terminates the class. Good to call before closing script.
    def __destroy__(self):
        #self.pulse.stop();
        GPIO.output(self.pin, GPIO.HIGH);
        GPIO.cleanup();
