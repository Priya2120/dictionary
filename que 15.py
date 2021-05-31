# Ask user to give name and marks of 10 different students. Store them in dictionary.

dictionary = {}
count = 0
while count < 5:
   name = input("Enter your name: ")
   mark = input("Enter your mark out of 100: ")
   if name not in dictionary:
       dictionary[name] = mark
       count = count + 1
   else:
       name = input("Enter a unique name: ")
       mark = input("Enter the mark out of 100: ")
       if name not in dictionary:
          dictionary[name] = mark
          count = count + 1

print (dictionary)
