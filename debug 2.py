# Niche ek program hai jisme keys 1 se lekar 15 ke beech main hai 
# aur values keys ka square hai jaise ki. Output kuch 
# esha hona chahiye :- ab aapko is program ko theek karna hai.


dict={}
x=0
for  i in range(1,16):
    i=i**2
    x+=1
    dict.update({x:i})
print(dict)