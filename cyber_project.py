from prog_lib import *

string="abcdefghijklmnopqrstuvwxyz"
op_dic={"e":"encode","d":"decode","q":"exit"}
display(op_dic)
command=input("Enter your command: ")
while(command.lower()!="exit"):

    if command.lower()=="e":
     str_4_encode=input("enter your String: ")
     n=int(input("Enter no. of rotation that you want : "))
     new_string=string[n:]+string[0:n]
     encoded_string=" "
     for i in range(0,len(str_4_encode)):
        if str_4_encode[i] != " ":
            if str_4_encode[i].isupper():
                encoded_string += str_4_encode[i]
            for w in range(0,len(string)):

             if str_4_encode[i]==string[w]:
               encoded_string+=new_string[w]
        else:
           encoded_string+=str_4_encode[i]
     print(encoded_string)

    elif command.lower()=="d":
        str_4_decode=input("Enter your String: ")
        one_word=input("Give one word of your String :")
        decoded_string = " "
        for i in range(0,len(str_4_decode)):
            for w in range(0,len(one_word)):
                if str_4_decode[i]==one_word[w]:
                    n=string.index(str_4_decode[i])-string.index(one_word[w])
                    print("Rotation of your String is :", n)
        for i in range(0, len(str_4_decode)):
         if str_4_decode[i] != " ":
            if str_4_decode[i].isupper():
                decoded_string += str_4_decode[i]
            for w in range(0, len(string)):

                    if str_4_decode[i]== string[w]:
                        decoded_string += string[w-n]
         else:
             decoded_string += str_4_decode[i]
        print("Your decoded string is :", decoded_string)
    elif command.lower()=="exit":
        print("you are exited")
    else:
        print("wrong command")
    command = input("Enter your command: ")