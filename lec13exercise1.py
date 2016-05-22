import turtle
window = turtle.Screen()
window.bgcolor("white")

new_turtle = turtle.Turtle()

def draw_star(new_turtle):
    for x in range(0, 5):
        new_turtle.pendown()
        new_turtle.forward(100)
        new_turtle.right(144)
        # new_turtle.forward(100)
        # new_turtle.right(120)

def draw_circle(new_turtle):
    for x in range(0,12):
        new_turtle.circle(50)
        new_turtle.right(30)

def main():
    # create an instance of Turtle
    fred = turtle.Turtle()
    draw_star(fred)
  
    lindsay = turtle.Turtle()
    lindsay.penup()
    lindsay.setx(-150)
    lindsay.pendown()
    draw_circle(lindsay)
   

    window.exitonclick()


if __name__ == '__main__':
    main()
