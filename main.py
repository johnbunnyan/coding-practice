first = int(input())
second = input()
second_last = int(second[-1])
second_mid = int(second[-2])
second_first = int(second[-3])

# print(second_last)
# print(second_mid)
# print(second_first)

third=first * second_last
forth=first * second_mid * 10
fifth=first * second_first * 100
sixth=third+forth+fifth

print(third)
print(forth // 10)
print(fifth // 100)
print(sixth)


