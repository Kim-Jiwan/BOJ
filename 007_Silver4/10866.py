import sys

class Deque:
    def __init__(self):
        self.__deque = []

    def __str__(self):
        return f"{self.__deque}"

    def push_front(self, x):
        self.__deque.insert(0, x)

    def push_back(self, x):
        self.__deque.append(x)

    def pop_front(self):
        if self.__deque:
            print(self.__deque[0])
            self.__deque.pop(0)
        else:
            print(-1)

    def pop_back(self):
        if self.__deque:
            print(self.__deque[-1])
            self.__deque.pop()
        else:
            print(-1)

    def size(self):
        print(len(self.__deque))

    def empty(self):
        if self.__deque:
            print(0)
        else:
            print(1)
        
    def front(self):
        if self.__deque:
            print(self.__deque[0])
        else:
            print(-1)

    def back(self):
        if self.__deque:
            print(self.__deque[-1])
        else:
            print(-1)

input = sys.stdin.readline
deque = Deque()
N = int(input())

for _ in range(N):
    instruction = input().rstrip()

    if instruction[0:4] == 'push':
        push = list(instruction.split())

        if push[0] == "push_front":
            deque.push_front(int(push[1]))
        elif push[0] == "push_back":
            deque.push_back(int(push[1]))

    elif instruction == "pop_front":
        deque.pop_front()
    elif instruction == "pop_back":
        deque.pop_back()
    elif instruction == "size":
        deque.size()
    elif instruction == "empty":
        deque.empty()
    elif instruction == "front":
        deque.front()
    elif instruction == "back":
        deque.back()