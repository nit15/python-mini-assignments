list1=[]
list2=[]
list3=[]
i=0
for i in range(0,50):
    list1.append(i)

print(list1)
i=1
for i in range(1,51):
    list2.append(i*i)
print(list2)
i=1
l=97
for i in range(1,27):
    list3.append(chr(l)*i)
    l+=1

print(list3)