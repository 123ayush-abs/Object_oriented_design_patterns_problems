# Charoo-thoughtworks-cinema_seat
'''Problem Statement:  In a movie theatre 2 shows are running. You are given available seat of both show. There are some groups who want to book the tickets so first ask the show no. and then check whether seats are available or not if available then book their seats else ask them to enter seats again.
After each successful booking print total available seats and total booked seats.
Show 1:
Available seat:- A1, A2, A3, A4, A5, A6, A9
Show 2:
Available seat:- A1, A2, A4, A5, A6, B1, B3, B4, B5, B6, B7
Group1: - 
Enter show no:- 1
Enter seats:- A1, A4
Print:- “Successfully booked”
Available seat:- A2, A3, A5, A6, A9
Booked Seat:- A1, A4'''

#APPROACH :--- WE CAN HAVE 3 CLASES AS MOVIE,SHOW1 AND SHOW2 CLASS 
#MOVIE CLASS WILL HOLD ALL THE SEAT AVAILABLE FOR BOTH SHOW SO THAT WE CAN ACCES THEM at one place
#SHOW1 CLASS IS USED TO BOOK THE SEAT REQUESTED BY USERS AND FIND THE REMAINING SEATS IN SHOW1 OF MOVIE
#SHOW2 CLASS IS USED TO BOOK THE SEAT REQUESTED BY USERS AND FIND THE REMAINING SEATS IN SHOW2 OF MOVIE
@staticmethod isseatthere()=>> is a ulility method which is used to check the if seat are avail or not
LOgic:----
avail seat ko set m convert kra then requested seat set k unuin kra agr result set k lenght == avail_seat k equal ho to availablle hai
remove kren k=>> simple iterate krke avail_seat se hta diya req_seat ko aur usko update kr diya using list comprehension
