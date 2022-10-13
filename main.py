A, B, C = list(map(int, input().split()))

# (A+B)%C
# ((A%C) + (B%C))%C
# (A×B)%C
# ((A%C) × (B%C))%C 

first = (A+B)%C
second = ((A%C) + (B%C))%C
third = (A*B)%C
forth = ((A%C) * (B%C))%C 


print(first)
print(second)
print(third)
print(forth)
