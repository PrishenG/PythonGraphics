#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     Learning how to use turtle
#
# Author:      P.S. Govender
#
# Created:     02/03/2018
# Copyright:   (c) ACER I5 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import turtle
wn = turtle.Screen()
wn.bgcolor("red")
wn.title("Nadine and Prishen")

Nadine = turtle.Turtle()
Nadine.color("hotpink")
Nadine.pensize(5)
Nadine.shape("turtle")

Prishen = turtle.Turtle()
Prishen.color("white")
Prishen.pensize(10)
Prishen.shape("turtle")

Nadine.left(60)
Nadine.forward(300)
Nadine.left(60)
Nadine.forward(80)
Nadine.left(60)
Nadine.forward(70)
Nadine.left(60)
Nadine.forward(80)
Nadine.right(120)
Nadine.forward(80)
Nadine.left(60)
Nadine.forward(70)
Nadine.left(60)
Nadine.forward(80)
Nadine.left(60)
Nadine.forward(300)

Prishen.right(100)
Prishen.forward(80)
Prishen.right(45)
Prishen.forward(90)
Prishen.right(180)
Prishen.forward(90)
Prishen.right(90)
Prishen.forward(90)
Prishen.right(180)
Prishen.forward(90)
Prishen.right(45)
Prishen.forward(480)
Prishen.left(160)
Prishen.forward(100)
Prishen.left(110)
Prishen.forward(70)
Prishen.left(110)
Prishen.forward(100)

wn.mainloop()
