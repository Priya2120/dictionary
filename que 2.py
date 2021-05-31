# Ek program likhiye jisse ki agar di hui key pehle se dictionary me 
# exist karti ho toh “exists “ print kare aur agar nahi karti ho toh 
# “not exists” print kare. Example :-

dict={"name":"Raju","mark":56}
key_name=input("enter the key name :-")
if key_name in dict:
    print("exist")
else:
   print("not exist")