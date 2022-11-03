total = int(input())

result = []

for i in range(total):
  text = list(input())
  plus = 0
  cnt=0
  score=0

  for j in range(len(text)):
    # print("score",score)
    if text[j] == 'O':
      plus += 1
      cnt += plus
      # print("Oplus",plus)
      # print("Ocnt",cnt)
    if text[j] == 'X':
      score += cnt
      cnt = 0
      plus = 0
      # print("Xplus",plus)
      # print("Xcnt",cnt)
    if j == len(text)-1:
      score += cnt
      cnt = 0
      result.append(score)


for i in range(len(result)):
  print(result[i])
      
# 변수가 많으면 print로 변수추적하기를 주저하지 말자!