import turtle

turtle.bgcolor('red')
neck = turtle.Turtle()
neck.speed(20)
neck.color("black","#FFD7C1")
neck.penup()
neck.goto(-282.50,-160.14)
neck.pendown()
neck.begin_fill()
neck.rt(85)
neck.fd(30)
neck.left(45)
neck.bk(40)
neck.fd(70)
neck.lt(35)
neck.back(110)
neck.fd(110)
neck.circle(-30,extent=50)
neck.forward(50)
neck.rt(140)
neck.circle(-800,extent=15)
xx=neck.pos()
neck.goto(-385,50)
neck.end_fill()
neck.hideturtle()

cartoon_character_goku = turtle.Turtle()
cartoon_character_goku.speed(20)
cartoon_character_goku.color("black", "#FFD7C1")
cartoon_character_goku.penup()
cartoon_character_goku.goto(-205,-85)
cartoon_character_goku.pendown()
cartoon_character_goku.begin_fill()
cartoon_character_goku.lt(50)
cartoon_character_goku.fd(10)
cartoon_character_goku.lt(45)
cartoon_character_goku.fd(85)
z = cartoon_character_goku.pos()
cartoon_character_goku.penup()
cartoon_character_goku.goto(-205,-85)
cartoon_character_goku.pendown()
cartoon_character_goku.rt(145)
cartoon_character_goku.fd(30)
cartoon_character_goku.right(110)
cartoon_character_goku.fd(20)
cartoon_character_goku.lt(60)
cartoon_character_goku.forward(10)
cartoon_character_goku.right(45)
cartoon_character_goku.forward(10)
x=cartoon_character_goku.pos()
cartoon_character_goku.rt(45)
cartoon_character_goku.fd(20)
cartoon_character_goku.lt(25)
cartoon_character_goku.fd(10)
cartoon_character_goku.penup()
cartoon_character_goku.goto(x)
cartoon_character_goku.pendown()
cartoon_character_goku.left(45)
cartoon_character_goku.fd(10)
cartoon_character_goku.rt(45)
cartoon_character_goku.fd(10)
cartoon_character_goku.back(5)
cartoon_character_goku.lt(45)
cartoon_character_goku.fd(35)
for i in range(5):
    cartoon_character_goku.rt(17)
    cartoon_character_goku.fd(3)
cartoon_character_goku.fd(30)
n = cartoon_character_goku.pos()
cartoon_character_goku.fd(70)
cartoon_character_goku.rt(70)
cartoon_character_goku.fd(40)
y=cartoon_character_goku.pos()
cartoon_character_goku.fd(100)
cartoon_character_goku.goto(z)
cartoon_character_goku.end_fill()
cartoon_character_goku.hideturtle()

hair = turtle.Turtle()
hair.speed(20)
hair.penup()
hair.goto(-385,50)
start=hair.pos()
hair.pendown()
hair.begin_fill()
hair.lt(45)
hair.circle(-100,extent=30)
hair.lt(65)
hair.circle(-200,extent=45)
hair.rt(160)
hair.circle(200,extent=35)
hair.lt(135)
hair.forward(50)
hair.rt(20)
hair.circle(-200,extent=45)
hair.right(135)
hair.circle(200,extent=25)
hair.left(145)
hair.circle(-120,extent=75)
hair.rt(135)
hair.circle(300,extent=15)
hair.lt(145)
hair.fd(30)
hair.circle(-150,extent=30)
hair.rt(135)
hair.circle(300,extent=25)
hair.lt(90)
hair.circle(-60,extent=50)
hair.rt(130)
hair.circle(100,extent=45)
hair.left(130)
hair.circle(-60,extent=50)
hair.rt(130)
hair.circle(100,extent=35)
hair.lt(100)
hair.circle(60,extent=50)
hair.rt(135)
hair.circle(-60,extent=30)
hair.lt(120)
hair.forward(155)
hair.goto(start)
hair.end_fill()
hair.hideturtle()

ear=turtle.Turtle()
ear.speed(20)
ear.color("black","#FFD7C1")
ear.penup()
ear.goto(y)
ear.pendown()
ear.begin_fill()
ear.right(90)
for i in range(5):
    ear.rt(27)
    ear.fd(2)
