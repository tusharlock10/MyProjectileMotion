from math import *
import time,sys
from random import *
import pygame as pg
import pygame.gfxdraw
from pygame.locals import *
import pygame.font

def inside(string,m):
    work_str=string[0:m]
    return work_str.split(',')


print ('''TJ Productions 2017

___  ____________  ___
|  \/  || ___ \  \/  |
| .  . || |_/ / .  . |
| |\/| ||  __/| |\/| |
| |  | || |   | |  | |
\_|  |_/\_|   \_|  |_/
                      
                      

PROJECTILE MOTION program
-By Tushar Jain

 # To change the settings, you can tweek the values in Settings.txt file
  # But be careful, not to ruin the settings file''')


        

############# TO BE WRITTEN IN SETTINGS FILE###################

big_list=[]
#######################################SETTINGS##########################################

def get_big_list():
    global big_list
    temp='''Only change the values, the (n) shows exactly those characters should be there before #. If any error, just delete this settings file
030,600#      Projectile 1 coordinates x1,y1 (7)
030,600#      Projectile 2 coordinates x2,y2 (7)
030,600#      Projectile 3 coordinates x3,y3 (7)
030,600#      Projectile 4 coordinates x4,y4 (7)
20.0#            MAX FramesPerSecond of the program [increase for smoothness, decrease for performance](4)
01#               SPEED, if SPEED is 02 then 1 real second = 2 second in program (2)
000,000,000,000#                          Advance time for Proj. 1,2,3,4 resp. (15)
050.00,050.00,050.00,060.00#      Velocities for Proj. 1,2,3,4 resp. (27)
30.00,45.00,60.00,22.50#              Angles for Proj. 1,2,3,4 resp. (23)
700,600#      Dimensions of the program window (7)
030,500#      Origin shiftof the axis (7)
255,255,255#        Color of Proj. 1 (11)
000,255,255#        Color of Proj. 2 (11)
255,000,000#        Color of Proj. 3 (11)
200,000,200#        Color of Proj. 4 (11)
050,050,050#        Backgound color (11)
09.81#          Artificial gravity in SI units (5)
1#                 Show path or not (1=True) & (0=False) (1)
1#                 Show FPS (1=True) & (0=False) (1)
1#                 Show the watermark TJ Productions 2017- the copyright label of the author (1=True) & (0=False) (1)


                    Copyright: TJ Productions 2017
                    Author: Tushar Jain
                    License: TJ Productions 2017
                # This is only a shareware and no one except the author of this program, has the right
                         to modify or change the contents of this program.'''
    try:
        f=open('Settings.txt')
    except:
        f=open('Settings.txt','w')
        f.write(temp)
    f.close()
    f=open('Settings.txt')
    big_list=f.readlines()
    big_list


def get_start_coord(lst):
    global x1,y1,x2,y2,x3,y3,x4,y4
    '''Big list 1-4'''
    s1,s2,s3,s4=lst
    p1,p2,p3,p4=[inside(s1,7),inside(s2,7),inside(s3,7),inside(s2,7)]
    x1,y1=int(p1[0]),int(p1[1])
    x2,y2=int(p2[0]),int(p2[1])
    x3,y3=int(p3[0]),int(p3[1])
    x4,y4=int(p4[0]),int(p4[1])
    

def get_MAX_FPS(lst):
    global MAX_FPS
    '''Big list 5'''
    temp=lst
    MAX_FPS=float(temp[:4])

def get_SPEED(lst):
    global SPEED
    '''Big list 6'''
    temp=lst
    SPEED=int(temp[:2])

def get_t_v_a(lst):
    global t1,t2,t3,t4,v1,v2,v3,v4,a1,a2,a3,a4
    '''Big list 7-9'''
    s1=lst[0]
    p1,p2,p3,p4=inside(s1,15)
    t1,t2,t3,t4=int(p1),int(p2),int(p3),int(p4)
    s1=lst[1]
    p1,p2,p3,p4=inside(s1,27)
    v1,v2,v3,v4=float(p1),float(p2),float(p3),float(p4)
    s1=lst[2]
    p1,p2,p3,p4=inside(s1,23)
    a1,a2,a3,a4=float(p1),float(p2),float(p3),float(p4)


def get_D(lst):
    global D
    '''Big list 10'''
    s=lst
    p1,p2=inside(s,7)
    D=[int(p1),int(p2)]


def get_axis(lst):
    global axisX,axisY
    '''Big list 11'''
    s=lst
    p1,p2=inside(s,7)
    axisX,axisY=int(p1),int(p2)


