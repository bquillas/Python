# import turtle

# window = turtle.Screen()
# bill = turtle.Turtle()
# bill.forward(50)
# bill.left(90)
# bill.forward(50)
# bill.left(90)
# bill.forward(50)
# bill.left(90)
# bill.forward(50)
# bill.left(90)

# turtle.mainloop()

# import turtle

# window = turtle.Screen()

# colors=['red','purple','blue','green','yellow','orange']

# t = turtle.Pen()
# t.speed(0)
# for x in range(360):
#     t.pencolor(colors[x%6])
#     t.width(x/100+1)
#     t.forward(x)
#     t.left(59)

# turtle.mainloop()

import turtle

def main():
    window = turtle.Screen()
    bill = turtle.Turtle()

    make_square(bill)

    turtle.mainloop()


def make_square(bill):
    lenght = int(input("Square lenght: "))

    for i in range(4):
        make_lines(bill,lenght)

def make_lines(bill,lenght):
    bill.forward(lenght)
    bill.left(90)


if __name__ == '__main__':
    main()