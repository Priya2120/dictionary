# User se 10 students ke naam aur marks lekar unhe ek dictionary me store karaye. Output :- 

i=1
a=[]
b=[]
while i<11:
    student_name=input("enter the name :-")
    marks=input("enter the marks :-")
    a.append(student_name)
    b.append(marks)
    i+=1
dic={}
j=0
e=[]
while j<len(a):
    d=a[j],b[j]
    j+=1
    e.append(d)
dic.update(e)
print(dic)