'''
Name: Nitya Parikh
Batch: 12-2
Ph No.: 9173314024
Program : 6
'''

number=int(input("Enter number:"))
def cube(number):
 c=number*number*number
 print(c)

def by_three(number):
    if number%3==0:
        cube(number)
    else:
        print("false")

while(number<0):
    print("you enter negative number please enter positive number")
    number=int(input("Enter number:"))
    by_three(number)