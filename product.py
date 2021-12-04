from sunshine_db import insertproduct
class Product:
    id=0
    name=""
    qty=0
    rate=0
    price=0

    def setProduct(self,billno):
        self.id=int(input("Enter Product Id :"))
        self.name=input("Enter Product Name :")
        self.qty=int(input("Enter Product Qty :"))
        self.rate=float(input("Enter Product Rate :"))
        self.price=self.qty*self.rate
        insertproduct(billno,self.id,self.name,self.qty,self.rate,self.price)

    def getProduct(self):
        print(self.id,"\t",self.name,"\t",self.qty,"\t",self.rate,"\t",self.price)
