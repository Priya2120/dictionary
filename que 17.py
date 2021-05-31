# Use dictionary to store antonyms of words. E.g.- 'Right':'Left', 'Up':'Down', etc. 
# Display all words and then ask user to enter a word and display antonym of it.

word = {'right':'left','up':'down','good':'bad','cool':'hot','east':'west'}
print ("Enter any word from following words")
for i in word.keys():
    print(i)
y = input("enter the key :- ")
if y in word :
    print('antonym is ', word[y])
else:     
    print('not in the list given :')


  


