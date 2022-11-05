from collections import defaultdict
from abc import ABC,abstractmethod
class Caluclate_Fair(ABC):
    @abstractmethod
    def Calculate_Fair_taxi(self,cust_distance):
        pass 
class Driver_Suggestion:
    def Suggest_Driver_withoutdest(self,car_dict,cab_name,cab_dest=None):
        if(cab_name not in car_dict):
            return "Select Another Car Sir!!"
        else:
           
            driver_name=''
            min_dist=10**9
            for driver in car_dict[cab_name]:
                if(float(driver[1])<4):
                    continue 
                else:
                    if(driver[2]<=min_dist and float(driver[1])>=4):
                        min_dist=driver[2]
                        driver_name=driver[0]
                    else:
                        pass
       
        if(len(driver_name)==0 ):
            return "Could not find driver"
        return driver_name
    def Suggest_Driver_dest(self,car_dict,cab_name,cab_dest=None):
        if(cab_name not in car_dict):
            return "Select Another Car Sir!!"
        else:
          
            driver_name=''
            min_dist=10**9
            for driver in car_dict[cab_name]:
                if(float(driver[1])<4):
                    continue 
                else:
                    if(driver[2]<=min_dist and cab_dest in driver[3][0]):
                        min_dist=driver[2]
                        driver_name=driver[0]
                    else:
                        pass
     
        if(len(driver_name)==0 ):
            return "Could not find driver"
        return driver_name   
class Register_Cab(Caluclate_Fair,Driver_Suggestion):
    cab_dict=defaultdict(list)
    def __init__(self,driver_name,cab_model,rating,dfc,dest=None):  
        self.driver_name=driver_name
        self.cab_model=cab_model
        self.rating=rating
        self.dest=dest 
        self.dfc=dfc 
        Register_Cab.cab_dict[self.cab_model].append([self.driver_name,self.rating,self.dfc,self.dest])
    def Calculate_Fair_taxi(self,cust_distance):
        return cust_distance*8
    def get_driver_by_name(self,cab_model,dest=None):
        if(dest is None):
            driver_name=self.Suggest_Driver_withoutdest(Register_Cab.cab_dict,cab_model)
        else:
             driver_name=self.Suggest_Driver_dest(Register_Cab.cab_dict,cab_model,dest)
        return driver_name

#main function

# taxi=Register_Cab('A', 'HatchBack', 4 ,500)
# taxi=Register_Cab('B' ,'HatchBack' ,4.3, 1000)
# taxi=Register_Cab('C','5SEATER',4.8,200)
# taxi=Register_Cab('D','Sedan',4.1,700)
# taxi=Register_Cab('E','HatchBack',4.8,430)
# fair=taxi.Calculate_Fair_taxi(20.5)
# driver_status=taxi.get_driver_by_name('HatchBack')
# print(fair)
# print(driver_status)

#test case 2;---
taxi=Register_Cab('A', '5SEATER', 4 ,500,["Gurgaon", "Noida", "Delhi"])
taxi=Register_Cab('B' ,'HatchBack' ,4.3, 1000,["Gurgaon"])
taxi=Register_Cab('C','5SEATER',4.8,200,["Noida"])
taxi=Register_Cab('D','Sedan',4.1,700,["Noida"])
taxi=Register_Cab('E','5SEATER',4.7,430,["Delhi"])
fair=taxi.Calculate_Fair_taxi(60)
driver_status=taxi.get_driver_by_name('5SEATER',"Gurgaon")
print(fair)
print(driver_status)
# print(Register_Cab.cab_dict)

# # test case 3
# taxi=Register_Cab('A', 'Sedan', 4 ,500)
# taxi=Register_Cab('B' ,'HatchBack' ,4.3, 1000)
# taxi=Register_Cab('C','5SEATER',4.8,200)
# taxi=Register_Cab('D','Sedan',4.1,700)
# taxi=Register_Cab('E','HatchBack',4.8,430)
# fair=taxi.Calculate_Fair_taxi(20.5)
# driver_status=taxi.get_driver_by_name('HatchBack')
# print(fair)
# print(driver_status)


    
            
 
        

                






