import turtle
import math


def fibonacci(n):
    a = 0
    b = 1
    square_a = a
    square_b = b

    fibo.pencolor("orange")

    fibo.fd(b * multiply)
    fibo.lt(90)
    fibo.fd(b * multiply)
    fibo.lt(90)
    fibo.fd(b * multiply)
    fibo.lt(90)
    fibo.fd(b * multiply)

    temp = square_b
    square_b = square_b + square_a
    square_a = temp

    for i in range(1, n):
        fibo.bk(square_a * multiply)
        fibo.rt(90)
        fibo.fd(square_b * multiply)
        fibo.lt(90)
        fibo.fd(square_b * multiply)
        fibo.lt(90)
        fibo.fd(square_b * multiply)

        temp = square_b
        square_b = square_b + square_a
        square_a = temp

    fibo.penup()
    fibo.setposition(multiply, 0)
    fibo.seth(0)
    fibo.pendown()

    fibo.pencolor("blue")

    fibo.lt(90)
    for i in range(n):
        print(b)
        spirals = math.pi * b * multiply / 2
        spirals /= 90
        for j in range(90):
            fibo.fd(spirals)
            fibo.lt(1)
        temp = a
        a = b
        b = temp + b


multiply = 5
n = int(input("escolha o número de repetições (> 1): "))

if n > 0:
    print(f"série de Fibonacci para {n} elementos: ")
    fibo = turtle.Turtle()
    turtle.title("fibonacci spirals")
    fibo.speed(100)
    fibonacci(n)
    turtle.done()
else:
    print("o número de repetições deve ser > 0.")
