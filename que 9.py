# "MISSISSIPPI" iss word me har letter ki occurrency count karke ek 
# dictionary me store karaye. Jisme letter dictionary ki keys aur 
# occurrency Uss dictionary ki values hongi. 


# a="MISSISSIPPI"
# b={}
# for i in a:
#     if not in b:
#         a[i]=1
#     else:
#         a[i]+=1
# print(b)

a="MISSISSIPPI"
new={}
for i in a:
    if i not in new:
        new[i]=1
    else:
        new[i]+=1
print(new)
