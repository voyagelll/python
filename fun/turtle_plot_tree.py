import turtle
import random
from math import *

def Fibonacci_Recursion_tool(n):  #
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci_Recursion_tool(n - 1) + Fibonacci_Recursion_tool(n - 2)


def Fibonacci_Recursion(n):     #
    result_list = []
    for i in range(1, n + 3):
        result_list.append(Fibonacci_Recursion_tool(i))
    return result_list


def leaf(x,y,node):#
    til=turtle.heading()
    i= random.random()
    an = random.randint(10,180)
    ye = random.randint(6,9)/10
    turtle.color(ye, ye*0.9,0)
    turtle.fillcolor(ye+0.1,ye+0.05,0)
    turtle.pensize(1)
    turtle.pendown()
    turtle.setheading(an + 90)
    turtle.forward(8*i)
    px=turtle.xcor()
    py=turtle.ycor()
    turtle.begin_fill()
    turtle.circle(7.5*i, 120)  # 画一段120度的弧线
    turtle.penup()  # 抬起笔来

    turtle.goto(px, py)  # 回到圆点位置
    turtle.setheading(an + 90)  # 向上画
    turtle.pendown()  # 落笔，开始画
    turtle.circle(-7.5*i, 120)  # 画一段120度的弧线
    turtle.setheading(an + 100)
    turtle.circle(10.5*i, 150)
    turtle.end_fill()  # 画一段150度的弧线
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(til)
    turtle.pensize(node / 2 + 1)


def draw(node,length,level,yu,button):
    turtle.pendown()
    t = cos(radians(turtle.heading()+5)) / 8 + 0.25
    turtle.pencolor(t*1.6, t*1.2, t*1.4)
    #turtle.pencolor("gray")
    turtle.pensize(node/1.2)        
    x = random.randint(0, 10)
    #turtle.forward(length)  # 画树枝
    #yu[level] = yu[level] - 1

    if  level==top and x==5 :
       turtle.forward(length)  # 画树枝
       yu[level] = yu[level] - 1
       c=random.randint(2,10)
       for i in range(1,c):
           leaf(turtle.xcor(), turtle.ycor(),node)
           # 添加0.3倍的飘落叶子
           if random.random() >0.5:
               turtle.penup()
               # 飘落
               t1 = turtle.heading()
               an1 = -40 + random.random() * 40
               turtle.setheading(an1)
               dis = int(800 * random.random() * 0.5 + 400 * random.random() * 0.3 + 200 * random.random() * 0.2)
               turtle.forward(dis)
               turtle.setheading(t1)

               turtle.right(90)
               # 画叶子
               leaf(turtle.xcor(), turtle.ycor(), node)
               turtle.left(90)
               # 返回
               t2 = turtle.heading()
               turtle.setheading(an1)
               turtle.backward(dis)
               turtle.setheading(t2)


    elif level==top and x!=5 :
        turtle.penup()
        turtle.forward(length)
        #leaf(turtle.xcor(),turtle.ycor())# jump

    elif level>3 and (x>6) :
        turtle.pendown()
        turtle.forward(length)
        c = random.randint(4, 6)
       # leaf(turtle.xcor(), turtle.ycor())
        for i in range(3, c):
            leaf(turtle.xcor(), turtle.ycor(),node)
        leaf(turtle.xcor(), turtle.ycor(),node)
        button=1# jump"""
    else:
        turtle.forward(length)  # 画树枝
        yu[level] = yu[level] -1
    if node>0 and button==0:

        # 计算右侧分支偏转角度,在固定角度偏转增加一个随机的偏移量
        right = random.random() * 5 + 17
        # 计算左侧分支偏转角度,在固定角度偏转增加一个随机的偏移量
        left = random.random() * 20 + 19
        # 计算下一级分支的长度
        child_length = length * (random.random() * 0.25 + 0.7)
        # 右转一定角度,画右分支
        r=random.randint(0, 1)
        # print(r)
        if r==1:
          turtle.right(right)
          level = level + 1
          # print("level",level)
        else:
          turtle.left(right)
          level = level + 1
          # print("level", level)
        draw(node - 1, child_length,level,yu,button)

        yu[level] = yu[level] +1

        if yu[level]>1:
            # 左转一定角度，画左分支

            if r==1:
               turtle.left(right + left)
               draw(node - 1, child_length, level, yu,button)
               # 将偏转的角度，转回
               turtle.right(left)
               # print("yu", yu)
               yu[level] = yu[level] - 1
            else:
                turtle.right(right + left)
                draw(node - 1, child_length, level, yu,button)
                # 将偏转的角度，转回
                turtle.left(left)
                # print("yu", yu)
                yu[level] = yu[level] - 1
        else:
            if r==1:
              turtle.left(right + left)
              turtle.right(left)
              # print("yu", yu)
            else:
                turtle.right(right + left)
                turtle.left(left)
                # print("yu", yu)
    turtle.penup()
    #退回到上一级节点顶部位置
    turtle.backward(length)

