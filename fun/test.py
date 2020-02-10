import turtle as t 


t.pensize(4)
t.colormode(255)
t.color((255, 155, 192), 'pink')
t.speed(5)


def nose():
	t.pu()
	t.goto(-100, 100)
	t.pd()
	t.seth(-30)
	t.begin_fill()
	a = 0.4 
	for i in range(120):
		if 0<=i<30 or 60<=i<90:
			a = a+0.08
			t.lt(3)
			t.fd(a)
		else:
			a = a-0.08
			t.lt(3)
			t.fd(a)
	t.end_fill()


nose()
# t.lt(100)
t.exitonclick()