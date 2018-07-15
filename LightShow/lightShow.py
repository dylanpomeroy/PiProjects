from __future__ import division

import RPi.GPIO as GPIO
import time

# general GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# define the gpio numbers for each light
lights = [18, 23, 24, 25, 12]

# used to turn a light at the [gpio] on for [seconds] and then turn it off
def fL(gpio, seconds):
        GPIO.output(gpio, GPIO.HIGH)
        time.sleep(seconds)
        GPIO.output(gpio, GPIO.LOW)
        return

# executes the first sequence
def sequence1(iterations, speed):
    print("starting sequence 1")
    seconds = speed / 10
    for i in range(0, iterations):
        for x in lights:
            fL(x, seconds)
        for x in reversed(lights):
            fL(x, seconds)

# executes the second sequence
def sequence2(iterations, speed):
    print("starting sequence 2")
    seconds = speed / 10
    for i in range(0, iterations):
        dirSign = 1
        j = 1
        while j > 1 or dirSign == 1:
            fL(lights[0], seconds)
            fL(lights[j], seconds)
            
            if (j == 4):
                # reverses j's direction
                dirSign = -1
            j += dirSign

# executes the third sequence
def sequence3(iterations, speed):
    print("starting sequence 3")
    seconds = speed / 10
    for i in range(0, iterations):
        fL(24, seconds)
        fL(25, seconds)
        fL(23, seconds)
        fL(12, seconds)
        fL(18, seconds)
        fL(25, seconds)
        fL(23, seconds)

# executes the fourth sequence
def sequence4(iterations, speed):
    print("staring sequence 4")
    seconds = speed / 10
    for i in range(0, iterations):
        dirSign = -1
        j = 3
        while j < 3 or dirSign == -1:
            fL(lights[4], seconds)
            fL(lights[j], seconds)

            if (j == 0):
                # reverses j's direction
                dirSign = 1
            j += dirSign

# setup the GPIO inputs we use
for light in lights:
    GPIO.setup(light, GPIO.OUT)

# run until program is stopped
while True:
    sequence1(3, 1)
    sequence2(2, 2)
    sequence3(2, 3)
    sequence4(2, 2)