ear.forward(25)
ear.rt(70)
ear.circle(-200,extent=10)
ear.color("#FFD7C1","#FFD7C1")
ear.rt(110)
ear.forward(30)
ear.goto(y)
ear.end_fill()
ear.hideturtle()

blue = turtle.Turtle()
blue.speed(20)
blue.color("dark blue")
blue.penup()
blue.goto(-206.27,-262.95)
blue.pendown()
blue.begin_fill()
blue.right(35)
blue.circle(-100,extent=40)
blue.rt(110)
blue.fd(250)
blue.goto(xx)
blue.end_fill()
blue.hideturtle()

orange = turtle.Turtle()
orange.speed(20)
orange.color("#F85B1A")
orange.penup()
orange.goto(xx)
orange.pendown()
orange.begin_fill()
orange.rt(50)
orange.circle(400,extent=40)
orange.left(10)
orange.back(250)
orange.goto(xx)
orange.end_fill()

eye = turtle.Turtle()
eye.speed(20)
eye.penup()
eye.goto(-210,-75)
eye.pendown()
eye.right(125)
eye.forward(5)
e = eye.pos()
eye.rt(90)
eye.begin_fill()
eye.fd(60)
eye.lt(70)
eye.fd(10)
eye.lt(115)
eye.fd(17)
e1 = eye.pos()
eye.fd(40)
eye.goto(e)
eye.end_fill()
eye.goto(e1)
eye.color("black","white")
eye.begin_fill()
eye.rt(70)
eye.fd(17)
eye.lt(85)
eye.fd(37)
eye.end_fill()
eye.begin_fill()
eye.color("black")
eye.circle(5)
eye.end_fill()
eye.hideturtle()

hair2 = turtle.Turtle()
hair2.speed(20)
hair2.penup()
hair2.goto((189.15,-42.93))
hair2.pendown()
hair2.begin_fill()
hair2.lt(105)
hair2.fd(80)
hair2.left(25)
hair2.back(20)
hair2.rt(50)
hair2.fd(30)
hair2.rt(25)
hair2.fd(100)
hair2.lt(35)
hair2.back(40)
hair2.rt(35)
hair2.circle(-200,extent=30)
hair2.lt(45)
hair2.back(35)
hair2.rt(25)
hair2.circle(-100,extent=20)
hair2.circle(100,extent=30)
hair2.left(35)
hair2.back(310)
hair2.lt(90)
hair2.fd(100)
hair2.goto((189.15,-42.93))
hair2.end_fill()
hair2.hideturtle()

neck1 = turtle.Turtle()
neck1.speed(20)
neck1.color("black","#FFE1CD")
neck1.penup()
neck1.goto(243.28,-169.45)
neck1.pendown()
neck1.begin_fill()
neck1.rt(85)
neck1.fd(30)
neck1.rt(45)
neck1.bk(40)
neck1.fd(70)
t = neck1.pos()
neck1.lt(130)
neck1.circle(300,extent=32)
neck1.lt(90)
end = neck1.pos()
neck1.circle(300,extent=30)
neck1.goto(243.28,-169.45)
neck1.end_fill()
neck1.hideturtle()

cartoon_character_vegeta = turtle.Turtle()
cartoon_character_vegeta.speed(20)
cartoon_character_vegeta.color("black","#FFE1CD")
cartoon_character_vegeta.penup()
cartoon_character_vegeta.goto(180,-85)
cartoon_character_vegeta.pendown()
cartoon_character_vegeta.begin_fill()
cartoon_character_vegeta.rt(140)
cartoon_character_vegeta.fd(30)
cartoon_character_vegeta.lt(110)
cartoon_character_vegeta.fd(20)
cartoon_character_vegeta.rt(60)
cartoon_character_vegeta.forward(7)
cartoon_character_vegeta.lt(45)
cartoon_character_vegeta.fd(10)
v = cartoon_character_vegeta.pos()
cartoon_character_vegeta.lt(55)
cartoon_character_vegeta.fd(20)
cartoon_character_vegeta.lt(25)
cartoon_character_vegeta.fd(10)
cartoon_character_vegeta.penup()
cartoon_character_vegeta.goto(v)
cartoon_character_vegeta.pendown()
cartoon_character_vegeta.rt(105)
cartoon_character_vegeta.fd(10)
cartoon_character_vegeta.lt(45)
cartoon_character_vegeta.fd(10)
cartoon_character_vegeta.back(5)
cartoon_character_vegeta.rt(45)
cartoon_character_vegeta.fd(35)
cartoon_character_vegeta.speed(20)
for i in range(5):
    cartoon_character_vegeta.lt(17)
    cartoon_character_vegeta.fd(3)
