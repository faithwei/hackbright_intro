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

def main():
    # create an instance of Turtle
    fred = turtle.Turtle()
    draw_star(fred)
    window.exitonclick()

    lindsay = turtle.Turtle()
    lindsay.setx(-150)

    for x in range(0, 36):
        draw_star(right)
        ginger.right(10)




# draw_star()

if __name__ == '__main__':
    main()