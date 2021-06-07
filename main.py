# Problem : Vowels Count

def count_variables(sentence):
  vowels=['a','e','i','o','u','A','E','I','O','U']
  count = 0
  for char in sentence:
    if char in vowels:
      count = count +1
  return count
  
print(count_variables(input("Write your name : ")))
