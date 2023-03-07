# 예제 보면서 패턴 파악
# 정답인 예제와 오답인 예제의 차이 도출하기
# 오답 케이스
# (()) ())
# (() ((()) () (
# (())()))
# (()
# (과 )의 짝이 맞아야 한다

# 정답 케이스
# (()()) ((()))
# () () () () (()()()) ()
# (())()
# ((()))

# 인간 뇌피셜(나의 방식)으로 문제풀기


# 코드 로직으로 옮기기
# (가 나오면 스택으로 쌓는다
# )가 나오기 시작하면 )만 연달아 나와야한다
# 그리고 그 개수가 (가 쌓인 개수와 같아야 한다
# 짝이 맞으면 초기화
# 초기화했는데 (가 아니라 )가 나오면 탈락

import sys
length = int(input())

stack = []

for i in range(length):
  elem = list(sys.stdin.readline().strip())

  for unit in elem:
    if unit == '(':
      stack.append('(')
  
    elif unit == ')':
      if len(stack) != 0 and stack[-1] == '(':
        stack.pop()
      elif len(stack) == 0:
        stack.append(')')

  if len(stack) == 0:
    print('YES')
    stack = []
  else:
   print('NO')
   stack = []


   



