from turtle import Turtle, Screen
import random 
colors= ["green","red","Blue","coral","pink","CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","SlateGray" ]

tim = Turtle()
tim.shape("turtle")
tim.color("darkblue") 


directions = [0,90,180,270]

tim.speed(0)
tim.pensize(10)

for _ in range(250):
    tim.forward(25)
    tim.color(random.choice(colors))
    tim.setheading(random.choice(directions))
####



screen = Screen()
screen.exitonclick()