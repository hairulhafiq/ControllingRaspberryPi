#!/usr/bin/env python
import RPi.GPIO as gpio	
import time, sys

class _Getch:
	def __init__(self):
	   try:
		self.impl = _GetchWindows()
		
	   except ImportError:
		self.impl = _GetchUnix()

	def __call__(self): return self.impl()

class _GetchUnix:
	def __init__(self):
	   import tty, sys

        def __call__(self):
                import sys, tty, termios
                fd = sys.stdin.fileno()
                old_settings =  termios.tcgetattr(fd)
                try:
                        tty.setraw(sys.stdin.fileno())
                        ch = sys.stdin.read(1)
                finally:
                        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                return ch

class _GetchWindows:
	def __init__(self):
	   import msvcrt

	def __call__(self):
	   import msvcrt
	   return msvcrt.getch()

def Setup():
	   gpio.setmode(gpio.BOARD)
	   gpio.setwarnings(False)
	   gpio.setup(7, gpio.OUT)
	   gpio.setwarnings(False)
	   gpio.setup(22, gpio.OUT)
	   gpio.setwarnings(False)
	   gpio.setup(11, gpio.OUT)
	   gpio.setwarnings(False)
	   gpio.setup(19, gpio.OUT)

def QuitIt():
	   sys.exit()

def getInput():
	   got = int(raw_input('--> '))
	   return got

def action(key):
        global delay

        if key == 'w':
                print 'Forward'
                gpio.output(11, True)
                gpio.output(19, True)
                gpio.output(7, True)
                gpio.output(22, True)
                time.sleep(delay)
                gpio.output(11, False)
                gpio.output(19, False)

        if key == 's':
                print 'Reverse'
                gpio.output(11, True)
                gpio.output(19, True)
                gpio.output(7, False)
                gpio.output(22, False)
                time.sleep(delay)
                gpio.output(11, False)
                gpio.output(19, False)

        if key == 'a':
                print 'Left Pivot'
                gpio.output(11, True)
                gpio.output(19, True)
                gpio.output(7, False)
                gpio.output(22, True)
                time.sleep(delay)
                gpio.output(11, False)
                gpio.output(19, False)

        if key == 'd':
        	print 'Right Pivot'
                gpio.output(11, True)
                gpio.output(19, True)
                gpio.output(7, True)
                gpio.output(22, False)
                time.sleep(delay)
                gpio.output(11, False)
                gpio.output(19, False)

        if key == 't':
        	print 'Triangle Formation'
                gpio.output(11, True)
                gpio.output(19, True)
                gpio.output(7, False)
                gpio.output(22, True)
                time.sleep(0.9)
                gpio.output(7, True)
                gpio.output(22, True)
                time.sleep(2)
                gpio.output(7, True)
                gpio.output(22, False)
                time.sleep(0.8)
                gpio.output(11, False)
                gpio.output(19, False)

        if key == 'i':
                print 'Line Formation'
                gpio.output(11, True)
                gpio.output(19, True)
                gpio.output(7, False)
                gpio.output(22, True)
                time.sleep(0.9)
                gpio.output(7, False)
                gpio.output(22, False)
                time.sleep(2)
                gpio.output(7, True)
                gpio.output(22, False)
                time.sleep(0.8)
                gpio.output(11, False)
                gpio.output(19, False)

        if key == 'v':
                print 'Diamond Formation'
                gpio.output(11, True)
                gpio.output(19, True)
                gpio.output(7, True)
                gpio.output(22, False)
                time.sleep(0.4)
                gpio.output(7, True)
                gpio.output(22, True)
                time.sleep(2)
                gpio.output(7, False)
                gpio.output(22, True)
                time.sleep(0.8)
                gpio.output(7, True)
                gpio.output(22, True)
                time.sleep(2)
                gpio.output(7, True)
                gpio.output(22, False)
                time.sleep(0.8)
                gpio.output(7, False)
                gpio.output(22, False)
                time.sleep(2)
                gpio.output(7, False)
                gpio.output(22, True)
                time.sleep(0.8)
                gpio.output(7, False)
                gpio.output(22, False)
                time.sleep(2)
                gpio.output(7, True)
                gpio.output(22, False)
                time.sleep(0.4)
                gpio.output(11, False)
                gpio.output(19, False)

        if key == 'h':
                print 'Horizontal'
                gpio.output(11, True)
                gpio.output(19, True)
                gpio.output(7, False)
                gpio.output(22, True)
                time.sleep(0.8)
                gpio.output(7, True)
                gpio.output(22, True)
                time.sleep(2.7)
                gpio.output(7, True)
                gpio.output(22, False)
                time.sleep(0.7)
                gpio.output(7, True)
                gpio.output(22, True)
                time.sleep(2.7)
                gpio.output(11, False)
                gpio.output(19, False)

        if key =='n':
                print 'Line Formation'
                gpio.output(11, True)
                gpio.output(19, True)
                gpio.output(7, False)
                gpio.output(22, False)
                time.sleep(3)
                gpio.output(7, False)
                gpio.output(22, False)
                time.sleep(0.8)
                gpio.output(7, True)
                gpio.output(22, False)
                time.sleep(0.7)
                gpio.output(11, False)
                gpio.output(19, False)

        if key == 'c':
                print '15cm'
                gpio.output(11, True)
                gpio.output(19, True)
                gpio.output(7, False)
                gpio.output(22, False)
                time.sleep(2)
                gpio.output(11, False)
                gpio.output(19, False)

        if key == 'l':
        	delay = delay + 0.1
                print('Delay Up: ' + str(delay))

        if key == 'k':
        	delay = delay - 0.1
                print('Delay Down: ' + str(delay))

        if key == 'q':
        	print'Quit'
                QuitIt()

delay = 0.2

getch = _Getch()

Setup()
	
while True:
        action (getch())
