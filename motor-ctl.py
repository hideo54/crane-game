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

# DO NOT FORGET execute `python motor-ctl.py close` when you stop running the game.
if len(sys.argv) == 2
    command = sys.argv[1]
    if command in ['open', 'right', 'forward', 'down', 'back', 'close']:
        with open('pins.json', 'r') as file:
            data = json.loads(file.read())
            enable = data['enable']
            input1 = data['input1']
            input2 = data['input2']
            input3 = data['input3']
            input4 = data['input4']
            input5 = data['input5']
            input6 = data['input6']
        def disableAllInput():
            GPIO.output(input1, False)
            GPIO.output(input2, False)
            GPIO.output(input3, False)
            GPIO.output(input4, False)
            GPIO.output(input5, False)
            GPIO.output(input6, False)
        if command == 'open':
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(data.values(), GPIO.OUT)
            GPIO.output(data.values(), False)
            GPIO.output(enable, True)
            print('Ready to run the game.')
            sys.exit()
        elif command == 'right':
            disableAllInput()
            GPIO.output(input1, True)
        elif command == 'forward':
            disableAllInput()
            GPIO.output(input3, True)
        elif command == 'down':
            disableAllInput()
            GPIO.output(input5, True)
        elif command == 'close':
            disableAllInput()
            GPIO.cleanup()
            sys.exit()
    else:
        print(usage)
        sys.exit()
else:
    print(usage)
    sys.exit()
