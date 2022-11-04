# 1
# 1+1=2 $
# 3
# 2+2=4 $
# 5
# 3+3=6 $
# 7
# 4+4=8 $
# 9
# 5+5=10 $
# 10+1+0=11 @
# 6+6=12 $
# 11+1+1=13 @
# 7+7=14 $
# 12+1+2=15 @
# 8+8=16 $
# 13+1+3=17 @
# 9+9=18 $
# 14+1+4=19 @
# 20 
# 15+1+5=21 @
# 20+2+0=22 !
# 16+1+6=23 @
# 21+2+1=24 !
# 17+1+7=25 @
# 22+2+2=26 !
# 18+1+8=27 @
# 23+2+3=28 !
# 19+1+9=29 @
# 24+2+4=30 !
# 31
# 25+2+5=32 !
# 30+3+0=33 %
# 26+2+6=34 !
# 31+3+1=35 %

# 1)
# 11 간격으로 나오는 줄 알았는데 중간에 텀이 바뀐다.
#   -> 셀프 넘버가 아닌 것의 패턴은 안다

# a + a[0]+a[1]+[..] = b

# 셀프넘버가 아닌 것들을 배열에 모아둔다

# 2)
# 반복문 돌면서 셀프넘버 아닌 애들이 아닌 수를 출력

def d(n):
  toStr=str(n)
  next=n
  for i in range(len(toStr)):
      # print(i)
      # print("next",next)
      # print("add",toStr[i])
      next += int(toStr[i])
      # print("after",next)

  return next      


unSelfs=[]

for i in range(1,10000):
  nextNum = d(i)
  if nextNum < 10000 and nextNum != 0:
    unSelfs.append(nextNum)


for i in range(1,10000):
  if i not in unSelfs:
    print(i)

    