cartoon_character_vegeta.fd(30)
g = cartoon_character_vegeta.pos()
cartoon_character_vegeta.fd(70)
cartoon_character_vegeta.lt(70)
cartoon_character_vegeta.fd(40)
cartoon_character_vegeta.rt(150)
cartoon_character_vegeta.circle(5,extent=110)
cartoon_character_vegeta.fd(30)
cartoon_character_vegeta.lt(70)
cartoon_character_vegeta.circle(200,extent=7)
cartoon_character_vegeta.circle(10,extent=100)
cartoon_character_vegeta.fd(25)
cartoon_character_vegeta.rt(100)
cartoon_character_vegeta.fd(30)
cartoon_character_vegeta.rt(145)
cartoon_character_vegeta.fd(10)
cartoon_character_vegeta.circle(5,extent=140)
cartoon_character_vegeta.forward(70)
cartoon_character_vegeta.circle(20,extent=65)
cartoon_character_vegeta.fd(5)
cartoon_character_vegeta.circle(45,extent=65)
cartoon_character_vegeta.fd(35)
cartoon_character_vegeta.fd(35)
cartoon_character_vegeta.goto(180,-85)
cartoon_character_vegeta.end_fill()
cartoon_character_vegeta.hideturtle()

blue1 = turtle.Turtle()
blue1.speed(20)
blue1.color("blue")
blue1.penup()
blue1.goto(t)
blue1.pendown()
blue1.begin_fill()
blue1.rt(160)
blue1.circle(20,extent=40)
blue1.fd(110)
blue1.lt(120)
blue1.fd(250)
blue1.goto(end)
blue1.end_fill()
blue1.hideturtle()

suit= turtle.Turtle()
suit.speed(20)
suit.color("#F3A903")
suit.penup()
suit.goto(end)
suit.pendown()
suit.begin_fill()
suit.rt(180)
suit.circle(120,extent=75)
suit.lt(100)
suit.fd(50)
s = suit.pos()
suit.lt(100)
suit.circle(-70,extent=95)
suit.goto(end)
suit.end_fill()
suit.penup()
suit.goto(s)
suit.pendown()
suit.color("black","#707070")
suit.pensize(2)
suit.begin_fill()
suit.rt(182)
suit.fd(70)
suit.circle(10,extent=90)
suit.fd(5)
suit.rt(90)
suit.fd(50)
suit.circle(18,extent=70)
suit.fd(35)
suit.lt(110)
suit.fd(250)
suit.lt(90)
suit.fd(63)
suit.goto(s)
suit.end_fill()
suit.hideturtle()

eye1 = turtle.Turtle()
eye1.speed(20)
eye1.penup()
eye1.goto(185,-75)
eye1.pendown()
eye1.right(35)
eye1.forward(5)
e2 = eye1.pos()
eye1.lt(70)
eye1.begin_fill()
eye1.fd(60)
eye1.rt(70)
eye1.fd(10)
eye1.rt(115)
eye1.fd(17)
e3 = eye1.pos()
eye1.fd(40)
eye1.goto(e2)
eye1.end_fill()
eye1.goto(e3)
eye1.color("black","white")
eye1.begin_fill()
eye1.lt(70)
eye1.fd(17)
eye1.rt(85)
eye1.fd(37)
eye1.end_fill()
eye1.begin_fill()
eye1.color("black")
eye1.circle(-5)
eye1.end_fill()
eye1.hideturtle()

turtle.mainloop()
