import sys

total = int(sys.stdin.readline().rstrip())

for i in range(total):
  # 한개짜리는 잘 받을 수 있다.
  # a = int(sys.stdin.readline().rstrip())
  # print("ww",type(a))

  # 한 줄에 두개짜리 받기(한번에 1,2 수행하지 않기!)
 # 1. 일단 입력받기
   a = sys.stdin.readline().rstrip()
  # 2. 입력받은 문자열 나누고 int 매핑
  b, c = map(int, a.split())
   print(b+c)




