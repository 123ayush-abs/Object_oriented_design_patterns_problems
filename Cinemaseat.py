class Movie:
    show1seat=["A1","A2","A3","A4","A5","A6","A9"]
    show2seat=["A1","A2","A4","A5","A6","B1","B3","B4","B5","B6","B7"]
    @staticmethod
    def Iseatthere(booked_seat,avail_seat):
        avail_set=set(avail_seat)
        booked_seat=set(booked_seat)
        res_set=avail_set.union(booked_seat)
        if(len(res_set)==len(avail_seat)):
            return 1
        else:
            return 0
    
    
class Show1:
    def __init__(self,bookedseat):
        self.bookedseat=bookedseat
    def Reamin_Seat(self):
        Movie.show1seat=[seat for seat in Movie.show1seat if seat not in self.bookedseat]
        # for seat in self.bookedseat:
        #    Movie.show1seat.remove(seat)
        
    
class Show2:
    def __init__(self,bookedseat):
        self.bookedseat=bookedseat
    def Reamin_Seat(self):
        Movie.show2seat=[seat for seat in Movie.show2seat if seat not in self.bookedseat]
        # for seat in self.bookedseat:
        #     Movie.show2seat.remove(seat)

# def Iseatthere(booked_seat,avail_seat):
#     avail_set=set(avail_seat)
#     booked_seat=set(booked_seat)
#     res_set=avail_set.union(booked_seat)
#     if(len(res_set)==len(avail_seat)):
#         return 1
#     else:
#         return 0
print("Menue:--")
print("Press 0 to quit")
while(1):
    show_num=int(input("Enter Show Number"))
    seat_req=list(map(str,input("Enter Seats Required:").split()))
    if(show_num==1 and Movie.Iseatthere(seat_req, Movie.show1seat)==1):
        print("Booked!!")
        obj1=Show1(seat_req)
        obj1.Reamin_Seat()
        print(Movie.show1seat)
        
    elif(show_num==2 and Movie.Iseatthere(seat_req, Movie.show2seat)==1):
        print("Booked for SHow2::")
        obj2=Show2(seat_req)
        obj2.Reamin_Seat()
        print(Movie.show2seat)
    elif(show_num==0):
        break
    
    
    
    
# class B(Movie):
#     def update(self):
#         Movie.show1seat.append("A100")
# b=B()
# b.update()
# print(Movie.show1seat)        
        
                      
           

          
                      
                      
           

                                 
                      
