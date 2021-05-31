# Ek dictionary ki value ke sabhi items ko count kijiye jo ki ek list me hai. 

dict =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
count=0
for i in dict:
    count=count+len(dict[i])
print(count)