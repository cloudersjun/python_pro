# coding:utf-8
class RBTree:
    def __init__(self):
        self.nil = RBTreeNode(0)
        self.root = self.nil


class RBTreeNode:
    def __init__(self, x):
        self.key = x
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'black'


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


array = [1, 3, 2, 4, 11, 5, 56, 23, 9]
tree = RBTree()
merge_size = 2
begin = "true"
order = "asc"
st = Stack()
temp = list()
for i in xrange(0, len(array)):
    # print array[i]
    if begin == "true":
        temp = list()
        temp.append(array[i])
        st.push(temp)
        begin = "false"
        if array[i] < array[i + 1]:
            order = "asc"
        else:
            order = "desc"
    else:
        temp = st.pop()
        temp.append(array[i])
        if i == len(array) - 1:
            st.push(temp)
            continue
        if array[i] < array[i + 1] and order == "desc":
            begin = "true"
        elif array[i] > array[i + 1] and order == "asc":
            begin = "true"
        else:
            begin = "false"
        st.push(temp)
print st.l