turtle.hideturtle()     #隐藏turtle
turtle.speed(0);        #设置画笔移动的速度，0-10 值越小速度越快
#turtle.tracer(0,0)      #设置动画的开关和延迟，均为0
turtle.penup()          #抬起画笔
turtle.left(90)         #默认方向为朝x轴的正方向，左转90度则朝上
turtle.backward(300)#设置turtle的位置，朝下移动300
top=9
yu=Fibonacci_Recursion(top)
yu.remove(yu[0])
print(yu)
button=0
for i in range(10):
  print(i)
  draw(top,120,0,yu,button)        #调用函数开始绘制

turtle.write("      教室工作室-ClassStudio", font=("微软雅黑", 14, "normal"))

turtle.done()





# peppaPig
import turtle as t
#嘤嘤嘤 定义了个小猪佩奇类
class peppaPig:
    def __init__(self):
        self.penset()
        self.nose()
        self.head()
        self.ears()
        self.eyes()
        self.cheek()
        self.mouth()
        self.body()
        self.hands()
        self.feet()
        t.hideturtle()
        t.exitonclick()
 
    def penset(self):
        t.pensize(4)    #设置画笔大小
        t.colormode(255) #设置GBK颜色范围
        t.color((255,155,192),"pink")  #设置画笔颜色和填充色
        t.speed(10)  #设置画笔速度
 
    #鼻子
    def nose(self):
        t.pu()  #penup的简写，提笔
        t.goto(-100,100)  #前往坐标(-100,100)
        t.pd()  #pendown的简写，下笔
        t.seth(-30)
        t.begin_fill()  #外形填充的开始标志
        a = 0.4
        for i in range(120):
            if 0<=i<30 or 60<=i<90:
              a = a+0.08
              t.lt(3) #left的简写，向左转3度
              t.fd(a) #forward的简写，向前走a的步长
            else:
                a = a-0.08
                t.lt(3)
                t.fd(a)
        t.end_fill()
        t.pu()
        t.seth(90)
        t.fd(25)
        t.seth(0)
        t.fd(10)
        t.pd()
        t.color((255,155,192))
        t.seth(10)
        t.begin_fill()
        t.circle(5)
        t.color(160,82,45)
        t.end_fill()
        t.pu()
        t.seth(0)
        t.fd(20)
        t.pd()
        t.pencolor(255,155,192)
        t.seth(10)
        t.begin_fill()
        t.circle(5)
        t.color(160,82,45)
        t.end_fill()  #外形填充的结束标志
 
    #头
    def head(self):
        t.color((255,155,192),"pink")
        t.pu()
        t.seth(90)
        t.fd(41)
        t.seth(0)
        t.fd(0)
        t.pd()
        t.begin_fill()
        t.seth(180)
        t.circle(300,-30)
        t.circle(100,-60)
        t.circle(80,-100)
        t.circle(150,-20)
        t.circle(60,-95)
        t.seth(161)
        t.circle(-300,15)
        t.pu()
        t.goto(-100,100)
        t.pd()
        t.seth(-30)
        a = 0.4
        for i in range(60):
            if  0<=i<30 or 60<=i<90:
                a = a+0.08
                t.lt(3) #向左转3度
                t.fd(a) #向前走a的步长
            else:
                a = a-0.08
                t.lt(3)
                t.fd(a)
        t.end_fill()
 
    #耳朵
    def ears(self):
        t.color((255,155,192),"pink")
        t.pu()
        t.seth(90)
        t.fd(-7)
        t.seth(0)
        t.fd(70)
        t.pd()
        t.begin_fill()
        t.seth(100)
        t.circle(-50,50)
        t.circle(-10,120)
        t.circle(-50,54)
        t.end_fill()
        t.pu()
        t.seth(90)
        t.fd(-12)
        t.seth(0)
        t.fd(30)
        t.pd()
        t.begin_fill()
        t.seth(100)
        t.circle(-50,50)
        t.circle(-10,120)
        t.circle(-50,56)
        t.end_fill()
 
    #眼睛
    def eyes(self):
        t.color((255,155,192),"white")
        t.pu()
        t.seth(90)
        t.fd(-20)
        t.seth(0)
        t.fd(-95)
        t.pd()
        t.begin_fill()
        t.circle(15)
        t.end_fill()
        t.color("black")
        t.pu()
        t.seth(90)
        t.fd(12)
        t.seth(0)
        t.fd(-3)
        t.pd()
        t.begin_fill()
        t.circle(3)
        t.end_fill()
        t.color((255,155,192),"white")
        t.pu()
        t.seth(90)
        t.fd(-25)
        t.seth(0)
        t.fd(40)
        t.pd()
        t.begin_fill()
        t.circle(15)
        t.end_fill()
        t.color("black")
        t.pu()
        t.seth(90)
        t.fd(12)
        t.seth(0)
        t.fd(-3)
        t.pd()
        t.begin_fill()
        t.circle(3)
        t.end_fill()
 
    #腮
    def cheek(self):
        t.color((255,155,192))
        t.pu()
        t.seth(90)
        t.fd(-95)
        t.seth(0)
        t.fd(65)
        t.pd()
        t.begin_fill()
        t.circle(30)
        t.end_fill()
 
    #嘴
    def mouth(self):
        t.color(239,69,19)
        t.pu()
        t.seth(90)
        t.fd(15)
        t.seth(0)
        t.fd(-100)
        t.pd()
        t.seth(-80)
        t.circle(30,40)
        t.circle(40,80)
 
    #身体
    def body(self):
        t.color("red",(255,99,71))
        t.pu()
        t.seth(90)
        t.fd(-20)
        t.seth(0)
        t.fd(-78)
        t.pd()
        t.begin_fill()
        t.seth(-130)
        t.circle(100,10)
        t.circle(300,30)
        t.seth(0)
        t.fd(230)
        t.seth(90)
        t.circle(300,30)
        t.circle(100,3)
        t.color((255,155,192),(255,100,100))
        t.seth(-135)
        t.circle(-80,63)
        t.circle(-150,24)
        t.end_fill()
 
    #手
    def hands(self):
        t.color((255,155,192))
        t.pu()
        t.seth(90)
        t.fd(-40)
        t.seth(0)
        t.fd(-27)
        t.pd()
        t.seth(-160)
        t.circle(300,15)
        t.pu()
        t.seth(90)
        t.fd(15)
        t.seth(0)
        t.fd(0)
        t.pd()
        t.seth(-10)
        t.circle(-20,90)
        t.pu()
        t.seth(90)
        t.fd(30)
        t.seth(0)
        t.fd(237)
        t.pd()
        t.seth(-20)
        t.circle(-300,15)
        t.pu()
        t.seth(90)
        t.fd(20)
        t.seth(0)
        t.fd(0)
        t.pd()
        t.seth(-170)
        t.circle(20,90)
 
    #脚
    def feet(self):
        t.pensize(10)
        t.color((240,128,128))
        t.pu()
        t.seth(90)
        t.fd(-75)
        t.seth(0)
        t.fd(-180)
        t.pd()
        t.seth(-90)
        t.fd(40)
        t.seth(-180)
        t.color("black")
        t.pensize(15)
        t.fd(20)
        t.pensize(10)
        t.color((240,128,128))
        t.pu()
        t.seth(90)
        t.fd(40)
        t.seth(0)
        t.fd(90)
        t.pd()
        t.seth(-90)
        t.fd(40)
        t.seth(-180)
        t.color("black")
        t.pensize(15)
        t.fd(20)
 
if __name__ == '__main__':
    peppaPig()
