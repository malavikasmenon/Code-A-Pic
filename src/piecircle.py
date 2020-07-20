def goToPoint(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()


def setBase():
    turtle.color("white")
    turtle.fillcolor("#FEF9DF")
    goToPoint(-300,-300)
    turtle.begin_fill()
    for i in range (0,2):
        turtle.fd(640)
        turtle.lt(90)
        turtle.fd(640)
        turtle.lt(90)
    turtle.end_fill()
    print(turtle.position())
    goToPoint(-290,-290)
    turtle.pencolor("black")
    turtle.begin_fill()
    for i in range (0,2):
        turtle.fd(620)
        turtle.lt(90)
        turtle.fd(620)
        turtle.lt(90)
    turtle.end_fill()

def heading():
    goToPoint(0,280)
    turtle.color('#610C05')
    style = ('Algerian', 30, 'bold')
    turtle.write('The Corona Times', font=style, align='center')

def line():
    turtle.showturtle()
    turtle.penup()
    turtle.goto(-290,270)
    turtle.pendown() 
    turtle.color("black")
    turtle.fd(620)
    turtle.hideturtle()

def pieChart():
    letter_frequencies = [ \
    ('Big-B Tests Positive', 25) ,('  Gold Seized\n at TVM Airport',25), \
        ('          Stars &\n        Lockdown',12.5), ('        India Crosses\n      10 Lakh Cases', 12.5),\
            ('Conspiracy? \nActor\'s Suicide', 7.5),('Migrant Workers\' \nDeaths',6),\
                ('EIA \nDraft',4), ('Assam \nFloods', 4)]

    colors = cycle(['#468C6C','#F2A71B','#DA6E21', '#3F8F90', '#2D5C67', '#9F4942', '#3C4059', '#D94A56'])

    radius = 175
    labelRadius = radius * 1.4
    fontSize = 12
    font = ("Ariel", fontSize, "bold")

    # The pie slices

    total = sum(fraction for _, fraction in letter_frequencies)  

    baker = turtle.Turtle() 
    baker.penup()
    baker.sety(-radius)
    baker.pendown()

    for _, fraction in letter_frequencies:
        baker.fillcolor(next(colors))
        baker.begin_fill()
        baker.circle(radius, fraction * 360 / total)
        position = baker.position()
        baker.goto(0, 0)
        baker.end_fill()
        baker.setposition(position)

    # The labels
    turtle.hideturtle()
    baker.penup()
    baker.sety(-labelRadius)

    for label, fraction in letter_frequencies:
        baker.circle(labelRadius, fraction * 360 / total / 2)
        baker.write(label, align="center", font=font)
        baker.circle(labelRadius, fraction * 360 / total / 2)
    baker.hideturtle()


import turtle
from itertools import cycle
turtle.speed(5)
window = turtle.Screen()
window.bgcolor("black")
setBase()
heading()
line()
pieChart()
turtle.hideturtle()
turtle.exitonclick()
