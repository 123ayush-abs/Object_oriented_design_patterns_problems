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
class Pleatue:
    def __init__(self,px=0,py=0):
        self.px=px
        self.py=py 
    def issafeState(self,rx,ry):
        if(rx<=self.px and ry<=self.py):
            return "Flase"
        else:
            return "True"
class Mars_Rover(Pleatue):
    def __init__(self,rx,ry,head,dir_list):
        self.initial_x=rx
        self.initial_y=ry
        self.dir_list=dir_list
        self.head=head
        Pleatue.__init__(self)
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
                    self.initial_x-=1
                    self.initial_y+=0
                    res=self.issafeState(self.initial_x,self.initial_y)
                    if(res=='False'):
                        pass 
                    else:
                        return "OUT OF MARS"
                elif(self.head=='E' ):
                    self.initial_x+=1
                    self.initial_y+=0
                    res=self.issafeState(self.initial_x,self.initial_y)
                    if(res=='False'):
                        pass 
                    else:
                        return "OUT OF MARS"
                elif(self.head=='N' ):
                    self.initial_y+=1
                    self.initial_x+=0
                    res=self.issafeState(self.initial_x,self.initial_y)
                    if(res=='False'):
                        pass 
                    else:
                        return "OUT OF MARS"
                elif(self.head=='S' ):
                    self.initial_y-=1
                    self.initial_x+=0
                    res=self.issafeState(self.initial_x,self.initial_y)
                    if(res=='False'):
                        pass 
                    else:
                        return "OUT OF MARS" 
            else:
                return "Invalid Commands"
        return[self.initial_x,self.initial_y,self.head]
def main_func():    
    p_x,p_y=map(int,input("Enter Pleatue Coordinates:").split())
    pleatue=Pleatue(p_x,p_y)
    print("1:-Enter Total Rovers:")
    rover_num=int(input())
    for rov_num in range(rover_num):
        r_x,r_y,head=map(str,input("Enter Rover Info:").split())
        r_x=int(r_x)
        r_y=int(r_y)
        head=str(head)
        Commands=input("Enter Sequence of commands:")
        rover=Mars_Rover(r_x,r_y,head,Commands)
        result=rover.Move_Commands()
        print(result)
main_func()
            
                    
             
    