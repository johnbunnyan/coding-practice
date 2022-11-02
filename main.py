divided = []

for i in range(10):
  num = int(input())
  divide = num % 42
  divided.append(divide)

unique = set(divided)
ln = len(unique)

print(ln)


# <set사용>
# names = ['Barry', 'Alice', 'Bob', 'Bob']

# unique_names = set(names)
# Result:
# {'Alice', 'Barry', 'Bob'}