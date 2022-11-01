loop, condition = map(int,input().split())

arr =  list(map(int,input().split()))

result=[]

for i in range(loop):

  if arr[i] < condition:
    result.append(arr[i])
    

resultToStr=' '.join(str(e) for e in result)
print(resultToStr)


