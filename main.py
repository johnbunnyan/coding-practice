length = int(input())


def recursion(s, l, r, count):
    count = count+1
    if l >= r: return 1, count
    elif s[l] != s[r]: return 0, count
    else: return recursion(s, l+1, r-1,count)

def isPalindrome(s):
    count = 0
    return recursion(s, 0, len(s)-1, count)
  
for i in range(length):
  target = input()
  print(str(isPalindrome(target)[0]) + ' '+ str(isPalindrome(target)[1]))

