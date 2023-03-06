# from solve.baek.stack.stack_10828 import solve



# if __name__ == "__main__":
#   solve()


# length = int(input())
# stack = []

# for i in range(length):
#     command = input()
#     check = command.split()

    
#     if check[0] == 'push':
#       stack.append(check[1])
    
#     elif check[0] == 'pop':
#       poped_len = len(stack)
#       if poped_len == 0:
#         print(-1)
#       else:
#         poped = stack.pop()
#         print(poped)

#     elif check[0] == 'top':
#       poped_len = len(stack)
#       if poped_len == 0:
#         print(-1)
#       else:
#         stack_top = stack[-1]
#         print(stack_top)

#     elif check[0] == 'size':
#       stack_len = len(stack)
#       print(stack_len)

#     elif check[0] == 'empty':
#       stack_len = len(stack)
#       if stack_len == 0:
#         print(1)
#       else:
#         print(0)


# class Stack:
#      def __init__(self):
#          self.items = []

#      def isEmpty(self):
#          return self.items == []

#      def push(self, item):
#          self.items.append(item)

#      def pop(self):
#          return self.items.pop()

#      def peek(self):
#          return self.items[len(self.items)-1]

#      def size(self):
#          return len(self.items)

#stack = Stack()
from collections import deque
import sys

stack = deque()
length = int(sys.stdin.readline().rstrip())

for i in range(length):
    command = sys.stdin.readline().rstrip()
    check = command.split()

    
    if check[0] == 'push':
      stack.append(check[1])
    
    elif check[0] == 'pop':
      poped_len = len(stack)
      if poped_len == 0:
        print(-1)
      else:
        poped = stack.pop()
        print(poped)

    elif check[0] == 'top':
      poped_len = len(stack)
      if poped_len == 0:
        print(-1)
      else:
        print(stack[-1])

    elif check[0] == 'size':
      print(len(stack))

    elif check[0] == 'empty':
      state = len(stack)
      if state == 0:
        print(1)
      else:
        print(0)
        