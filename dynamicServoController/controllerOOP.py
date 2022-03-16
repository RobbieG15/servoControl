from pyfirmata import Arduino, SERVO, util
import keyboard

class ServoModule():
    def __init__(self):
        self.pin = ''
        self.lowerBound = 0
        self.upperBound = 180
        self.lowerBoundKeybind = ''
        self.upperBoundKeybind = ''
        self.stepSize = 1
        self.name = ''

    def setPin(self):
        while True:
            try:
                self.pin = int(input('What pin will this servo communicate with? Enter an integer.\n'))
                self.pin = str(self.pin)
                self.pin = 'd:' + self.pin + ':o'
                break
            except:
                print('Please enter integer value. Try again.')
    def setLowerBound(self):
        while True:
            try:
                self.lowerBound = int(input('What will your lower bound degrees be for the servo? Enter an integer.\n'))
                break
            except:
                print('Please enter integer value. Try again.')
    def setUpperBound(self):
        while True:
            try:
                self.upperBound = int(input('What will your upper bound degrees be for the servo? Enter an integer.\n'))
                break
            except:
                print('Please enter integer value. Try again.')  
    def setStepSize(self):
        while True:
            try:
                self.stepSize = int(input('What will your step size be for the servo? Enter an integer.\n'))
                break
            except:
                print('Please enter integer value. Try again.') 
    def setLowerBoundKeybind(self):
        while True:
            try:
                self.lowerBoundKeybind = input('What will your lower bound keybind be for the servo? Enter a letter.\n')
                break
            except:
                print('Please enter a valid key.')    
    def setUpperBoundKeybind(self):
        while True:
            try:
                self.upperBoundKeybind = input('What will your upper bound keybind be for the servo? Enter a letter.\n')
                break
            except:
                print('Please enter a valid key.')
    def setName(self):
        while True:
            try:
                self.name = input('What will your name be for the servo? Enter a descriptive name (no spaces).\n')
                break
            except:
                print('Please enter a valid name.')
    def setAll(self):
        self.setName()
        self.setPin()
        self.setLowerBound()
        self.setLowerBoundKeybind()
        self.setUpperBound()
        self.setUpperBoundKeybind()
        self.setStepSize()

    def getName(self):
        return self.name
    def getPin(self):
        return self.pin
    def getLowerBound(self):
        return self.lowerBound
    def getLowerBoundKeybind(self):
        return self.lowerBoundKeybind
    def getUpperBound(self):
        return self.upperBound
    def getUpperBoundKeybind(self):
        return self.upperBoundKeybind
    def getStepSize(self):
        return self.stepSize
    def getAll(self):
        return [self.name, 
                self.pin, 
                self.lowerBound, 
                self.lowerBoundKeybind, 
                self.upperBound, 
                self.upperBoundKeybind, 
                self.stepSize]

class ManageServos():

    def __init__(self, board):
        self.names = []
        self.pins = []
        self.lowerBounds = []
        self.upperBounds = []
        self.lowerBoundKeybinds = []
        self.upperBoundKeybinds = []
        self.stepSizes = []
        self.savedPath = 'settings.txt'
        self.board = board

    def AddServo(self, list1):
        self.names.append(list1[0])
        self.pins.append(list1[1])
        self.lowerBounds.append(list1[2])
        self.lowerBoundKeybinds.append(list1[3])
        self.upperBounds.append(list1[4])
        self.upperBoundKeybinds.append(list1[5])
        self.stepSizes.append(list1[6])
    
    def ShowContents(self):
        for name in self.names:
            index = self.names.index(name)
            print(f'{self.names[index]}, {self.pins[index]}, {self.lowerBounds[index]}, {self.lowerBoundKeybinds[index]}, {self.upperBounds[index]}, {self.upperBoundKeybinds[index]}, {self.stepSizes[index]}')

    def CreatePins(self):
        for pin in self.pins():
            index = self.pins.index(pin)
            self.pins[index] = self.board.get_pin(pin)
            self.pins[index].mode = SERVO

    def SaveContents(self):
        f = open(self.savedPath, "a")
        for name in self.names:
            index = self.names.index(name)
            f.write(f'{self.names[index]}\n')
            f.write(f'{self.pins[index]}\n')
            f.write(f'{self.lowerBounds[index]}\n')
            f.write(f'{self.lowerBoundKeybinds[index]}\n')
            f.write(f'{self.upperBounds[index]}\n')
            f.write(f'{self.upperBoundKeybinds[index]}\n')
            f.write(f'{self.stepSizes[index]}\n')
        f.close()

    def getAll(self):
        currentPos = []
        for i in self.names:
            currentPos.append(0)
        return [self.names, self.pins, self.lowerBounds, self.lowerBoundKeybinds, self.upperBounds, self.upperBoundKeybinds, self.stepSizes, currentPos]

def continueQ():
    cont = ''
    while cont != 'y' or cont != 'n':
        cont = input('Would you like to create a servo? (y/n)\n').lower()

    return cont
    
def GetPort():
    return input("What port are you using to connect Arduino?\n")

def Controls(servos, event):
    def MoveServo(pin, angle):
        pin.write(angle)

    for name in servos[0]:
        index = servos[0].index(name)
        if event.event_type == keyboard.KEY_DOWN and event.name == servos[3][index]:
            if servos[7][index] >= servos[2][index] - servos[6][index]:
                servos[7][index] -= servos[6][index]
                MoveServo(servos[1][index], servos[7][index])
        if event.event_type == keyboard.KEY_DOWN and event.name == servos[5][index]:
            if servos[7][index] <= servos[4][index] + servos[6][index]:
                servos[7][index] += servos[6][index]
                MoveServo(servos[1][index], servos[7][index])       

def Main():
    board = Arduino(GetPort())
    iter8 = util.Iterator(board)
    iter8.start()
    servoManager = ManageServos(board)
    Servo1 = ServoModule()

    while True:
        cont = continueQ()
        if cont == 'n':
            break
        else:
            Servo1.setAll()
            contents = Servo1.getAll()
            servoManager.AddServo(contents)
    
    servoManager.SaveContents()
    servoManager.CreatePins()
    servos = servoManager.getAll()
    
    while True:
        event = keyboard.read_event()
        Controls(servos, event)



if __name__ == "__main__":
    Main()
