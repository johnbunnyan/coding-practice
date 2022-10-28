origin = input()
originNum = int(origin)
if originNum < 10:
  origin = '0'+origin
first= origin[0] 
second= origin[1]

# newFirst=0
# newSecond=int(second)
new = ''
count = 0

while new != origin:
  add = int(first)+int(second)
  strAdd = str(add)
  if add < 10: strAdd = '0'+strAdd
  # print(strAdd,type(strAdd))
  new = second + strAdd[1]
  first = new[0]
  second = new[1]
  count += 1
  # print(new)


print(count)
  

