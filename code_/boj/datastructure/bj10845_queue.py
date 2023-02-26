'''
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
import sys

class MyQueue:
    pointer = 0
    data = []

    def push(self, x):
        self.data.append(x)
    
    def pop(self):
        if self.pointer < len(self.data):
            res = self.data[self.pointer]
            self.data[self.pointer] = None
            self.pointer += 1
            return res
        return -1

    def size(self):
        return len(self.data)-self.pointer

    def empty(self):
        if self.pointer < len(self.data):
            return 0
        return 1

    def front(self):
        if self.pointer < len(self.data):
            return self.data[self.pointer]
        return -1
    
    def back(self):
        if self.pointer < len(self.data):
            return self.data[-1]
        return -1


N = int(sys.stdin.readline())
my_queue = MyQueue()
methods = {
    "push": my_queue.push,
    "pop": my_queue.pop, 
    "size": my_queue.size, 
    "empty": my_queue.empty, 
    "front": my_queue.front,
    "back": my_queue.back
    }
inputs = [sys.stdin.readline().split() for _ in range(N)]
for i in inputs:
    if len(i) > 1:
        methods[i[0]](i[-1])
    else:
        print(methods[i[0]]())