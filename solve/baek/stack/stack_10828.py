
def solve():
  length = int(input())
  stack = []

  for i in range(length):
    command = input()
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
      stack_top = stack[-1]
      print(stack_top)

    elif check[0] == 'size':
      stack_len = len(stack)
      print(stack_len)

    elif check[0] == 'empty':
      stack_len = len(stack)
      if stack_len == 0:
        print(1)
      else:
        print(0)
    

    
  return check