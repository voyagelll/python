"""
	杨辉三角形
"""
def triangles():
    pass


"""
	斐波拉契亚数列
"""
def fib(max):
    a, b = 0, 1
    while max:
        # print(b, end=" ")
        yield b
        a, b = b, a+b
        max -= 1


if __name__ == '__main__':
    for i in fib(6):
        print(i)