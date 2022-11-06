from collections import defaultdict
#stratedy method
def Suggest_Driver_withoutdest(car_dict,cab_name):
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
def Suggest_Driver_dest(car_dict,cab_name,cab_dest):
        if(cab_name not in car_dict):
            return "Select Another Car Sir!!"
        else:
          
            driver_name=''
            min_dist=10**9
            for driver in car_dict[cab_name]:
                if(float(driver[1])<4):
                    continue 
                else:
                    if(driver[2]<=min_dist and cab_dest in driver[3]):
                        min_dist=driver[2]
                        driver_name=driver[0]
                        
                    else:
                        pass
        if(len(driver_name)==0 ):
            return "Could not find driver"
        return driver_name 


# class Caluclate_Fair(ABC):
#     @abstractmethod
#     def Calculate_Fair_taxi(self,cust_distance):
#         pass 
class Driver_Suggestion:
    def __init__(self,car_dict,strategy=None):
        self.car_dict=car_dict
        self.strategy=strategy
      
    def Get_Driver_Status(self,cab_name,dest=None):
     
        if(self.dest is None):
            self.strategy=Suggest_Driver_withoutdest
            driver_name=self.strategy(self.car_dict,cab_name)
        else:
            self.strategy=Suggest_Driver_dest
            driver_name=self.strategy(self.car_dict,cab_name,dest)
        return driver_name
            
        
    
class Register_Cab(Driver_Suggestion):
    cab_dict=defaultdict(list)
    def __init__(self,driver_name=None,cab_model=None,rating=None,dfc=None,dest=None):  
        self.driver_name=driver_name
        self.cab_model=cab_model
        self.rating=rating
        if(dest is not None):
            self.dest=dict.fromkeys(dest,0)
        else:
            self.dest=dest
        self.dfc=dfc 
        Register_Cab.cab_dict[self.cab_model].append([self.driver_name,self.rating,self.dfc,self.dest])
        Driver_Suggestion.__init__(self,  Register_Cab.cab_dict)
       
    @staticmethod  #utility method
    def Calculate_Fair_taxi(cust_distance):
        return cust_distance*8
    
    
# #input
# def Amin_input():    
#     taxi_num=int(input("Enter The total taxi:"))
#     for i in range(taxi_num):
#         driver_name=input("Enter driver name:")
#         cab_model=input("Enter cab model:")
#         rating=float(input("Enter druver rating:"))
#         dfc=input("Enter distance from customer:")
#         dfc=dfc.split()
#         if(dfc[1]=='Km'):
#             dfc=int(dfc[0])*1000
#         else:
#             dfc=int(dfc[0])
#         dest=list(map(str,input("Enter destination details if any").split()))
#         taxi=Register_Cab(driver_name,cab_model,rating,dfc,dest)
# def User_input():
#     dist=input("Enter total distance:")
#     cab=input("ENter car name:")
#     des=list(map(str,input("Enter destination details if any").split()))
#     taxi=Register_Cab()
#     print(taxi.Get_Driver_Status(cab,des))
#     print(taxi.Calculate_Fair_taxi(dist))
# Amin_input()
# User_input()
        
    
#main function

# taxi=Register_Cab('A', 'HatchBack', 4 ,500)
# taxi=Register_Cab('B' ,'HatchBack' ,4.3, 1000)
# taxi=Register_Cab('C','5SEATER',4.8,200)
# taxi=Register_Cab('D','Sedan',4.1,700)
# taxi=Register_Cab('E','HatchBack',4.8,430)
# fair=Register_Cab.Calculate_Fair_taxi(20.5)
# driver_status=taxi.Get_Driver_Status('HatchBack')
# print(fair)
# print(driver_status)

# # # #test case 2;---
# taxi=Register_Cab('A', '5SEATER', 4 ,500,["Gurgaon", "Noida", "Delhi"])
# taxi=Register_Cab('B' ,'HatchBack' ,4.3, 1000,["Gurgaon"])
# taxi=Register_Cab('C','5SEATER',4.8,200,["Noida"])
# taxi=Register_Cab('D','Sedan',4.1,700,["Noida"])
# taxi=Register_Cab('E','5SEATER',4.7,430,["Delhi"])
# fair=taxi.Calculate_Fair_taxi(60)
# driver_status=taxi.Get_Driver_Status("5SEATER","Delhi")
# print(fair)
# print(driver_status)
# # print(Register_Cab.cab_dict)

# # test case 3
taxi=Register_Cab('A', 'Sedan', 4 ,500)
taxi=Register_Cab('B' ,'HatchBack' ,4.3, 1000)
taxi=Register_Cab('C','5SEATER',4.8,200)
taxi=Register_Cab('D','Sedan',4.1,700)
taxi=Register_Cab('E','HatchBack',4.8,430)
fair=taxi.Calculate_Fair_taxi(20.5)
driver_status=taxi.Get_Driver_Status('HatchBack')
print(fair)
print(driver_status)


    
            
 
        

                






