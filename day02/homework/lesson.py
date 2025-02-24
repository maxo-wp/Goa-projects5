import turtle

# ფუნქცია მართკუთხედის ხატვისთვის
def draw_rectangle(x, y, width, height, color):
    """ხატავს მართკუთხედს მოცემულ კოორდინატებზე (x, y) განსაზღვრული სიგანით და სიმაღლით, 
    შევსებული მითითებული ფერთან."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

# ფანჯრის მომზადება
turtle.speed(3)
turtle.bgcolor("skyblue")

# მთავარი შენობა
# ნიღაბი: ფართო და დიდ სიმაღლით
draw_rectangle(-200, -150, 400, 300, "lightgray")

# მთავარი შენობის ბატლემენტები (ზედა ხაზი)
# ვხატავთ მცირე მართკუთხედებს ზედა ნაწილზე
battlement_count = 8
battlement_width = 40
battlement_height = 20
start_x = -200
start_y = 150  # ძირითად შენობის ზედა სხვისი წერტილი

for i in range(battlement_count):
    x = start_x + i * (400 / battlement_count)
    draw_rectangle(x, start_y, battlement_width, battlement_height, "darkgray")

# მარცხენა ტაუნი (ტაძარი)
draw_rectangle(-260, -150, 60, 400, "gray")
# მარცხენა ტაუონის ბატლემენტები
for i in range(3):
    x = -260 + i * 20
    draw_rectangle(x, 250, 15, 20, "black")

# მარჯვენა ტაუნი (ტაძარი)
draw_rectangle(200, -150, 60, 400, "gray")
# მარჯვენა ტაუონის ბატლემენტები
for i in range(3):
    x = 200 + i * 20
    draw_rectangle(x, 250, 15, 20, "black")

# ცენტრალური კარი
draw_rectangle(-40, -150, 80, 120, "brown")

# კარიის ქვეშ ზომიერ ამოკლებით ხეაორგელით ანარკის შეტანის დასაკრავებლად
turtle.penup()
turtle.goto(-40, -150)
turtle.pendown()
turtle.color("brown")
turtle.setheading(0)
turtle.forward(80)
turtle.setheading(90)
turtle.circle(40, 180)  # ნახევარი წრე კარის ზემოთ

# ფანჯრები მთავარი შენობაზე
draw_rectangle(-160, 0, 40, 40, "blue")
draw_rectangle(120, 0, 40, 40, "blue")
draw_rectangle(-160, 100, 40, 40, "blue")
draw_rectangle(120, 100, 40, 40, "blue")

turtle.hideturtle()
turtle.done()