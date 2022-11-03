# As a smart OTT company, we want to offer customized OTT plans for our customers
# so that the customers should be able to choose to build their plan by choosing different
# streaming platforms and how many viewing hours they want for each of them.
# We do support the following streaming services and below is their tariff plan.

# Streaming Service | Price per unit    | Unit in hours
# Netflix           | Rs. 10            | 10 hrs
# Amazon Prime      |   Rs. 2           | 5 hrs
# Hotstar           | Rs. 1             | 5 hrs

# Viewing hours can be subscribed based on the multiples of the above mentioned units only.
# Based on the user’s choice, the system should show the total amount which should be paid by
# the customer.

# Sample Input 1
# Viewing hours for Netflix: 20
# Viewing hours for Amazon Prime: 10
# Viewing hours for Hotstar: 50
# Sample Output
# Total amount should be paid: Rs.34 (10 * 2 + 2 * 2 + 1 * 10)

# Sample Input 2
# Viewing hours for Netflix: 10
# Viewing hours for Amazon Prime: 0
# Viewing hours for Hotstar: 100
# Sample Output
# Total amount should be paid: Rs.30 (10 * 1 + 2 * 0 + 1 * 20)

# Sample Input 3
# Viewing hours for Netflix: 10
# Viewing hours for Amazon Prime: 2
# Sample Output
# Amazon Prime allows viewing hours in multiples of 5 only[3] [4]



Netflix={
    "Units":10,
    "Price_unit":10
}
Amazon_prime={
    "Units":5,
    "Price_unit":2
}
Hotstar={
    "Units":5,
    "Price_unit":1
}
class Check_hours_validity:
    def check_allowed_multiples(self,view_hours=None,ott_plat=None):
        if(ott_plat=="netflix" and view_hours%Netflix['Units']!=0):
            sres=ott_plat+" requres hours multiples of "+str(Netflix['Units'])
            return sres
        elif(ott_plat=="amazon" and view_hours%Amazon_prime['Units']!=0):
            sres=ott_plat+" requres hours multiples of "+str(Amazon_prime['Units'])
            return sres
        elif(ott_plat=="hotstar" and view_hours%Hotstar['Units']!=0):
            sres=ott_plat+" requres hours multiples of "+str(Hotstar['Units'])
            return sres
        else:
            return "true"
        
class Caluclate_plan(Check_hours_validity):
    def __init__(self,input_dict):
        self.input_dict=input_dict
        self.amount=0
    def Generate_plan_amount(self):
        for i in self.input_dict:
            if(i=='netflix'):
                sres=self.check_allowed_multiples(self.input_dict[i],"netflix")
                if(sres=="true"):
                    self.amount+=(self.input_dict[i]//Netflix['Units'])*Netflix['Price_unit']
                else:
                    return sres
            elif(i=='amazon'):
                sres=self.check_allowed_multiples(self.input_dict[i],"amazon")
                if(sres=="true"):
                    self.amount+=(self.input_dict[i]//Amazon_prime['Units'])*Amazon_prime['Price_unit']
                else:
                    return sres
            elif(i=='hotstar'):
                sres= self.check_allowed_multiples(self.input_dict[i],"hotstar")
                if(sres=='true'):
                    self.amount+=(self.input_dict[i]//Hotstar['Units'])*Hotstar['Price_unit']
                else:
                    return sres
        return "Total Amount to be paid: Rs."+" "+str(self.amount)
    
def main_func():
    print("Available OTT")
    print("1-Netflix")
    print("2:-Amazon")
    print("3:- Hotstar")
    total_plat=int(input("Enter for how mant you want to activate your plan:"))
    d={}
    for i in range(total_plat):
        ott_plat,view=input("Enter Ott platform and viewing hours:").split()
        d[ott_plat]=int(view)
    obj=Caluclate_plan(d)
    print(obj.Generate_plan_amount())
main_func()
        
            