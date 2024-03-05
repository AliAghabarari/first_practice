import turtle

size = int(input("write size of your shape: "))
color = input("write color of your pen: ")
shape = turtle.Turtle()
shape.shape('turtle')
shape.color(color)
for i in range(4):
    shape.forward(100)
    shape.left(90)

turtle.mainloop()