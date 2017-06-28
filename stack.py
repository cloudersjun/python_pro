# coding:utf-8
class Stack:
    l = list()

    def __init__(self):
        self.l = list()

    def pop(self):
        item = self.l[len(self.l) - 1]
        self.l.remove(item)
        return item

    def push(self, a):
        self.l.append(a)


stack = Stack()
array = [1, 2, 3, 4, 5, 6]
for i in array:
    stack.push(i)
while len(stack.l) > 0:
    print stack.pop()
