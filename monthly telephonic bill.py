calls=int(input("enter no. of calls:"))
bill=200
if 0<calls<100:
    print("your phone bill is RS",bill)
elif 100<calls<150:
    a=calls-100
    bill=bill+a*.60
    print("your phone bill is RS",bill)
elif 150<calls<200:
    a=calls-150
    bill=bill+30+a*.50
    print("your phone bill is RS",bill)
else:
    a=calls-200
    bill=bill+55+a*.40
    print("your phone bill is RS",bill)
