import turtle

wn = turtle.Screen()
wn.bgcolor("orange")

tess = turtle.Turtle()
tess.color("black")
tess.pensize(3)

tess.forward(165)
tess.left(90)
tess.forward(75)
tess.left(90)
tess.forward(165)
tess.left(90)
tess.forward(75)            # set his color

tess.forward(80)                 # Let tess draw an equilateral triangle
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)                   # complete the triangle

tess.right(180)                  # turn tess around
tess.forward(80)                 # move her away from the origin so we can see alex

tess.forward(50)                 # make alex draw a square
tess.left(90)
tess.forward(50)
tess.left(90)
tess.forward(50)
tess.left(90)
tess.forward(50)
tess.left(90)

wn.exitonclick()
