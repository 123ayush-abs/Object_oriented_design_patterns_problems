# There is a company which have started selling the ipods ONLINE . But they want to sell these ipods online at best price.
# i) They have ipod Inventories at Brazil and Argentina. Each of the inventory can store only 100 ipods.
# ii) ipods at Brazil are sold at 100$/unit and at Argentina they are sold at 50$/unit.
# iii) after every order the stock at both brazil and argentina inventories are again back to 100 units.
# iv) the no of transport ipods ordered should be only in multiple of 10.(i.e no of ipods ordered shouldnt be im number like 123 etc. 
# v) the order placed should be either fullfilled completely or nothin
# vi) if the order is placed like 120 ipods from brazil then the remaining ipods can be brought from the other inventory i.e.argentina. but here shipping price of 400$ per 10 units is applied.
# We have to select best price solution.
# Input - [Country] : [iPod required]
# Output - [Best Price] : [Remaining iPod in Brazil] : [Remaining iPod in Argentina]
# i) Brazil : 5
# 500 : 95 : 100
# ii) Brazil : 50
# 4500 : 100 : 50
# iii) Argentina : 120
# 7800 : 80 : 0
# iv) Argentina : 250
# Out of stock!!!!

class Ipod:
    def __init__(self,country,ipod_req):
        self.country=country
        self.ipod_req=ipod_req
        self.brazil_ipods=100
        self.argentina_ipods=100
        self.brazil_left=0
        self.argentina_left=0
        self.brazil_cost=100
        self.argentina_cost=50
        self.total_ipods=200
        self.transport_charge=40
        self.amount=0
    def Best_price_ipod(self):
        if(self.ipod_req>self.total_ipods):
            return "Out of Stock!!"
        
        elif(self.ipod_req%10==0 and self.ipod_req<=100):
            if(self.country=="Brazil"):
                self.amount=(self.argentina_cost+self.transport_charge)*self.ipod_req
                self.brazil_left+=self.brazil_ipods
                self.argentina_left+=self.argentina_ipods-self.ipod_req
            else:
                self.amount=(self.argentina_cost)*self.ipod_req
                self.brazil_left+=self.brazil_ipods
                self.argentina_left+=self.argentina_ipods-self.ipod_req
            return [self.amount,self.brazil_left,self.argentina_left]
        
        elif(self.ipod_req%10==0 and self.ipod_req>100):
            if(self.country=="Argentina"):
                self.amount+=(self.argentina_cost*100)+(self.ipod_req-100)*self.brazil_cost+(self.ipod_req-100)*self.transport_charge
                self.brazil_left+=self.brazil_ipods-(self.ipod_req-100)
                self.argentina_left+=0
            else:
                self.amount+=((self.argentina_cost+self.transport_charge)*100)+(self.ipod_req-100)*self.brazil_cost
                self.brazil_left+=self.brazil_ipods-(self.ipod_req-100)
                self.argentina_left+=0
            return [self.amount,self.brazil_left,self.argentina_left]
        
        elif(self.ipod_req%10!=0 and self.ipod_req<=100):
            if(self.country=="Brazil"):
                self.amount+=(self.ipod_req*self.brazil_cost)
                self.brazil_left=100-self.ipod_req
                self.argentina_left=100
            else:
                self.amount+=(self.ipod_req*self.argentina_cost)
                self.brazil_left=100
                self.argentina_left=100-self.ipod_req
            return [self.amount,self.brazil_left,self.argentina_left]
            
        else:
            return "OUT Of STOCK"


def main_input():
    Country=input("Enter Country:")
    Ipod_req=int(input("Enter ipods needed:"))
    ipod=Ipod(Country,Ipod_req)
    print(ipod.Best_price_ipod())                
main_input()
            