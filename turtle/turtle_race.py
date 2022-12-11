import turtle
import random

def turtle_case (player, x, y, z, w):
    player.goto(x, y)
    player.pendown()
    player.circle(23)
    player.penup()
    player.goto(z, w)

def tortoise (player, n, x, y):
    player.color(input(f"jogador {n}, escolha sua cor: "))
    player.shape("turtle")
    player.penup()
    player.goto(x, y)

def steps (player):
    die_roll = random.choice(die)
    die_steps = die_roll * 20
    print("o resultado do dado é: ")
    print(die_roll)
    print("o número de passos será: ")
    print(die_steps)
    player.fd(die_steps)

turtle.title("tortoise race vers. beta")
turtle.speed(50)

p_one = turtle.Turtle()
turtle_one = input("dê um nome para a sua tartaruga: ")
tortoise(p_one, 1, -200, 100)
turtle_case(p_one, 300, 80, -200, 100)

p_two = p_one.clone()
turtle_two = input("dê um nome para a sua tartaruga: ")
tortoise(p_two, 2, -200, 0)
turtle_case(p_two, 300, -20, -200, 0)

p_three = p_two.clone()
turtle_three = input("dê um nome para a sua tartaruga: ")
tortoise(p_three, 3, -200, -100)
turtle_case(p_three, 300, -120, -200, -100)

die = [1, 2, 3, 4, 5, 6]

for i in range(20):
    if p_one.pos() >= (280, 80):
        p_two.color("gray")
        p_three.color("gray")
        print(f"parabéns! jogador 01 e {turtle_one} venceram!")
        break
    elif p_two.pos() >= (280, -20):
        p_one.color("gray")
        p_three.color("gray")
        print(f"parabéns! jogador 02 e {turtle_two} venceram!")
        break
    elif p_three.pos() >= (280, -120):
        p_one.color("gray")
        p_two.color("gray")
        print(f"parabéns! jogador 03 e {turtle_three} venceram!")
        break
    else:
        p_one_turn = input("pressione 'enter' para rolar o dado")
        steps(p_one)

        p_two_turn = input("pressione 'enter' para rolar o dado")
        steps(p_two)

        p_three_turn = input("pressione 'enter' para rolar o dado")
        steps(p_three)

turtle.done()