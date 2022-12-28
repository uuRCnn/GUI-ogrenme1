from turtle import Screen
import turtle as t
import random


flork = t.Turtle()
t.colormode(255)
flork.speed(100)


def renk_ayarla():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    renk = (r, g, b)
    return renk


def hesapla(açısı):
    for _ in range(int(360 / açısı)):
        flork.color(renk_ayarla())
        flork.circle(50)
        flork.setheading(flork.heading() + açısı)


hesapla(10)
screen = Screen()
screen.exitonclick()