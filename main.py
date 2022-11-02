# 3
# 2
# 4
# 5
# 7
# 8
# 9
# 6
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
# 21
# 22
# 23
# 24
# 25
# 26
# 27
# 28
# 29




arr = []

for i in range(28):
  num = int(input())
  arr.append(num)

arr.sort()
# print(arr)
result = []

for i in range(1,31):
  if i not in arr:
    print(i)
  

# <리스트 정렬 하기 - sort>
# https://blockdmask.tistory.com/564
    
# <리스트 안에 어떤 요소 있는지 체크 - not in>  https://pydole.tistory.com/entry/Python-%ED%8F%AC%ED%95%A8Containment-%EC%97%B0%EC%82%B0%EC%9E%90-in-not-in
