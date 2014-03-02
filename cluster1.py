import pylab as pl
import random
import math


list_x=[]
list_y=[]

cnet_x=[2.2,4.6,3.1]
cnet_y=[4.1,3.4,4.5]



for iter in range(1,31):
    list_x.append(random.uniform(0,5))
    list_y.append(random.uniform(0,5))
    
for iter in range(0,30):
    pl.plot(list_x[iter],list_y[iter],'og')
        
                



pl.plot(cnet_x[0],cnet_y[0],'sr',markersize=8)
pl.plot(cnet_x[1],cnet_y[1],'sy',markersize=8)
pl.plot(cnet_x[2],cnet_y[2],'sb',markersize=8)

#pl.plot(list_x,list_y,'go')
#pl.plot(x2, y2,'bo')
pl.show()
