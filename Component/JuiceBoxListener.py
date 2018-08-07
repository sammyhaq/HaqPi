"""
JuiceBoxListener.py
Code by Sammy Haq
https://github.com/sammyhaq

Code that listens to the GPIO to see if the battery on the Raspberry Pi is low.
If it is, it triggers a callback function that safely shuts off the device.

"""


import RPi.GPIO as GPIO
import os
from HaqPyTools import UI


class JuiceBoxListener:

    # Constructor
    def __init__(self, pin, controller):

        self.pin = pin
        self.controller = controller

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        # Triggers if the battery is low.
        def lowBattery_callbackFunction(pin):

            print("Battery low! shutting down..")

            # if writer isn't closed yet, close it
            if (not self.controller.writerAction().isClosed()):
                self.controller.writerAction().closeWriter()

            self.controller.buzzerAction().metronome(0.1, 0.3, 0.05)
            self.controller.ledAction().breathe(30, 0.005)

            GPIO.cleanup()

            os.system("sudo shutdown -h now")

        # adds a listener that keeps watching the battery pin. Triggers
        # lowBattery_callbackFunction if battery is low.
        GPIO.add_event_detect(pin, GPIO.RISING,
                              callback=lowBattery_callbackFunction)
