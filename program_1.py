
def enter_data(reply):
    if reply=="yes":
     ans=int(input("enter number:"))
     return ans
    elif reply=="no":
     print("program terminated successfully")
     return 0
    else :
        print("Wrong input")


list=[int(input("Enter no.:"))]
rpl=input("Do you want to continue ? : (yes/ no)")
while rpl!="no":
 list.append(enter_data(rpl))
 rpl = input("Do you want to continue ? : (yes/ no)")
print("LIST:" , list)
print("LAST ITEM :", list.__getitem__(-1))
list.reverse()
print("REVERSE ORDER :", list )
#check list contains 5
if list.__contains__(5):
 print("yes")
else:
    print("no")
# no. of 5's
n=0
for no in list:
 if no==5:
     n+=1
print("no of 5's in list:", n)
#remove first and last element and sort the list
list.pop(0)
list.pop()
list.sort()
print(list)
#print less then no. of 5
c=0
for no in list:
    if no<5:
     c+=1
print("no. of number less than 5:", c)

