# Servo Control 

## Arduino IDE and Setup

This repo has multiple ways to run `Servos` from a keyboard. It is meant to be compatible with an `Arduino Board` and the `firmata` library. In order to successfully use any of the controllers in this repo, you first need to install the `Arduino IDE`. From there you have to locate how to install the `firmata package` and orient the correct `port` within that `IDE` that your `Arduino` is attached to. The last thing you need to do is load the `StandardFirmata` code inside the `Arduino IDE` and run it. Once that is all set and completed without error, it is time to dive into the `Python` side of things.

## Python Setup

In terms of setup for `Python`, I recommend using a steady build of `Python3` because that is what I used to develop and test. Next, you need to download `keyboard` and `pyfirmata` via `pip`. Search the web on further instructions on how to do so. Once that is done, you should be good to go to sample the code. I recommend using `dynamicServoController` because that one is more versatile and can be used for more use cases. Keep in mind these programs will only control `Servo` motors and will not control attachments such as `LEDS` or `Stepper Motors`. 

## Contact

Send an Email to `robbieg1515@gmail.com` regarding any additional controller requests or to report the occurence of bugs while using. I am aware that better input checking needs to be implemented in all of the code.

## Dynamic Servo Controller

The `dynamicServoController` is the script I recommend using regardless of what `servos` you will be controlling. It has the most freedom as of now. It will allow you to import a `port` that the `Arduino` is connected to. In addition, it will allow for custom `servo` inputs. You will be able to create a `name`, `pin # on Arduino`, `lower bound` and `upper bound` degree for the servo, `keybinds` for both adding degrees and subtracting from the servo, and a `step size` that the degrees will add to the `current position` at a time. The amount of servos in a system is not limited by the program, rather by the number of communication ports on the `Arduino`. I am currently working on a `save` feature that will allow you to save your setting that you have made for your particular case and use them again without calibrating the `servos` every time.

## Static Servo Controller

The `staticSetServoController` is the first project I made to test out operating a robotic arm that was 3-d printed. It only works with my specific build and is truly obsolete with any other type of build in this case. I recommend taking a peak at this code if you want to make a controller of your own because it is a lot more simple than the `dynamic` version. This version does not have any `OOP` in it. Instead, I made all of it to only work with one specific use. I would only recommend this code if you are going to modify it to work with just one `Arduino Servo` project you have in mind.