import random
import turtle as t

# def const
SCREEN_WIDTH=1200
SCREEN_HEIGHT=1200
STAR_COLOR="white"
MOON_COLOR="white"
NIGHT_COLOR="black"

# def sky
t.Screen().tracer(0,0)
t.Screen().screensize(SCREEN_WIDTH,SCREEN_HEIGHT)
t.Screen().setworldcoordinates(-SCREEN_WIDTH,-SCREEN_HEIGHT,SCREEN_WIDTH,SCREEN_HEIGHT)
t.Screen().bgcolor(NIGHT_COLOR)

# def moon
def moon(size=80):
  t.penup()
  t.left(20)

  t.color(MOON_COLOR, MOON_COLOR)
  t.dot(size)
  t.forward(size*.25)
  t.color(NIGHT_COLOR, NIGHT_COLOR)
  t.dot(size)

# def random_star
def random_star():
  t.penup()
  t.color(STAR_COLOR, STAR_COLOR)

  x=random.randint(-SCREEN_WIDTH,SCREEN_WIDTH)
  y=random.randint(-SCREEN_HEIGHT,SCREEN_HEIGHT)

  dot_size=random.random()*3

  t.goto(x,y)
  t.dot(dot_size)


for _ in range(1000):
    random_star()

moon(150)

t.hideturtle()
t.Screen().update()

# exit only on click (not before!)
t.exitonclick()