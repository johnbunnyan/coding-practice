nums = list(map(int, input().split()))


for i in range(len(nums)):
  if i == 0 or i == 1 : 
    nums[i] = 1 - nums[i]

  elif i == 2 or i == 3 or i == 4 : nums[i] = 2 -nums[i]
      
  elif i == 5 :
      nums[i] = 8 -nums[i]
 
stringfy = ' '.join(map(str,nums))
print(stringfy)
