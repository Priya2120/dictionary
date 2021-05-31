# Ek program likho jo ki dictionaries ki values ko sort(ascending or descending) 

dict={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
sorted_values=sorted(dict.values())
sorted_dict={}
for i in sorted_values:
    for k in dict.keys():
        if dict[k]==i:
            sorted_dict[k]=dict[k]
            break
print(sorted_dict)