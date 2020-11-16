import turtle

wn = turtle.Screen()
wn.bgcolor("orange")

tess = turtle.Turtle()
tess.color("black")
tess.pensize(3)

distance = 50
for _ in range(10):
    tess.forward(distance)
    tess.left(90)
    distance = distance + 10

tess.shape("turtle")
tess.color("blue")
dis = 5
tess.up()
for _ in range(30):
    tess.stamp()
    tess.forward(dis)
    tess.right(24)
    dis = dis + 2
