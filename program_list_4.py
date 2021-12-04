i=0
list=[]
for i in range(0,12):
 list.append(int(input("Enter no. beetween 1 to 12:")))
 i+=1
for no in list:
     if no>10:
       list[list.index(no)]=10


print(list)