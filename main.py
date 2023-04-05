# num은 순서
num = int(input())

def fib_rec(num):
  if num < 1:
    return 0
  elif num == 1:
    return 1
  return fib_rec(num-1) + fib_rec(num-2)

print(fib_rec(num))
  

