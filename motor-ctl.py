import RPi.GPIO as GPIO
import json
import sys
import time

usage = '[Usage] `python motor-ctl.py [number] [direction] [command]`'

# DO NOT FORGET execute `python motor-ctl.py close` when you stop running the game.
if len(sys.argv) == 2
    if sys.argv[1] == 'open':
        mode = 'open'
    elif sys.argv[1] == 'close':
        GPIO.cleanup()
        sys.exit()
    else:
        print(usage)
        sys.exit()
elif len(sys.argv) == 4:
    mode = 'run'
    try:
        motor = int(sys.argv[1])
        if motor != 1 or 2 or 3:
            raise Exception('improper')
    except:
        print('Specify motor number as 1, 2, or 3')
        print(usage)
        sys.exit()

    direction = sys.argv[2]
    if direction != 'left' or 'right':
        print('Specify move direction as left or right')
        print(usage)
        sys.exit()

    command = sys.argv[3]
    if command != 'start' or 'stop':
        print('Specify command as start or stop')
        print(usage)
        sys.exit()
else:
    print(usage)
    sys.exit()

# All error-processing must be finished till here.
# DO NOT USE GPIO TILL HERE.
# There must be only expeceted-type values bellow.

with open('pins.json', 'r') as file:
    data = json.loads(file.read())
    enable = data['enable']
    input1 = data['input1']
    input2 = data['input2']
    input3 = data['input3']
    input4 = data['input4']
    input5 = data['input5']
    input6 = data['input6']

if mode == 'start'
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(data.values(), GPIO.OUT)
    GPIO.output(data.values(), False)
    GPIO.output(enable, True)
    print('Ready to run the game.')
    sys.exit()

if motor == 1:
    output = [input1, input2]
elif motor == 2:
    output = [input3, input4]
elif motor == 3:
    output = [input5, input6]

if direction == 'right':
    output.reverse()

GPIO.output(output[0], True)
GPIO.output(output[1], False)
