
while True:
  try:
    num1, num2 = map(int, input().split())
    print(num1 + num2)
  except EOFError:
    break


# 검색으로 해결
# 파이썬 입력이 끝날때까지 받는 경우(End Of File, EOFerror)
# https://velog.io/@kimjhq1/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5%EC%9D%B4-%EB%81%9D%EB%82%A0%EB%95%8C%EA%B9%8C%EC%A7%80-%EB%B0%9B%EB%8A%94-%EA%B2%BD%EC%9A%B0End-Of-File-EOFerror
