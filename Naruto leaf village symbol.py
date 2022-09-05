import turtle as t
t. bgcolor("black")
t. pencolor("orange")
t. speed(1)
t. pensize(14)
t. hideturtle()

r = (20)

t. penup()
t. forward(100)
t. pendown()
t. left(90)
for x in range(1,15): 
    t. circle(r + x*5,-48)
    

t. right(90)
t.forward(50)
t. penup()
t. left(11)
t. backward(199)
t. pendown()
t. left(90+30)
t. forward(130)
t. left(180+60)
t. forward(150)

t. done()
