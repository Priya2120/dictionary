# Do lists lekar ek dictionary banaiye jisme pehli list ke elements 
# keys ho aur dusri list ke elements unn keys ki values ho. 


from typing import Dict


list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,] 
a={}
i=0
b=[]
while i<len(list1):
    c=list1[i],list2[i]
    b.append(c)
    i=i+1
a.update(b)
print(a)
    