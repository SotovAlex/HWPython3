import turtle

t = turtle.Turtle()
t.speed(0)
t.width(3)

# Настройка
t.color("green")
t.fillcolor("green")

# Тело лягушки
t.begin_fill()
t.circle(50)
t.end_fill()

# Правый глаз
t.penup()
t.goto(-20, 80)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(15)
t.end_fill()

# Зрачок
t.penup()
t.goto(-20, 85)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(6)
t.end_fill()

# Левый глаз
t.penup()
t.goto(20, 80)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(15)
t.end_fill()

# Зрачок
t.penup()
t.goto(20, 85)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(6)
t.end_fill()

# Улыбка
t.penup()
t.goto(-25, 55)
t.pendown()
t.setheading(-60)
t.circle(30, 120)
t.ht()

turtle.done()