import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_hexagon(some_turtle):
    for i in range(1,7):
        some_turtle.forward(100)
        some_turtle.right(60)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    
    #create turtle
    halo = turtle.Turtle()
    halo.shape("turtle")
    halo.color("yellow")
    halo.speed(6)
    for i in range(1, 37):
        draw_square(halo)
        halo.right(10)
    
    #create circle
    """magica = turtle.Turtle()
        magica.shape("turtle")
        magica.color("blue")
        magica.circle(100)

    #create hexagon
    aveda = turtle.Turtle()
    aveda.shape("turtle")
    aveda.color("orange")
    draw_hexagon(aveda)"""
    
    window.exitonclick()

draw_art()

