import sys

stack = []


while True:
  elem = list(sys.stdin.readline().rstrip())
  if elem[0] == '.':
    break
  
  for unit in elem:
    if unit == '(':
      stack.append('(')
    elif unit == '[':
      stack.append('[')

    if unit == ')':
      if len(stack) != 0 and stack[-1] == '(':
        stack.pop()
      elif len(stack) == 0 or stack[-1] == '[':
        stack.append(')')
  
      
        
    elif unit == ']':
      if len(stack) != 0 and stack[-1] == '[':
        stack.pop()
      elif len(stack) == 0 or stack[-1] == '(':
        stack.append(']')

        
      
  # print(stack)
  if len(stack) == 0:
    print('yes')
    stack = []
  else:
   print('no')
   stack = []


   



