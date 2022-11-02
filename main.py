total = int(input())
arr = list(map(int, input().split()))

arr.sort()

max = arr[-1]

newArr = []

for i in range(len(arr)):
  newNum = arr[i]/max*100
  newArr.append(newNum)

avg = sum(newArr)/len(newArr)
print(avg)

