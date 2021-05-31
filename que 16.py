# Sort the dictionary created in previous example according to marks.

D = {}
n = int(input('How many student record you want to store?? '))
ls = []
for i in range(0, n):
    num = input("Enter the student name and it's percentage: ").split()
    ls.append((num))
ls = sorted(ls, reverse = True)
print('Sorted list of students according to their marks in descending order')
for i in ls:
    print(i[1],i[0])