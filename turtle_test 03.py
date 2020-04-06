from turtle import*

pensize(5)

# 画出第一个三角形（倒）
for i in range(3):
    forward(99)
    right(120)

# 打补丁
forward(33)
left(60)
forward(33)
right(120)

# 画出第二个三角形（正）
for i in range(3):
    forward(99)
    right(120)

# 打补丁
left(60)

# 画出外层六边形
for i in range(6):
    forward()
    right()

