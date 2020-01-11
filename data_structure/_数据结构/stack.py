"""
    栈（堆栈）
        - 允许插入删除操作的一端称为栈顶，另一端为栈低，只允许在一端进行操作。
          按照先进先出的原理运作
"""

class Stack(object):
    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    # 入栈
    def push(self, data):
        if len(self.stack) >= self.limit:
            raise IndexError('超出栈容量限制')
        self.stack.append(data)

    # 出栈
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError('pop from an empty stack')

    # 查看栈顶元素
    def peek(self):
        if self.stack:
            return self.stack[-1]

    # 判断是否为空
    def is_empty(self):
        return not bool(self.stack)

    # 返回大小
    def size(self):
        return len(self.stack)



"""
    检查括号是否完全匹配
"""
def check_parentheses(ex):
    stack = Stack()
    for i in ex:
        if i == '(':
            stack.push(i)
        elif i == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()


# print(check_parentheses('((()))'))
# print(check_parentheses('((())'))
# print(check_parentheses('(()))'))


"""
    后缀计算器
"""