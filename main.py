# <노트>
# 1. 소수점 이후 자리 포메팅
# https://seopark.tistory.com/24
# 2. 반올림 메서드

def solve(a):
    ans = 0
    for i in range(len(a)):
        ans += a[i]
 
    return ans

print(solve([1,2,3]))