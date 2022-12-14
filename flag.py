import turtle
from turtle import *

shape("turtle")
speed(5)
penup()
goto(-300, 150)
pendown()
color("#c1272c")
begin_fill()
for i in range(2):
    forward(600)
    right(90)
    forward(400)
    right(90)

end_fill()
width(15)
goto(-150, 0)
pendown()
color("darkgreen")

for i in range(5):
    forward(300)
    right(144)

penup()
goto(-80, 200)

write("أسود الأطلس "+"\N{flexed biceps}"+"\N{palms up together}", font=("Arbic", 30, "bold"))

penup()
end_fill()


