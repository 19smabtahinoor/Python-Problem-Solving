
# solution 1 
def largest_num(nums):
  largest = nums[1]
  for num in nums:
    if num > largest:
      largest = num
  return largest
myNumbers = [1,2,3,4,5,55,-45]
print("Largest Number is ",largest_num(myNumbers))