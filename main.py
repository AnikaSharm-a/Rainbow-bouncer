# Imports
from tkinter import *
from math import sqrt
from time import sleep
from random import randint

# Screen setup
tk = Tk()
s = Canvas(tk, width = 600, height = 600, background = "black")
s.pack()

# Ring variables
x = 0
size = 600

# Creating rings
for ring in range(6):
  s.create_oval(x,x, x+size,x+size, fill = "", outline = "white")
  x += 50
  size -= 100

# Ball's coordinates
xball = 1
yball = 200
xspeed = 5
yspeed = -2

# Loop to make the ball
while True:

  # Distance of the ball from center
  d = sqrt((300-xball)**2 + (300-yball)**2)
  

  # Deciding colour of ball based on distance from center
  if d <= 50: colour = "red"
  elif d <= 100: colour = "blue"
  elif d <= 150: colour = "lawn green"
  elif d <= 200: colour = "purple" 
  elif d <= 250: colour = "pink"  
  elif d <= 300: colour = "turquoise"  
  else: colour = "white" 


  # Creating the ball
  ball = s.create_oval(xball,yball, xball+20,yball+20, fill = colour, outline = "")


  # Bouncing effect
  if xball+20 > 600 or xball < 0:
    xspeed *= -1

  if yball+20 > 600 or yball < 0:
    yspeed *= -1


  # Increments
  xball += xspeed
  yball += yspeed


  # Update, sleep, delete
  s.update()
  sleep(0.03)
  s.delete(ball)