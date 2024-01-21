import turtle

def drawSquare(t, sz):
    """Make turtle t draw a square of with side sz."""

    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()              # Set up the window and its attributes
wn.bgcolor("lightgreen")

alex = turtle.Turtle()            # create alex
drawSquare(alex, 50)             # Call the function to draw the square passing the actual turtle and the actual side size

wn.exitonclick()
import turtle

def drawMulticolorSquare(t, sz):
    """Make turtle t draw a multi-colour square of sz."""
    for i in ['red','purple','hotpink','blue']:
        t.color(i)
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()           # create tess and set some attributes
tess.pensize(3)

size = 20                        # size of the smallest square
for i in range(15):
    drawMulticolorSquare(tess, size)
    size = size + 10             # increase the size for next time
    tess.forward(10)             # move tess along a little
    tess.right(18)               # and give her some extra turn

wn.exitonclick()

def square(x):
#raise x to the second power
    return x*x
print('testing square function')
assert square(3) == 9
def secti(a, b):
    soucet = a + b
    return soucet

vysledek = secti(3, 4)
print(vysledek)
def square(x):
    runningtotal = 0
    for counter in range(x):
        runningtotal = runningtotal + x

    return runningtotal

toSquare = 10
squareResult = square(toSquare)
print("The result of", toSquare, "squared is", squareResult)
def squareit(n):
    return n * n

def cubeit(n):
    return n*n*n

def main():
    anum = int(input("Please enter a number"))
    print(squareit(anum))
    print(cubeit(anum))

if __name__ == "__main__":
    main()
  def distance(x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        dsquared = dx**2 + dy**2
        result = dsquared**0.5
        return result

def area(radius):
    b = 3.14159 * radius**2
    return b

def area2(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result

print(area2(0,0,1,1))



import turtle

def nakresli_spiralu():
    okno = turtle.Screen()
    okno.bgcolor("white")

    tess = turtle.Turtle()
    tess.shape("turtle")
    tess.color("blue")

    delka_strany = 1
    uhel = 91  # úhel otočení

    for _ in range(100):  # počet kroků
        tess.forward(delka_strany)
        tess.right(uhel)
        delka_strany += 2

    okno.mainloop()

# Zavolání funkce pro nakreslení spirály
nakresli_spiralu()
