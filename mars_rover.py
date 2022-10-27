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
def Factory_method(r_x,r_y,head,Commands,pleatue):
    return Mars_Rover(r_x,r_y,head,Commands,pleatue)

class Pleatue:
    min_x=0
    min_y=0 
    def __init__(self,px,py,mx=0,my=0):
        self.px=px 
        self.py=py 
        self.min_x=mx 
        self.min_y=my
    def issafeState(self,rx,ry):
        return self.min_x<=rx<=self.px and self.min_y<=ry<=self.py 
class Mars_Rover:
    def __init__(self,rx,ry,head,dir_list,plt_obj):
        self.initial_x=rx
        self.initial_y=ry
        self.dir_list=dir_list
        self.head=head
        self.plt_obj=plt_obj
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
                    ress=self.plt_obj.issafeState(self.initial_x,self.initial_y)
                    if(ress==False):
                        return "OUT OF MARS"
                elif(self.head=='E' ):
                    self.initial_y+=0 
                    self.initial_x=self.right_move(self.initial_x)
                    ress= self.plt_obj.issafeState(self.initial_x,self.initial_y)
                    if(ress==False):
                        return "OUY OF MARS"
                elif(self.head=='N' ):
                    self.initial_x+=0 
                    self.initial_y=self.Up_move(self.initial_y)
                    # self.initial_y+=1
                    # self.initial_x+=0
                    ress=self.plt_obj.issafeState(self.initial_x,self.initial_y)
                    if(ress==False):
                        return "OUY OF MARS"
                elif(self.head=='S' ):
                    self.initial_x+=0 
                    self.initial_y=self.Down_move(self.initial_y)
                    # self.initial_y-=1
                    # self.initial_x+=0
                    ress=self.plt_obj.issafeState(self.initial_x,self.initial_y)
                    if(ress==False):
                        return "OUY OF MARS"
            else:
                return "Invalid Commands"
        return[self.initial_x,self.initial_y,self.head]
def main_func():    
    p_x,p_y=map(int,input("Enter Pleatue Coordinates:").split())
    r_x,r_y,head=map(str,input("Enter Rover Info:").split())
    r_x=int(r_x)
    r_y=int(r_y)
    head=str(head)
    Commands=input("Enter Sequence of commands:")
    pleatue=Pleatue(p_x, p_y)
    rover=Factory_method(r_x,r_y,head,Commands,pleatue)
    result=rover.Move_Commands()
    print(result)
main_func()
            
                    
             
    
