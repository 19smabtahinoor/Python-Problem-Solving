# Problem : Remove Duplicate

def remove_duplicate(items):
  unique=[]
  for item in items:
    if item not in unique:
      unique.append(item)
  return unique

numbers = [1,2,2,66,3,35,35436,46,67]
print(remove_duplicate(numbers))
