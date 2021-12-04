from personal_info import  Personal_Info
from product import Product
from sunshine_db import insertbillinfo

class Order(Personal_Info):
    billno=0
    billdate=""
    total_amount=0
    discount=0
    tax=0
    net_amount=0
    Product_List=0

    def setOrder(self,title,o_key):
        self.billno=int(input("Enter Bill No:"))
        self.billdate=input("Enter Bill Date :")

        self.setPersonal_Info(title);
        op="yes";
        self.Product_List=[];
        while op.lower()=="yes" :
            product=Product()
            product.setProduct(self.billno)
            self.total_amount += product.price
            self.Product_List.append(product)

            op=input("do you want to add another product(yes/no)?:")

        self.discount=float(input("Enter Discount (%):"))
        self.discount=(self.discount*self.total_amount)/100
        self.tax = float(input("Enter Tax (%):"))
        self.tax = (self.tax * self.total_amount) / 100
        self.net_amount=self.total_amount-self.discount+self.tax
        insertbillinfo(Personal_Info.id,self.billno,self.billdate,self.discount,self.tax,self.net_amount,o_key)


    def getOrder(self,title):
        print("Bill No:",self.billno)
        print("Bill Date :",self.billdate)
        self.getPersonal_Info(title)

        print("Id \t Name \t Qty \t Rate \t Price ")
        for product in self.Product_List:
            product.getProduct()

        print("Total Amount :",self.total_amount)
        print("Discount :",self.discount)
        print("Tax:",self.tax)
        print("Net Amount :",self.net_amount)





