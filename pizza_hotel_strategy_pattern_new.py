# A local pizza store wants you to develop an application where customers can order a pizza of 
# their choice. The customer will be given a choice to customize their pizza based on below menu:
def Total_Bill_Nodis(topping_price,base_price,drink_price=None,desert_price=None):
    return base_price+topping_price
def Total_Bill_dis(topping_price,base_price,drink_price,desert_price):
    amt=base_price+topping_price+desert_price+drink_price
    dis=(5*amt)/100
    return amt-dis

class Pizza:
    base_price={"Regular":50,"Wholewheat":75}
    def __init__(self,base_type=None,discount_strategy=None):
        self.final_price=0
        self.base_type=base_type
        self.discount_strategy=discount_strategy
    def price_after_discount(self,topping_price,drink_price=None,desert_price=None):
        if(self.discount_strategy):
            self.final_price=self.discount_strategy(topping_price,Pizza.base_price[self.base_type],drink_price,desert_price)
        else:
            pass
        return self.final_price
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
    obj1=Pizza()
    sauce=input("Enter Sauce:")
    toppings_inp=list(map(str,input("Enter Toppings in pizza:").split()))
    drink=list(map(str,input("Enter drinks in pizza:").split()))
    desert=list(map(str,input("Enter Desert in pizza:").split()))
   
    if(len(drink)==0 or len(desert)==0):  #if not desert and drink present the total bill with no dsicount
        top_obj=obj1.Toppings(toppings_inp)
        price1=top_obj.toppings_price()
        obj_new=Pizza(pizza_base,discount_strategy=Total_Bill_Nodis)
        print("Amount:-",obj_new.price_after_discount(price1))
    
    else:       #if desert and drink present the total bill with dsicount
        top_obj=obj1.Toppings(toppings_inp)  #object of toppings inner class with toppings list as parameter
        price1=top_obj.toppings_price() 
        drink_obj=obj1.Drinks(drink)
        price2=drink_obj.drinks_price()
        desert_obj=obj1.Desert(desert)
        price3=desert_obj.des_price()
        obj_new=Pizza(pizza_base,discount_strategy=Total_Bill_dis)
        print("Amount:--")
        print(obj_new.price_after_discount(price1,price2,price3))
    
PizzaBook()
    
    
    
