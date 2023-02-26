import sys

N = int(sys.stdin.readline())

class MyQueue:
    max_size = N
    start = 1
    end = 0
    data = [None for _ in range(N)]

    def push_front(self, x):
        self.start = (self.start - 1)%self.max_size
        self.data[self.start%self.max_size] = x
    
    def push_back(self, x):
        self.end = (self.end + 1)%self.max_size
        self.data[self.end%self.max_size] = x

    def pop_front(self):
        if (self.end - self.start+1)%self.max_size != 0:
            res = self.data[self.start%self.max_size]
            self.data[self.start%self.max_size] = None
            self.start = (self.start + 1)%self.max_size
            return res
        return -1

    def pop_back(self):
        if (self.end - self.start+1)%self.max_size != 0:
            res = self.data[self.end%self.max_size]
            self.data[self.end%self.max_size] = None
            self.end = (self.end - 1)%self.max_size
            return res
        return -1

    def size(self):
        return (self.end - self.start+1)%self.max_size

    def empty(self):
        if (self.end - self.start+1)%self.max_size != 0:
            return 0
        return 1

    def front(self):
        if (self.end - self.start+1)%self.max_size != 0:
            return self.data[self.start]
        return -1
    
    def back(self):
        if (self.end - self.start+1)%self.max_size != 0:
            return self.data[self.end]
        return -1


my_queue = MyQueue()
methods = {
    "push_front": my_queue.push_front,
    "push_back": my_queue.push_back,
    "pop_front": my_queue.pop_front,
    "pop_back": my_queue.pop_back,
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