# <노트>
# 1. 소수점 이후 자리 포메팅
# https://seopark.tistory.com/24
# 2. 반올림 메서드


total = int(input())

result = []

for i in range(total):
  spread = list(map(int,input().split(' ')))
  amount = spread[0]
  students = spread[1:]
  # print(amount)
  # print(students)
  avg = sum(students)/amount
  # print("avg",avg)

  # 평균넘는 학생 비율 = 평균넘는 수/전체수
  overed=0
  for j in range(amount):
    if students[j] > avg:
      overed += 1

    if j == amount-1:
      rate = round(overed/amount*100,3)
      formatting = format(rate,".3f")
      print(str(formatting)+'%')
    
    
  