##################################
#! /usr/bin/env python
#
# Support module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#
# This module provides the functionality for the Spy Rover GUI.
# The code for the structure of the GUI is in the SpyRoverGUI.py module.
#
# Author- Aaron Safran
##################################

# See SpyRover.py for more info on this class
from SpyRover import *
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1


# Variables
rr = SpyRover()
UP = 'w'
DOWN = 's'
RIGHT = 'd'
LEFT = 'a'
STOP = ' '

# Functions

# SetLED() allows the user to turn power output on and off for pin 18, on the raspberry pi.
# This was used to test the viability of powering an IR led, while moving the rover around.
# While the IR LED was powered with no problem, one IR LED does not provide enought light for the raspi NOIR camera to see very well in the dark.
# Therefore, I am still figuring out the best way to give the spy rover effective night vision.
def SetLED(p1):
    rr.setLED_State(not rr.getLED_State())
    if (rr.getLED_State() == True):
        w.btnNightVision['background'] = '#11ff11'
        w.btnNightVision.configure(activebackground= '#11ff11')
    else:
        w.btnNightVision['background'] = '#d9d9d9'
        w.btnNightVision.configure(activebackground='#d9d9d9')

# SetSpeed() allows the user to change the speed of the rover using the spinbox.
def SetSpeed(p1):
    if (rr.getcanMove() == False):
        motorspeed = float(w.spbxMotorSpeed.get())
        rr.setMotor_speed(motorspeed)
        w.lblClickPrompt1['foreground'] = '#d9d9d9'
        rr.setcanMove(True)
    else:
        w.lblClickPrompt1['foreground'] = 'yellow'

def set_Tk_var():
    global spinbox
    spinbox = StringVar()
    
# The "Start" button and "Change Settings" buttons were added to make sure that the rover's speed cannot be changed while it is moving.    
def changeSettings(p1):
    w.lblClickPrompt1['foreground'] = '#d9d9d9'
    rr.stop()
    rr.setcanMove(False)
    
# The "Start" button and "Change Settings" button were added to make sure that the rover's speed cannot be changed while it is moving.
def BtnStart(p1):
    w.lblClickPrompt2['foreground'] = '#d9d9d9'
    rr.setcanMove(True)
    

# Recation() listens for key presses
# The W, S, D, A, and spacebar keys can be used to make the rover move forward, backwards, right, left, and stop, respectively.
# When these keys are pressed they will cause a corresponding label on the GUI to change color.
def Reaction(p1):
    
    keyp = p1.char
    default_bg_color = '#a8a8ff'
    active_bg_color = 'yellow'
    if (rr.getcanMove() == False):
        w.lblClickPrompt2['foreground'] = 'yellow'
    elif keyp == UP:
        rr.forward(0, rr.getMotor_speed()) # if you don't specifiy duration it keeps going indefinately
        w.lblA1['background'] = default_bg_color
        w.lblW['background'] = active_bg_color
        w.lblS['background'] = default_bg_color
        w.lblD['background'] = default_bg_color
        w.lblSpacebar['background'] = default_bg_color
    elif keyp == DOWN:
        rr.reverse(0, rr.getHalf_speed())
        w.lblA1['background'] = default_bg_color
        w.lblW['background'] = default_bg_color
        w.lblS['background'] = active_bg_color
        w.lblD['background'] = default_bg_color
        w.lblSpacebar['background'] = default_bg_color
    elif keyp == RIGHT:
        rr.right(0, rr.getHalf_speed())
        w.lblA1['background'] = default_bg_color
        w.lblW['background'] = default_bg_color
        w.lblS['background'] = default_bg_color
        w.lblD['background'] = active_bg_color
        w.lblSpacebar['background'] = default_bg_color
    elif keyp == LEFT:
        rr.left(0, rr.getHalf_speed())
        w.lblA1['background'] = active_bg_color
        w.lblW['background'] = default_bg_color
        w.lblS['background'] = default_bg_color
        w.lblD['background'] = default_bg_color
        w.lblSpacebar['background'] = default_bg_color  
    elif keyp == STOP:
        rr.stop()
        w.lblA1['background'] = default_bg_color
        w.lblW['background'] = default_bg_color
        w.lblS['background'] = default_bg_color
        w.lblD['background'] = default_bg_color
        w.lblSpacebar['background'] = active_bg_color


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    root.protocol('WM_DELETE_WINDOW', on_Exit)
    # ^root.protocol('WM_DELETE_WINDOW', on_Exit) redefines the default behaviour of destroying the window.
    #  Now on_Exit is called when the window is closed.


# on_Exit makes sure the LED is off and the GPIO pins are cleaned up before the program ends.
def on_Exit():
    rr.setLED_State(False)
    GPIO.cleanup()
    global top_level
    top_level.destroy()
    top_level = None
    

if __name__ == '__main__':
    import SpyRoverGUI
    SpyRoverGUI.vp_start_gui()
    
    
