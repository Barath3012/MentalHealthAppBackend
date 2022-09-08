import turtle
def drawRectangles(Turtle):
    draw_rect(Turtle,(-250,200),(270,200),(270,-200),(-250,-200),spacing=10)
    draw_rect(Turtle, (-238, 190), (265, 190), (265, -125), (-238, -125), spacing=3)
    draw_rect(Turtle, (-230, 185), (255, 185), (255, -60), (-230, -60))

    a = ["1"] + [f"{i}/{i+1}" for i in range(1,5)] + ["5"]
    y = 160

    Turtle.pu()
    for i in range(11):
        x = -220 + i * 44
        for j in a:
            if x > 255:
                break
            Turtle.goto(x,y)
            Turtle.write(j,font=("Verdana",
                                    11, "normal"))
            x += 44
        y -= 35

    y = 210
    x = -240
    a = [2011+i for i in range(11)]
    for i in a:
        Turtle.goto(x, y)
        Turtle.write(i, font=("Verdana",
                              10, "bold"))

        x += 46
    x = -300
    y = 190-35
    for i in a:
        Turtle.goto(x, y)
        Turtle.write(i, font=("Verdana",
                              10, "bold"))
        y -= 35

    Turtle.color("blue")
    draw_rect(Turtle,(80,115),(250,115),(250,-190),(80,-190))
    Turtle.color("black")
    Turtle.penup()
    Turtle.goto(-100,240)
    Turtle.write("Year of follow-up",font=("Verdana",
                              14, "bold"))


def draw_rect(Turtle,topLeft,topRight,bottomRight,bottomLeft,spacing=0):
    print(topLeft,topRight,bottomRight,bottomLeft)
    pointHeading = {0:topRight,270:bottomRight,180:bottomLeft,90:topLeft}
    if spacing == 0:
        Turtle.penup()
        Turtle.goto(topLeft)
        Turtle.pendown()
        Turtle.goto(topRight)
        Turtle.goto(bottomRight)
        Turtle.goto(bottomLeft)
        Turtle.goto(topLeft)
    else:
        Turtle.penup()
        Turtle.goto(topLeft)
        for angle in [0,270,180,90]:
            Turtle.setheading(angle)
            currentPoint = pointHeading[(angle+90)%360]
            headingPoint = pointHeading[angle]
            #print(currentPoint,headingPoint)
            times = (int(((currentPoint[0] - headingPoint[0])**2 + (currentPoint[1] - headingPoint[1])**2)**(1/2))//spacing)
            for i in range(times + 1 if times % 2 == 0 else times):
                if i % 2 == 0:
                    Turtle.pd()
                else:
                    Turtle.penup()
                Turtle.fd(spacing)

turtle.tracer(0)
turtle.ht()
ourTurtle = turtle.Turtle()
ourTurtle.ht()
drawRectangles(ourTurtle)
turtle.tracer(1)
turtle.onscreenclick(lambda x,y:print(x,y))
turtle.mainloop()

