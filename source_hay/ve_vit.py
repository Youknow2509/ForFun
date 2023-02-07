# Duck Hunt by Chris Pedersen
# This is free and unencumbered software released into the public domain.
# For more information, please refer to <http://unlicense.org/>

import math
import random

# Launch Window using Turtle Graphics/Tkinter
import turtle
screen = turtle.Screen()
screen.setup(635, 355)

# Add Background
screen.bgpic("DuckHuntBackgroundBlack.jpg")

# Create Duck Sprite
class Duck(turtle.Turtle):
  
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.run = 2.0
    self.rise = 2.0
    self.speed = 2.0
    # Pythagorean theorem (allows us to change direction while maintaining a constant speed)
    self.a = self.run
    self.b = self.rise
    self.csquared = (self.a * self.a) + (self.b * self.b)
    self.c = math.sqrt(self.csquared)
    self.multiplier = self.speed / self.c
    self.speedAdjustedRun = self.run * self.multiplier
    self.speedAdjustedRise = self.rise * self.multiplier
    
screen.addshape("RightDuckFlapUp.png") # Load Image Into Python Program
screen.addshape("RightDuckFlapDown.png") # Load Image Into Python Program
screen.addshape("LeftDuckFlapUp.png") # Load Image Into Python Program
screen.addshape("LeftDuckFlapDown.png") # Load Image Into Python Program
screen.addshape("GunSight.png")

duck = Duck()
duck.hideturtle() # hide turtle until the the duck image replaces the placeholder shape
duck.penup() # prevent duck object from drawing on screen as it moves
duck.left(90) # rotate duck sprite for proper placement on screen
duck.shape("RightDuckFlapUp.png") # Show Image on Screen
duck.showturtle()

# CREATE GUNSIGHT
gunsight = turtle.Turtle()
gunsight.penup()
gunsight.speed()
gunsight.setposition(0, 0)
gunsight.shape("GunSight.png")

duckAlive = True

# CREATE GUNSIGHT CONTROLS
def up():
  global gunsight
  gunsight.setposition(gunsight.xcor(), gunsight.ycor() + 10)
  
def down():
  global gunsight
  gunsight.setposition(gunsight.xcor(), gunsight.ycor() - 10)

def left():
  global gunsight
  gunsight.setposition(gunsight.xcor() - 10, gunsight.ycor())
  
def right():
  global gunsight
  gunsight.setposition(gunsight.xcor() + 10, gunsight.ycor())
  
def fire():
  global gunsight
  global duck
  global duckAlive
  if duckAlive == True:
    gunsightx = gunsight.xcor()
    gunsighty = gunsight.ycor()
    duckx = duck.xcor()
    ducky = duck.ycor()
    if duckx > gunsightx - 30 and duckx < gunsightx + 30:
      if ducky > gunsighty - 30 and ducky < gunsighty + 30:
        print("KILL SHOT!")
        duckAlive = False
        killDuck()
        duckAlive = True
      
def killDuck():
  global duck
  if duck.speedAdjustedRun > 0:
    duck.right(90)
  else:
    duck.left(90)
  duck.goto(duck.xcor(), -100)
  duck.hideturtle()
  duck.goto(random.randint(-200, 200), random.randint(-100, 100))
  if duck.speedAdjustedRun > 0:
    duck.left(90)
  else:
    duck.right(90)
  
  duck.showturtle()
  
screen.onkey(up, "up")
screen.onkey(down, "down")
screen.onkey(left, "left")
screen.onkey(right, "right")
screen.onkey(fire, "space")
screen.listen()

iterationCount = 0
# Create Main Gameloop
while True:
  if duckAlive == True:
    # Create Duck Wing Flapping Animation
    if iterationCount == 10:
      if duck.speedAdjustedRun > 0:
        duck.shape("RightDuckFlapDown.png")
      else:
        duck.shape("LeftDuckFlapDown.png")
      iterationCount = iterationCount + 1
    elif iterationCount == 20:
      if duck.speedAdjustedRun > 0:
        duck.shape("RightDuckFlapUp.png")
      else:
        duck.shape("LeftDuckFlapUp.png")
      iterationCount = 0
    else:
      iterationCount = iterationCount + 1
    
    # Move Duck
    newXCoordinate = duck.xcor() + duck.speedAdjustedRun
    newYCoordinate = duck.ycor() + duck.speedAdjustedRise
    duck.goto(newXCoordinate, newYCoordinate) # Move Duck
  
    # Change Future Direction if Duck Begins To Fly off Screen (Top/Bottom)
    if duck.ycor() > 150 or duck.ycor() < -67:
      duck.speedAdjustedRise = duck.speedAdjustedRise * -1

    # Change Future Direction if Duck Begins To Fly off Screen (Left/Right)
    if duck.xcor() > 275 or duck.xcor() < -275:
      duck.speedAdjustedRun = duck.speedAdjustedRun * -1