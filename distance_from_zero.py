'''
Name: Nitya Parikh
Batch: 12-2
Ph No. : 9173314024
Program no. : 3
'''

a=input()
def distance_from_zero(a):
    if a.isnumeric() or a.replace('.','',1).isdigit() :
     print(a)
    else:
        print("None")

distance_from_zero(a)