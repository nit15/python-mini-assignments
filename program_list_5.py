list1=[]
list2=[]
ans="yes"
#list1.append(input("enter name:"))
while ans!="no" or ans=="yes":
    list1.append(input("enter name:"))
    ans=input("do you want to enter more names? (yes/no)")

print(list1)
for name in list1:
    list2.append(name[1:])

print(list2)