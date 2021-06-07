
# solution 1 
def get_sums(nums):
  sum = 0
  for num in nums:
    sum = num + sum
  return sum

nums = [1,2,3,4,5]
total = get_sums(nums)
print('Total number is',total)


# solution 2
nums = [1,2,3,4,5,6,7,8,9,10]
total = sum(nums)
print(total)