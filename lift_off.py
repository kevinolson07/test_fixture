import RPi.GPIO as GPIO
import time
speed_pins = (35,36,37,38)
hf_pins = (11,12,13,15)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(speed_pins,GPIO.OUT)
GPIO.setup(hf_pins,GPIO.OUT)
GPIO.output(speed_pins,GPIO.LOW)
GPIO.output(hf_pins,GPIO.LOW)

# max_freq = 20
# min_freq = 1
duty = .5




def pwm(freq,liftoff_freq, touchdown_freq):
    freq +=1
    for x in range(freq):
        if freq >= liftoff_freq and freq <= touchdown_freq-1:
             GPIO.output(hf_pins,GPIO.HIGH)
             print("1")
        else:
            GPIO.output(hf_pins,GPIO.LOW)
        delay = (1/freq)*.5
        GPIO.output(speed_pins,GPIO.HIGH)
        print("HIGH")
        time.sleep(delay)
        GPIO.output(speed_pins,GPIO.LOW)
        print("LOW")
        time.sleep(delay)
        print(freq)


try:   
    min_freq = int(input("Enter min frequency:"))
except ValueError:
    print("Value you entered is not of value int.")
    min_freq = int(input("Enter min frequency:"))

try:   
    max_freq = int(input("Enter max frequency:"))
except ValueError:
    print("Value you entered is not of value int.")
    max_freq = int(input("Enter max frequency:"))

try:   
    liftoff_freq = int(input("Enter liftoff frequency:"))
except ValueError:
    print("Value you entered is not of value int.")
    liftoff_freq = int(input("Enter min frequency:"))

try:   
    touchdown_freq = int(input("Enter touchdown frequency:"))
except ValueError:
    print("Value you entered is not of value int.")
    touchdown_freq = int(input("Enter touchdown frequency:"))

try:   
    cycles = int(input("Enter number of cycles:"))
except ValueError:
    print("Value you entered is not of value int.")
    cycles = int(input("Enter number of cycles:"))

try:   
    cycle_delay = int(input("Enter delay between cycles:"))
except ValueError:
    print("Value you entered is not of value int.")
    cycle_delay = int(input("Enter delay between cycles (seconds):"))

for a in range(cycles):
    for i in range(min_freq,max_freq):
        pwm(i,liftoff_freq, touchdown_freq)
    time.sleep(cycle_delay)
