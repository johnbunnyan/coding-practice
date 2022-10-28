n = int(input())

for i in range(n):
  for j in range(n-1,-1,-1):
    #end키워드를 쓰면 print를 해도 다음줄로 넘어가지 않는다
  
    if i>=j: print("*", end='')
    else: print(' ',end='')
  if(i != n): print('')


# 문제는 다 풀 수 있다
# 못 푸는 건 게을러서다
# 패턴을 하나하나 적고
# 규칙을 파악하면 다 풀 수 있는 것
# 그래도 안되면 검색하면 다 됨
# ->
# https://codingcoding.tistory.com/1103#h_11