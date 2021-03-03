import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)
GPIO.output(12,GPIO.LOW)
GPIO.setup(13,GPIO.OUT)
GPIO.output(13,GPIO.LOW)

pwmFrequency = 980
period = 1/pwmFrequency
duty = [.5,.75,1]

# PWM driver function
def pwm_driver(duty, pin):
    for i in range(pwmFrequency): 
        timeHigh = duty*period
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(timeHigh)
        timeLow = (1-duty)*period
        GPIO.output(pin,GPIO.LOW)
        time.sleep(timeLow)

# Auto mode function
def autoMode():
    motor_select = int(input("Enter 1 for vibration table #1 or 2 for vibration table #2 or 3 for both: "))
    dwell = int(input("Enter dwell time in seconds: "))
    cycles = int(input("Enter number of cycles: "))
    if motor_select == 1:
        pin = 12
    elif motor_select == 2:
        pin = 13
    elif motor_select == 3:
        pin = (12,13)
    for c in range(cycles):
        for x in range(3):
            for t in range(dwell):
                pwm_driver(duty[x],pin)

# Manual mode Function
def manualMode():
    motor_select = int(input("Enter 1 for vibration table #1 or 2 for vibration table #2: "))
    selected_duty = int(input("Enter \'1\' for \'50%\' duty, \'2\' for \'75%\' duty or \'3\' for \'100%\' duty: "))
    dwell = int(input("Enter dwell time in seconds: "))
    if motor_select == 1:
        pin = 12
    elif motor_select == 2:
        pin = 13
    elif motor_select == 3:
        pin = (12,13)
    if selected_duty == 1 or selected_duty == 2 or selected_duty == 3:
        if selected_duty == 1:
            selected_duty = duty[0]
        if selected_duty == 2:
            selected_duty = duty[1]
        if selected_duty == 3:
            selected_duty = duty[2]
        print(selected_duty)
    else:
        print("Value not valid")
    for x in range(dwell):
        pwm_driver(selected_duty,pin)

# User input 
while True:
    try: 
        mode = int(input("Enter \'1\' for auto mode or \'2\' for manual mode: "))
        if mode == 1:
            autoMode()
        elif mode == 2:
            manualMode()
        else:
            print("Number not valid. try again")
    except ValueError:
        print("Value not valid. try again")