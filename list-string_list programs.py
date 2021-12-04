'''
nitya parikh
no: 9173314024
'''
list=[1,2,3,4]
list2=["nitya","parth"," ","kalpin","parth","mohit","nitya","kalpin","mohit","nitya","parth","kalpin","nitya"," "]

#1
list[0],list[-1]=list[-1],list[0]
print(list)

#2
i=int(input("enter index no. that you want to raplce:"))
m=int(input("enter second no. index that you want top replace with"))
list[i-1],list[m-1]=list[m-1],list[i-1]
print(list)

#3
print(list2)
word=input("enter word that is present in list : ")
i=int(input("Enter no. of occurance of word that you want to remove : "))
count=0
list3=[]
for item in list2:
    list3.append(item)
    if item==word:
        count+=1
    if count==i:
      list3.pop()
      count+=1
list2=list3
print(list2)

#4
print(len(list))

#5
element=input("enter any name to check it's present in the list or not :")
if list2.__contains__(element):
    print("it's exists")
else:
    print("doesn't exist")

#6
list.clear()
'''
for item in list:
 list.remove(item)
print(list)
'''

#7
list=[1,2,3,4]
list.reverse()
print(list)

#8
list4=list2.copy()
print(list4)

#9
word=input("enter word that is present in list : ")
count=0
for item in list2:
    if item==word:
        count+=1
print("occurance of"+""+word+":",count)

#10
sum=sum(list)
print(sum)

#11
i=1
for item in list:
    i=item*i
print(i)

#12
print("smallest no. in a list:", min(list))

#13
print("largest no. in a list:", max(list))

#14
print(list)
max=list[0]
sec_max=0
for i in range(1,len(list)):
    if list[i]>max:
        sec_max=max
        max = list[i]
print("second largest element in the list",sec_max)

#15




#16 & #17
print(list)
for item in list:
    if item%2==0:
        print("even no.s:",item)
    else:
        print("odd no.s :",item)
#18 & #19 & #20
odd=[]
even=[]
start_point=int(input("enter start point:"))
end_point=int(input("enter ending point:"))
for i in range(start_point, end_point ):

    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even no.s:",even)
print("total even no.s:",len(even))
print("odd no.s:", odd)
print("total odd no.s:",len(odd))

#26
list5=[1,2,3,4,5,6,7,8]
list5.remove(1)

#27
for item in list2:
    if item==" ":
      list2.remove(item)
print(list2)

#28
duplicates=[]
list6=[1,2,5,6,2,1,4,8,5,6]

for i in range(0,len(list6)):
    for j in range(i+1,len(list6)):
        if list6[i]==list6[j] and duplicates.count(list6[i])<1:
            duplicates.append(list6[i])

print("duplicates of integer list:", duplicates)

#29
print(list)
sum=0
for item in list:
    sum=sum+item
print("cumulative sum:",sum)

#30
new_list=[]
n=int(input("Give size of list you want to do:"))
m=0

for i in range(0,len(list5)):
    new_list.append(list5[i+1:n+m])
    m+=n

print(new_list)