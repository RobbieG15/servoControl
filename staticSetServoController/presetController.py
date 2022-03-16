from pyfirmata import Arduino, SERVO, util
import keyboard


port = 'Com4'

board = Arduino(port)
print("Successfully Connected")

# start an iterator thread so
# serial buffer doesn't overflow
iter8 = util.Iterator(board)
iter8.start()

# getting pin information
mainArm = board.get_pin('')
subArm = board.get_pin('')
mainRotate = board.get_pin('')
claw = board.get_pin('')
pins = [mainArm, subArm, mainRotate, claw]

# starting pos
mainArmPosStart = 5
subArmPosStart = 0
mainRotatePosStart = 0
clawPosStart = 0
startPos = [mainArmPosStart, subArmPosStart, mainRotatePosStart, clawPosStart]

# current pos
mainArmPos = 5
subArmPos = 0
mainRotatePos = 0
clawPos = 0
currentPos = [mainArmPos, subArmPos, mainRotatePos, clawPos]

# move function
def moveServo(pin, angle):
    pin.write(angle)
    print(f"Moved {pin} to {angle} degrees.")

# pos reset function
def positionReset():
    for pin in pins:
        moveServo(pin, startPos[pins.index(pin)])

# pos to current
def returnToCurrent():
    for pin in pins:
        moveServo(pin, currentPos[pins.index(pin)])
    
positionReset()

while True:
    # Wait for the next event.
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name == 'w':
        if subArmPos <= 135:
            subArmPos += 1
            moveServo(subArm, subArmPos)
    elif event.event_type == keyboard.KEY_DOWN and event.name == 's':
        if subArmPos >= 0:
            subArmPos -= 1
            moveServo(subArm, subArmPos)
    if event.event_type == keyboard.KEY_DOWN and event.name == 'd':
        if mainRotatePos <= 180:
            mainRotatePos += 1
            moveServo(mainRotate, mainRotatePos)
    elif event.event_type == keyboard.KEY_DOWN and event.name == 'a':
        if mainRotatePos >= 0:
            mainRotatePos -= 1
            moveServo(mainRotate, mainRotatePos)
    if event.event_type == keyboard.KEY_DOWN and event.name == 'q':
        if mainArmPos <= 10:
            mainArmPos += 1
            moveServo(mainArm, mainArmPos)
    elif event.event_type == keyboard.KEY_DOWN and event.name == 'e':
        if mainArmPos >= 5:
            mainArmPos -= 1
            moveServo(mainArm, mainArmPos)
    if event.event_type == keyboard.KEY_DOWN and event.name == 'm':
        if clawPos <= 180:
            clawPos += 1
            moveServo(claw, clawPos)
    elif event.event_type == keyboard.KEY_DOWN and event.name == 'k':
        if clawPos >= 0:
            clawPos -= 1
            moveServo(claw, clawPos)
    if event.event_type == keyboard.KEY_DOWN and event.name == 'r':
        positionReset()
