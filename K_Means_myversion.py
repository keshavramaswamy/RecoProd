import pylab as pl
import random
import math

print "Clustering"
list_x=[]
list_y=[]
print "Centroids:"
print "\n"

cnet_x=[2.2,4.6,3.1]
cnet_y=[4.1,3.4,4.5]

print "X-Coordinates of the centroid are"
for iter in cnet_x:
    print iter

print "\n"

print "Y-Coordinates of the centroid are"
for iter in cnet_y:
    print iter




print "Randomising other data points:"
for iter in range(1,11):
    list_x.append(random.uniform(0,5))
    list_y.append(random.uniform(0,5))

for iter1 in list_x:
    print iter1
    
print "\n"

for iter2 in list_y:
    print iter2
    


for iter in range(0,10):
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
