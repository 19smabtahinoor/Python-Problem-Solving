# Problem : Word Count

user_Text = input("Write your bio:")
count = 0
for char in user_Text:
  if char == ' ':
    count = count + 1

count = count + 1
print(count)
