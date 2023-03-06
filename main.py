import sys
length = int(sys.stdin.readline().strip())

stack = []

for i in range(length):
  inputt = int(sys.stdin.readline().strip())
  if inputt != 0:
    stack.append(inputt)
  else:
    stack.pop()

sum = sum(stack)
print(sum)
