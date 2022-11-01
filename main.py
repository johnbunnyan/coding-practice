loop = int(input())

arr =  list(map(int,input().split()))

result=[]

min = arr[0]
max = arr[0]

for i in range(1,loop):

  if arr[i] < min:
    min = arr[i]
  elif arr[i] > max:
    max = arr[i]
    

print(str(min) + ' ' + str(max))


