import turtle

window=turtle.Screen()
window.screensize(1000,1000)

draw=turtle.Turtle()
draw.pensize(2)

draw.speed('fastest')

angle = [36,144,144,144,144]

GetNumber = int(input("Enter a number: "))

while GetNumber <= 1 or GetNumber >= 20:
    print("Enter a number between from 2 to 19")
    GetNumber = int(input("Enter a number: "))

for shape in range(GetNumber):
    for i in angle:
        draw.left(i)
        draw.forward(180)
    draw.penup()
    draw.forward(60)
    draw.pendown()
    draw.left(170)