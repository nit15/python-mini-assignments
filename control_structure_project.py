print("1. type code B for budget ")
print("2. type code D for daily")
print("3. type Q for halt")
print("         ", end="TYPE HERE YOUR CLASSIFICATION CODE\n")
code=input("customer code :")
while code!='Q':

 print("          ", end="CUSTOMER DETAILS :\n")
 a=int(input("number of days :"))
 b=int(input('odometer reading at start :'))
 c=int(input("odometer reading at end :"))
 s1=b/10
 e1=c/10
 mile = e1-s1
 if code=='B' :
  bill=(mile*0.25)+(a*40)
 elif code=='D' :
  if mile>100 :
   bill=(mile-(a*100))*0.25+a*60
  else :
    bill=a*60
 else :
   print("enter valid Customer classification code")

 print("          ", end="CUSTOMER SUMMARY :\n")
 print("Customer classification code :", code)
 print("Rental period (DAYS) :\n", a)
 print("Odometer reading at start :\n", b)
 print("Odometer reading at end :\n", c)
 print("Amount due: \n$", bill, "\n\n")
 code = input("customer code :")

