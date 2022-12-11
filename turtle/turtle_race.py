import turtle
import random

def turtle_screen(screen):
    screen.Screen()
    screen.title("turtle race")
    screen.bgcolor("#32CD32")
    screen.color("white")
    screen.speed(0)
    screen.penup()
    screen.setposition(-180, 185)
    screen.write("TURTLE RACE!!", font=("Arial", 36, "bold"))
    screen.penup()
    screen.goto(-170, 185)
    screen.pendown()
    screen.pensize(4)
    screen.fd(350)
    screen.penup()
    screen.ht()


def finish_line(line):
    line.color("black")
    line.shape("square")
    line.shapesize(0.7)
    line.penup()

    for i in range(10):
        line.setpos(280, 130 - (i * 30))
        line.stamp()
        for j in range(10):
            line.setpos(295, 115 - (i * 30))
            line.stamp()

    line.color("white")
    line.penup()

    for i in range(10):
        line.setpos(295, 130 - (i * 30))
        line.stamp()
        for j in range(10):
            line.setpos(280, 115 - (i * 30))
            line.stamp()


def tortoise(player, n, x, y):
    player.color("black", input(f"jogador {n}, escolha sua cor: "))
    player.shape("turtle")
    player.shapesize(1.5, 1.5, 2)
    player.penup()
    player.goto(x, y)


def steps(player):
    die_roll = random.choice(die)
    die_steps = die_roll * 15
    print("o resultado do dado é: ")
    print(die_roll)
    print("o número de passos será: ")
    print(die_steps)
    player.fd(die_steps)


def winner(turtle_name, x, y):
    player = turtle.Turtle()
    player.speed(0)
    player.penup()
    player.setposition(x - 5, y - 5)
    player.pendown()
    player.write(f"PARABÉNS!! {turtle_name} VENCEU", font=("Arial", 13, "bold"))
    player.penup()
    player.ht()


turtle_screen(turtle)
finish_line(turtle)

p_one = turtle.Turtle()
turtle_one = input("nomeie sua tartaruga: ")
tortoise(p_one, 1, -280, 85)

p_two = p_one.clone()
turtle_two = input("nomeie sua tartaruga: ")
tortoise(p_two, 2, -280, -15)

p_three = p_two.clone()
turtle_three = input("nomeie sua tartaruga: ")
tortoise(p_three, 3, -280, -115)

die = [1, 2, 3, 4, 5, 6]

for i in range(40):
    if p_one.pos() >= (280, 85):
        p_two.color("gray")
        p_three.color("gray")
        print(f"parabéns! jogador 01 e {turtle_one} venceram!")
        winner(turtle_one, -280, 85)
        break

    elif p_two.pos() >= (280, -15):
        p_one.color("gray")
        p_three.color("gray")
        print(f"parabéns! jogador 02 e {turtle_two} venceram!")
        winner(turtle_two, -280, -15)
        break

    elif p_three.pos() >= (280, -115):
        p_one.color("gray")
        p_two.color("gray")
        print(f"parabéns! jogador 03 e {turtle_three} venceram!")
        winner(turtle_three, -280, -115)
        break

    else:
        p_one_turn = input("pressione 'ENTER' para rolar o dado")
        steps(p_one)

        p_two_turn = input("pressione 'ENTER' para rolar o dado")
        steps(p_two)

        p_three_turn = input("pressione 'ENTER' para rolar o dado")
        steps(p_three)

turtle.exitonclick()