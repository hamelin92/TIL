import sys


class Stack:
    data = []
    
    def push(self, x):
        self.data.append(x)
    
    def pop(self):
        if self.data:
            return self.data.pop()
        return -1

    def size(self):
        return len(self.data)

    def empty(self):
        if self.data:
            return 0
        return 1

    def top(self):
        if self.data:
            return self.data[-1]
        return -1


N = int(sys.stdin.readline())
stack = Stack()
methods = {"push": stack.push, "pop": stack.pop, "size": stack.size, "empty": stack.empty, "top": stack.top}
inputs = [sys.stdin.readline().split() for _ in range(N)]
for i in inputs:
    if len(i) > 1:
        methods[i[0]](i[-1])
    else:
        print(methods[i[0]]())
