list1=[3,1,4]
list2=[1,5,9]
list3=[]
if list1.__len__()<=list2.__len__():
    for i in range(0,list1.__len__()):
        list3.append(list1[i]+list2[i])
else:
    for i in range(0, list2.__len__()):
        list3.append(list1[i] + list2[i])
print(list3)