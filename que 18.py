 # Count the number of occurrence of each letter in word "MISSISSIPPI". 
 # Store count of every letter with the letter in a dictionary.

a="MISSISSIPPI"
new={}
for i in a:
    if i not in new:
        new[i]=1
    else:
        new[i]+=1
print(new)
