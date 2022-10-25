# A local pizza store wants you to develop an application where customers can order a pizza of 
# their choice. The customer will be given a choice to customize their pizza based on below menu:
class Pizza:
    base_price={"Regular":50,"Wholewheat":75}
    def __init__(self,base_type=None):
        self. amount=0
        self.base_type=base_type
    def Total_Bill_Nodis(self,total_toppings): #bill with no discount
        self.amount=Pizza.base_price[self.base_type]+total_toppings
        return self.amount
    def Total_Bill_dis(self,total_toppings,total_drink, total_desert):  #bill with discount
        self.amount=Pizza.base_price[self.base_type]+total_toppings+total_drink+ total_desert
        dis=(5*self.amount)/100
        self.amount-=dis 
        return self.amount
    
    class Toppings:  #toppings inner class
        def __init__(self,toppings_list=None):
            self.toppings={"Mozzarella":30,"Cheddar":35, "Spinach":20,"Corn":15,"Mushroom":15,"Chicken":50,
                  "Pepperoni":45}
            self.price=0
            self.toppings_list=toppings_list
        def toppings_price(self):
            for top in self.toppings_list:
                self.price+=self.toppings[top]
            return self.price
        
    class Drinks:#drinks inner class
        def __init__(self,drinks_list=None):
            self.drinks_list=drinks_list
            self.amt=0
            self.drink_dict={"Pepsi":17,"7up":19,"Coke":20}
        def drinks_price(self):
            for drink in self.drinks_list:
                self.amt+=self.drink_dict[drink]
            return self.amt
        
    class Desert:#desert inner class
        def __init__(self,des_list=None):
            self.desert_dict={"Lavacake":95,"Chocolatebrownie":86}
            self.des_list=des_list
            self.amt_des=0
        def des_price(self):
            for dess in self.des_list:
                self.amt_des+=self.desert_dict[dess]
            return self.amt_des
        
        
def PizzaBook():  #main function
    #user input
    pizza_base=input("Enter Pizza Basae:")
    sauce=input("Enter Sauce:")
    toppings_inp=list(map(str,input("Enter Toppings in pizza:").split()))
    drink=list(map(str,input("Enter drinks in pizza:").split()))
    desert=list(map(str,input("Enter Desert in pizza:").split()))
    obj1=Pizza(pizza_base)
    if(len(drink)==0 or len(desert)==0):  #if not desert and drink present the total bill with no dsicount
        top_obj=obj1.Toppings(toppings_inp)
        price1=top_obj.toppings_price()
        print("Amount:-",obj1.Total_Bill_Nodis(price1))
    else:       #if desert and drink present the total bill with dsicount
        top_obj=obj1.Toppings(toppings_inp)  #object of toppings inner class with toppings list as parameter
        price1=top_obj.toppings_price() 
        drink_obj=obj1.Drinks(drink)
        price2=drink_obj.drinks_price()
        desert_obj=obj1.Desert(desert)
        price3=desert_obj.des_price()
        print("Amount:-")
        print(obj1.Total_Bill_dis(price1,price2,price3))
PizzaBook()
    
    
    
