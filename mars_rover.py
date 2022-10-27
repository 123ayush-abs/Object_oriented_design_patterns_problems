right_rotate_dict={
    'N':'E',
    'E':'S',
    'W':'N',
    'S':'W'
    
}
left_rotate_dic={
    'N':'W',
    'W':'S',
    'S':'E',
    'E':'N'
}
def Factory_method(r_x,r_y,head,Commands,p_x,p_y):
    return Mars_Rover(r_x,r_y,head,Commands,p_x,p_y)

class Pleatue:
    @staticmethod
    def issafeState(px,py,rx,ry):
        if(rx<=px and ry<=py):
            return 1
        else:
            return 0
class Mars_Rover(Pleatue):
    def __init__(self,rx,ry,head,dir_list,px,py):
        self.initial_x=rx
        self.initial_y=ry
        self.dir_list=dir_list
        self.head=head
        self.px=px 
        self.py=py
    def left_move(self,x):
        x=x-1
        return x
    def right_move(self,x):
        x=x+1
        return x 
    def Up_move(self,y):
        y+=1
        return y 
    def Down_move(self,y):
        y-=1
        return y
    def Move_Commands(self):
        for direction in self.dir_list: 
            if(direction=='L'):
                self.initial_x+=0 
                self.initial_y+=0 
                self.head=left_rotate_dic[self.head]
                # print(self.head)
            elif(direction=='R'):
                self.initial_x+=0
                self.initial_y+=0 
                self.head=right_rotate_dict[self.head]
                # print(self.head)
            elif(direction=='M'):
                # print(self.head)
                if(self.head=='W' ):
                    self.initial_y+=0
                    self.initial_x=self.left_move(self.initial_x)
                    # self.initial_x-=1
                    # self.initial_y+=0
                    ress=Pleatue.issafeState(self.px,self.py,self.initial_x,self.initial_y)
                    if(ress==0):
                        return "OUY OF MARS"
                elif(self.head=='E' ):
                    self.initial_y+=0 
                    self.initial_x=self.right_move(self.initial_x)
                    ress=Pleatue.issafeState(self.px,self.py,self.initial_x,self.initial_y)
                    if(ress==0):
                        return "OUY OF MARS"
                elif(self.head=='N' ):
                    self.initial_x+=0 
                    self.initial_y=self.Up_move(self.initial_y)
                    # self.initial_y+=1
                    # self.initial_x+=0
                    ress=Pleatue.issafeState(self.px,self.py,self.initial_x,self.initial_y)
                    if(ress==0):
                        return "OUY OF MARS"
                elif(self.head=='S' ):
                    self.initial_x+=0 
                    self.initial_y=self.Down_move(self.initial_y)
                    # self.initial_y-=1
                    # self.initial_x+=0
                    ress=Pleatue.issafeState(self.px,self.py,self.initial_x,self.initial_y)
                    if(ress==0):
                        return "OUY OF MARS"
            else:
                return "Invalid Commands"
        return[self.initial_x,self.initial_y,self.head]
def main_func():    
    p_x,p_y=map(int,input("Enter Pleatue Coordinates:").split())
    print("1:-Enter Total Rovers:")
    rover_num=int(input())
    for rov_num in range(rover_num):
        r_x,r_y,head=map(str,input("Enter Rover Info:").split())
        r_x=int(r_x)
        r_y=int(r_y)
        head=str(head)
        Commands=input("Enter Sequence of commands:")
        rover=Factory_method(r_x,r_y,head,Commands,p_x,p_y)
        result=rover.Move_Commands()
        print(result)
main_func()
            
                    
             
    
