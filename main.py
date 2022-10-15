first, second, third = map(int,input().split())

reward = 0

if (first == second) and (second == third) and (first == third):
  reward = 10000+first*1000
  
elif (first == second != third) or (second == third != first) or (first == third != second):
  if first == second:
    reward = 1000+first*100
  elif second == third:
    reward = 1000+second*100
  elif first == third:
    reward = 1000+third*100

elif (first != second) and (second != third) and (first != third):
  largest = max(first, second, third)
  reward = largest * 100

print(reward)