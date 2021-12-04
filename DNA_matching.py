from prog_lib import display
Str1=str(input("enter string 1:"))
Str2=input("enter string 2:")




def scoring(Str1,Str2,mismatch,matches):
    Str_new_1 = " "
    Str_new_2 = " "
    for item1, item2 in zip(Str1, Str2):
        if item1 == item2:
            Str_new_1 += Str1[Str1.index(item1)].lower()
            Str_new_2 += Str2[Str2.index(item2)].lower()
            matches += 1
        else:
            Str_new_1 += Str1[Str1.index(item1)].upper()
            Str_new_2 += Str2[Str2.index(item2)].upper()
            mismatch += 1
    print("Matching :",matches)
    print("Mismatching :",mismatch)
    print("STRING1 :",Str_new_1)
    print("STRING2 :",Str_new_2)


menu_dic = {"a": "add", "d": "delete", "s": "score", "q": "quit"}
display(menu_dic)
op = input("What do you want to do? :")
# Str="aabbcc"
# print(Str)

while(op!="q"):
 if op=="a":
     str_no=int(input("select String (1 / 2) :"))
     index=int(input("before which index? :"))
     if str_no==1:
        Str1=Str1[0:index].__add__("-")+Str1[index:]
     elif str_no==2:
         Str2=Str2[0:index].__add__("-")+Str2[index:]
     display(menu_dic)
     op= input("What do you want to do? :")

 elif op=="d":
     str_no = int(input("select String (1 / 2) :"))
     index = int(input("which index? :"))
     if str_no == 1:
       if Str1.__getitem__(index)=="-":
           Str1=Str1[0:index]+Str1[index+1:]
     elif str_no == 2:
       if Str2.__getitem__(index)=="-":
           Str2 = Str2[0:index] + Str2[index + 1:]
     display(menu_dic)
     op = input("What do you want to do? :")

 elif op=="s":
     matches=0
     mismatch=0
     if len(Str1)==len(Str2):
        scoring(Str1,Str2,mismatch,matches)
        display(menu_dic)
        op = input("What do you want to do? :")

     elif len(Str1)<len(Str2):
         for range in (len(Str1), len(Str2)):
             Str1 += "-"
         scoring(Str1, Str2, mismatch, matches)
         display(menu_dic)
         op = input("What do you want to do? :")

     else :
         for range in (len(Str2), len(Str1)):
             Str2 += "-"
         scoring(Str1, Str2, mismatch, matches)
         display(menu_dic)
         op = input("What do you want to do? :")

 elif op=="q":
     print("program terminated")

 else:
     print("wrong input try again")
     display(menu_dic)
     op = input("What do you want to do? :")
