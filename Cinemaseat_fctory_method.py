#here we implemented the problem using the  factory method pattern
#that is we are deciding the type of the object at run time
#we have a factory methid that will build the object at run time
#dependig in the user's choice like if show_num is 1 then 
#it will build the object of the Show1 class and else for show 2

#we make movie class as the abstarct class which as having the abstarct method that check
#if the seats are avail or not but it is not implemented as it is abstract 
#then it will be overriddedn by child class
from abc import ABC, abstractmethod   #abstarct class import
#factory design pattern
class Movie(ABC):  #abstarct class having absract method
    @abstractmethod 
    def Iseatthere(self):  #have commin methid that can be modified by any child class acc to need
        pass
def factory(num,seat_req):  #factory function
    if(num==1):
        return Show1(seat_req)  #build object at run time with seat_req as parameter
    else:
        return Show2(seat_req)  #creting show2 class object
    
#show1 class inheriting movie class and overriding isseatthere function 
class Show1(Movie):
    show1seat=["A1","A2","A3","A4","A5","A6","A9"]
    def __init__(self,bookedseat=None):
        self.bookedseat=bookedseat 
    def Iseatthere(self):
        avail_set=set(Show1.show1seat)
        temp=set(self.bookedseat)
        res=avail_set.union(temp)
        if(len(res)==len(Show1.show1seat)):
            return 1
        else:
            return 0   
    def Reamin_Seat(self):
        Show1.show1seat=[seat for seat in Show1.show1seat if seat not in self.bookedseat]
        return Show1.show1seat
        
##show2 class inheriting movie class and overriding isseatthere function    
class Show2(Movie):
    show2seat=["A1","A2","A3","B1","B5","A6","A9"]
    def __init__(self,bookedseat):
        self.bookedseat=bookedseat
        
    def Iseatthere(self):
        avail_set=set(Show2.show2seat)
        temp=set(self.bookedseat)
        res=avail_set.union(temp)
        if(len(res)==len(Show2.show2seat)):
            return 1
        else:
            return 0
    def Reamin_Seat(self):
        Show2.show2seat=[seat for seat in Show2.show2seat if seat not in self.bookedseat]
        return Show2.show2seat
#main function and handling various cases
def main_fun():   
    print("Menue:--")  
    print("1:-Show1")
    print("2:- Show2")
    print("Press 0 to quit")
    while(1):
        show_num=int(input("Enter Show Number"))  #user input
        if(show_num not in [1,2]):
            print("Incorect show number")
            continue
        seat_req=list(map(str,input("Enter Seats Required:").split()))
        if(show_num==1 and Show1(seat_req).Iseatthere()==1): #check if requested seat are avail
            ress=factory(show_num,seat_req)  #creting type of the object at run time
            print("Booked")
            temp=ress.Reamin_Seat()
            print(temp)
        elif(show_num==2 and Show2(seat_req).Iseatthere()==1):
            print("Booked for SHow2::")
            ress=factory(show_num,seat_req)
            print("Booked")
            temp=ress.Reamin_Seat()
            print(temp)
        elif(show_num==0):
            break          
main_fun()