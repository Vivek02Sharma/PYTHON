import turtle as t

t. speed(10)
t. fillcolor("blue")
t. pencolor("blue")
t. hideturtle()
t. begin_fill()
for i in range(36):#36
      t. forward(20)#20
      t. left(70)
      t. forward(200)#200
      t. goto(1,0)
      i+=1
t.end_fill()
t.penup()
t.goto(1,-208)
t.pendown()
t.pensize(15)
t.circle(210)
t. done()
