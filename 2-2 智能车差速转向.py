import  math
speed = 20
kx = 0.85
left_speed=speed
right_speed=speed

angle = eval(input("请输入角度："))   #输入角度
if 0<=angle<=1: #右转弯
    left_speed = (1-angle*kx)*speed
    print("左轮速度为：",left_speed)#计算左轮速度
elif 1<angle<=2: # 左转弯和直行
    right_speed = (1-abs(angle*kx))*speed
    print("右轮速度为：",right_speed)#计算右轮速度
else:
    print("输入角度超出范围")
