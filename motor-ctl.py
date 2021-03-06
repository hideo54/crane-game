import RPi.GPIO as GPIO
import json
import sys
import time

usage = '''[Usage] `python motor-ctl.py [command]`
commands:
* open: Run before using machine
* right: Move to right
* forward: Move forward
* down: Move down
* back: Back to the default place
* close: Run after using machine'''

# Save pin numbers:
with open('pins.json', 'r') as file:
    data = json.loads(file.read())
    input1 = data['input1']
    input2 = data['input2']
    input3 = data['input3']
    input4 = data['input4']
    input5 = data['input5']
    input6 = data['input6']
    input7 = data['input7']
    input8 = data['input8']

def enableInputs(inputs):
    GPIO.output(data.values(), False)
    for input in inputs:
        GPIO.output(input, True)

# DO NOT FORGET execute `python motor-ctl.py close` when you stop running the game.
if len(sys.argv) == 2:
    command = sys.argv[1]
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(data.values(), GPIO.OUT)
    if command == 'right':
        enableInputs([input1])
    elif command == 'left':
        enableInputs([input2])
    elif command == 'forward':
        enableInputs([input3])
    elif command == 'backward':
        enableInputs([input4])
    elif command == 'down':
        enableInputs([input5])
    elif command == 'up':
        enableInputs([input6])
    elif command == 'grasp':
        enableInputs([input7])
    elif command == 'release':
        enableInputs([input8])
    elif command == 'back':
        # Grasp
        enableInputs([input7])
        time.sleep(6)
        enableInputs([])
        # Up
        enableInputs([input6])
        time.sleep(10)
        # Go to goal
        enableInputs([input1, input3, input6])
        time.sleep(6)
        enableInputs([input1, input6])
        time.sleep(4)
        enableInputs([input1])
        time.sleep(15)
        # Release
        enableInputs([input8])
        time.sleep(6)
        # Go home
        enableInputs([input2, input4])
        time.sleep(11)
        enableInputs([input2])
        time.sleep(1)
        enableinputs([])
# left: 20
# forward: 8
# Down: 10
    elif command == 'stop':
        enableInputs([])
    else:
        print('Invalid command.')
        print(usage)
        sys.quit()
else:
    print('Invalid command.')
    print(usage)
    sys.exit()
