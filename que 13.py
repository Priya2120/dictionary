# Ek code likhiye jo dictionary ki 3 highest value print karaye. 

 
my_dict = {
    'a':50, 
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20
    }
list1=[]
for i in my_dict:
    list1.append(my_dict[i])
# print(list1)
list1.sort(reverse=True)
# print(list1)
j=0
while j<3:
    for i in my_dict:
        if my_dict[i]==list1[j]:
            print(i)
    j=j+1





# print(sorted(my_dict[]))



# a=[]
# for i in my_dict:
#     a.append(i)
# b=[]
# for i in range(3):
#     b.append(max(a))
#     a.remove(max(a))
# print(sorted(b))




# for i in my_dict.values():
#     a.append(i)
# b=[]
# for i in range(3):
#     b.append(max(a))
#     a.remove(max(a))
# print(b)