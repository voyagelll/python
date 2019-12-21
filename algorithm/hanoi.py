# def hanoi(n, a, b, c):
#     if n == 1:
#         print(a, '-->', c)
#     else:
#         hanoi(n-1, a, c, b)
#         print(a, '-->', c)
#         hanoi(n-1, b, a, c)


# hanoi(2, 'A', 'B', 'C')

"""
a 》 b
a > c
b > c
"""

def hanoi2(n, a, b, c):
    if n == 1:
        print(a, '->', c)
    else:
        hanoi2(n-1, a, c, b)
        print(a, '->', c)
        hanoi2(n-1, b, a, c)

hanoi2(3, 'a', 'b', 'c')