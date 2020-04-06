# 画出五角星套五角星

from turtle import*

# print("请输入层数：")
# a=input()

pensize(5)
color("gold")

# 画基本五角星
for i in range(5):
    forward(50)
    right(144)

# 左转18°，换颜色，画五边形。五边形内角108°
left(36)
color("cyan")

for i in range(5):
    forward(30)
    right(72)

color("purple")
# 在五边形的每条边上画出外环三角形
for i in range(5):
    left(72)
    forward(50)
    right(144)
    forward(50)

stamp()