import pylab as pl
import random
import math

'''
y1 = [0,1,2,3,4,5] 
y2 = [6,7,8,9,10,11,12,13,14,15]

x1 = range(len(y1))
x2 = range(len(y2))
'''
'''
list_x=[ 4.5, 3.3, 3.7, 4.1, 4.0, 3.9, 4.3, 4.6, 4.7, 4.8]
list_y=[ 4.0, 4.1, 3.8, 4.2, 4.6, 4.8, 4.9, 3.9, 3.8, 4.1]
'''

list_x=[]
list_y=[]

cnet_x=[4.2,4.6,3.9]
cnet_y=[4.1,4,4.5]



for iter in range(1,31):
    list_x.append(random.uniform(3,5))
    list_y.append(random.uniform(3,5))
    
for iter in range(0,30):
    dist1 = math.hypot(list_x[iter] - cnet_x[0] , list_y[iter] - cnet_y[0])
    dist2 = math.hypot(list_x[iter] - cnet_x[1] , list_y[iter] - cnet_y[1])
    dist3 = math.hypot(list_x[iter] - cnet_x[2] , list_y[iter] - cnet_y[2])

    
    if(min(dist1,dist2,dist3)==dist1):
        pl.plot(list_x[iter],list_y[iter],'or')
        
    if(min(dist1,dist2,dist3)==dist2):
        pl.plot(list_x[iter],list_y[iter],'oy')

    if(min(dist1,dist2,dist3)==dist3):
        pl.plot(list_x[iter],list_y[iter],'ob')

    '''
    print dist1,dist2,dist3
    print min(dist1,dist2,dist3)
    '''
        
                



pl.plot(cnet_x[0],cnet_y[0],'sr',markersize=8)
pl.plot(cnet_x[1],cnet_y[1],'sy',markersize=8)
pl.plot(cnet_x[2],cnet_y[2],'sb',markersize=8)

#pl.plot(list_x,list_y,'go')
#pl.plot(x2, y2,'bo')
pl.show()
