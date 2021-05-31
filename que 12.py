# # Ek program likhiye jo:- Ek dictionary me 1 se 15 tak saare numbers ki 
# # keys banaye aur unke square unn keys ki values ho.

# dict={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
# for i in range(1,16):
#     dict[i]=i*i
# print(dict)


dict={}
x=0
for  i in range(1,16):
    i=i**2
    x+=1
    dict.update({x:i})
print(dict)