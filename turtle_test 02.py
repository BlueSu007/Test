from turtle import*

pensize(5)

for i in range(3):
    color("cyan")
    forward(99)

    color("magenta")
    circle(15)

    right(120)

# 回归初始色，打补丁后画出第二个三角形
color("cyan")
forward(33)
left(60)
forward(33)
right(120)

for i in range(3):
    color("cyan")
    forward(99)

    color("magenta")
    circle(15)

    right(120)

stamp()