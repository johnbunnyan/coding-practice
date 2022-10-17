n = int(input())

for i in range(n):
  for j in range(i+1):
    # 두번째 파라미터 end
    # (참고)https://www.daleseo.com/python-print/
    print('*', end='')
  if(i != n): print('')