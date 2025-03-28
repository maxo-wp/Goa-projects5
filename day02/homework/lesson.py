from turtle import *
shape("turtle")
#lets draw a palace
speed(4)
#step 1 : rectangle

width(7)
color("gray")
begin_fill()
forward(500)
left(90)
forward(300)
left(90)
forward(500)
left(90)

end_fill()


#end of rectangle

#step 2 : door

color("brown")
penup()
goto(220,0)
pendown()
begin_fill()
left(180)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
right(90)
forward(60)
end_fill()

#step 2 : roof

penup()
goto(200,305)  
pendown()
begin_fill()
color("orange")
forward(30)
right(90)
forward(30)
right(90)
forward(50)
right(90)
forward(30)
right(90)
forward(30)
end_fill()

penup()
goto(100,305)  
pendown()
begin_fill()
color("orange")
forward(30)
right(90)
forward(30)
right(90)
forward(50)
right(90)
forward(30)
right(90)
forward(30)
end_fill()

penup()
goto(450,305)  
pendown()
begin_fill()
color("orange")
forward(30)
right(90)
forward(30)
right(90)
forward(50)
right(90)
forward(30)
right(90)
forward(30)
end_fill()

penup()
goto(350,305)  
pendown()
begin_fill()
color("orange")
forward(30)
right(90)
forward(30)
right(90)
forward(50)
right(90)
forward(30)
right(90)
forward(30)
end_fill()



#step 4 : windows
penup()
goto(100,200)
pendown()
begin_fill()
color("white")
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

penup()
goto(200,250)
pendown()
begin_fill()
color("white")
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

penup()
goto(250,250)
pendown()
begin_fill()
color("white")
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

penup()
goto(350,200)
pendown()
begin_fill()
color("white")
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()
exitonclick()