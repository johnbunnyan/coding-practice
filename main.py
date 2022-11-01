loop = int(input())
# list()안쓰면 객체로 취급, list써줘야 인덱싱가능
arr =  list(map(int,input().split()))
target = int(input())

cnt = 0

for i in range(loop):

  if arr[i] == target:
    cnt += 1


print(cnt)


