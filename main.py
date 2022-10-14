h, m = map(int,input().split())

# 시간 -> 분
hourTomin = h * 60
total = hourTomin + m

# 전체 - 45
adjust = total - 45

# 분 -> 시간
resultH = adjust // 60

if resultH < 0:
  resultH += 24
resultM = adjust % 60

print(str(resultH)+' '+str(resultM))

