import csv
import numpy as np
import pylab as pl
from matplotlib import rcParams
from numpy import array

def givemax(numlist):
    max = numlist[0]
    index = 0
    for iter in range(1,len(numlist)):
        if numlist[iter] > max:
            max = numlist[iter]
            index = iter
    return index

def npng(flag,fname):

    list1 =[]
    cp =0
    cn =0
        
    
    if flag == 1:
        with open("1_"+fname+'.csv', 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                list1.append(row)

        list1.pop(0)
        cp =0
        cn =0
        
        for iter in list1:
            label =  iter[len(iter) - 1]
            if label =='positive':
                cp = cp + 1
            if label =='negative':
                cn = cn + 1

        return cp,cn
            
    if flag == 2:
        with open("2_"+fname+'.csv', 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                list1.append(row)

        list1.pop(0)
        cp =0
        cn =0
        for iter in list1:
            label =  iter[len(iter) - 1]
            if label =='positive':
                cp = cp + 1
            if label =='negative':
                cn = cn + 1

        return cp,cn
        

        
    if flag == 3:
        with open("3_"+fname+'.csv', 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                list1.append(row)

        list1.pop(0)
        cp =0
        cn =0
        for iter in list1:
            label =  iter[len(iter) - 1]
            if label =='positive':
                cp = cp + 1
            if label =='negative':
                cn = cn + 1

        return cp,cn
        

def drawgraph(list1,list2,flag):
    n = 4
    
    if flag == 1:
        fname = 'op1.png'
    if flag == 2:
        fname = 'op2.png'
    if flag == 3:
        fname = 'op3.png'
        
    X = np.arange(n)
    aY1 = array(list1)
    aY2 = array(list2)

    #print list1
    #print list2
    
    limit1 = givemax(list1)
    limit2 = givemax(list2)

    l1 = list1[limit1]
    l2 = list2[limit2]

    if l1 > l2:
        maxl = l1
    else:
        maxl = l2
        
    nmaxl = -1*maxl

    #print nmaxl
    #print maxl
    
    rcParams.update({'figure.autolayout': True})
    width = 0.35
    ap1 = pl.bar(X, +aY1, facecolor='#9999ff', edgecolor='white')
    ap2 = pl.bar(X, -aY2, facecolor='#ff9999', edgecolor='white')
    pl.ylabel('Number')
    pl.title('Aspect based Opinion Summary')

    pl.xticks(X+width/2.+.25, ('Camera','Battery','Screen','Performance') )
    pl.yticks(np.arange(nmaxl,maxl,2))
    pl.legend( (ap1[0], ap2[0]), ('Positive', 'Negative') )
    #pl.legend( ("A", "B"), ('Positive', 'Negative') )
    pl.savefig(fname)
    pl.close()

            

for i in range(1,4):

    plist =[]
    nlist =[]

    a=npng(i,"camera")
    plist.append(a[0])
    nlist.append(a[1])
    
    a=npng(i,"battery")
    plist.append(a[0])
    nlist.append(a[1])

    a=npng(i,"screen")
    plist.append(a[0])
    nlist.append(a[1])

    a=npng(i,"performance")
    plist.append(a[0])
    nlist.append(a[1])

    drawgraph(plist,nlist,i)

#print npng(1,"camera")