def  get_color(lst):
    global color1,color2,color3,color4,BGCOLOR
    '''Big list 12-16'''
    s1,s2,s3,s4,s5=lst
    p1,p2,p3,p4,p5=[inside(s1,11),inside(s2,11),inside(s3,11),inside(s4,11),inside(s5,11)]
    color1=[int(p1[0]),int(p1[1]),int(p1[2])]
    color2=[int(p2[0]),int(p2[1]),int(p2[2])]
    color3=[int(p3[0]),int(p3[1]),int(p3[2])]
    color4=[int(p4[0]),int(p4[1]),int(p4[2])]
    BGCOLOR=[int(p5[0]),int(p5[1]),int(p5[2])]


def get_gravity(lst):
    global gravity
    '''Big list 17'''
    s=lst
    p1=s[:5]
    gravity=float(p1)


def get_sp(lst):
    global single_proj
    '''Big list 18'''
    s=lst
    p=s[0]
    if not int(p):
        single_proj=True
    else:
        single_proj=False

def get_show_fps(lst):
    '''Big list 19'''
    return lst[0]

def get_show_label(lst):
    '''Big list 20'''
    return lst[0]

try:
    get_big_list()
    bl=big_list
    get_start_coord(bl[1:5])
    get_MAX_FPS(bl[5])
    get_SPEED(bl[6])
    get_t_v_a(bl[7:10])
    get_D(bl[10])
    get_axis(bl[11])
    get_color(bl[12:17])
    get_gravity(bl[17])
    get_sp(bl[18])
    show_fps=get_show_fps(bl[19])
    show_label=get_show_label(bl[20])
except:
    get_big_list()
    f=open('ERROR- README.txt','w')
    f.write('''Some error occured, the settings file is reset with default values
Make sure you change the values but take care of the format
Also do not write any character other than numbers in the settings file''')
    f.close()
    pygame.quit()
    

#############################################################
pg.init()
screen=pg.display.set_mode(D,RESIZABLE)

screen.fill(BGCOLOR)
pygame.display.set_caption('Projectile Motion')
pg.display.flip()
flag=True
clock=pg.time.Clock()
t=time.time()
#############################################################

class Projectile:
    def __init__(self,angle,v,t):
        self.a=float(radians(angle))
        self.v=float(v)
        self.t=float(t)
        self.x=0
        self.y=0

    def change_time(self):
        '''Changes time in each call'''
        self.t+=SPEED/(MAX_FPS)

    def get_x(self):
        self.x=self.v*self.t*cos(self.a)
        return self.x

    def get_y(self):
        self.y=(self.v*sin(self.a)*self.t)-(gravity*0.5*self.t*self.t)
        return self.y


def label(text,size,color,pos):
    f=pygame.font.match_font('arialround')
    try:
        Font=pygame.font.SysFont(f,size)
    except:return
    write=Font.render(text,True,color)
    screen.blit(write,pos)
def Show_FPS(c_fps):
    pygame.draw.rect(screen,BGCOLOR,[0,0,80,25])
    b=BGCOLOR
    color=[255-b[0],255-b[1],255-b[2]]
    label(c_fps,20,color,[0,0])
    
    
    
    
    

P1=Projectile(a1,v1,t1)
P2=Projectile(a2,v2,t2)
P3=Projectile(a3,v3,t3)
P4=Projectile(a4,v4,t4)


i=False
while flag:
    for e in pg.event.get():
        if e.type==QUIT:
            
            flag=False
        else:
            pass

    if single_proj:
        screen.fill(BGCOLOR)
        R=5
        d=2

    else:
        R=1
        d=0

    if not P1.y<0:pg.draw.circle(screen,color1,[int(P1.x)+axisX,int(axisY-P1.y)],R,d)
    if not P2.y<0:pg.draw.circle(screen,color2,[int(P2.x)+axisX,int(axisY-P2.y)],R,d)
    if not P3.y<0:pg.draw.circle(screen,color3,[int(P3.x)+axisX,int(axisY-P3.y)],R,d)
    if not P4.y<0:pg.draw.circle(screen,color4,[int(P4.x)+axisX,int(axisY-P4.y)],R,d)

    if (P1.y<0) and (P2.y<0) and (P3.y<0) and (P4.y<0):
        flag=False

    if show_fps:
        pass
        #c_fps=clock.get_fps()
        #Show_FPS(str(trunc(c_fps)))
    if show_label:
        #label('TJ Productions 2017',28,[120,120,120],[D[0]/2-150,D[1]/2])
        pass
        
    
    pg.draw.aaline(screen,(255,0,0),(axisX,axisY),(axisX,0))
    pg.draw.aaline(screen,(0,255,0),(axisX,axisY),(D[0],axisY))
    
    pg.display.update()


    P1.change_time()
    P2.change_time()
    P3.change_time()
    P4.change_time()
    
    P1.get_x(),P1.get_y()
    P2.get_x(),P2.get_y()
    P3.get_x(),P3.get_y()
    P4.get_x(),P4.get_y()
    
    
    clock.tick(MAX_FPS)

       
pg.quit()
