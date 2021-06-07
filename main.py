def get_sums(nums):
  sum = 0
  for num in nums:
    sum = num + sum
  return sum

nums = [1,2,3,4,5]
total = get_sums(nums)
print('Total number is',total)