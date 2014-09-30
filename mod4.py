import csv
import matplotlib.pyplot as pl
import math
frec=open("reco1.txt","w")
'''
def rev(x,flag):
    f=open("reco.txt","w")
    frec = open("reco1.txt","w")
    
    if flag == 1:
        if  x == "A":
            f.write("Nokia Lumia 520")
        elif x=="B":
            f.write("Sony Xperia M")
        elif x=="C":
            f.write("Apple iPhone 4")
        elif x=="D":
            f.write("Nokia Lumia 525")
        elif x=="E":
            f.write("Micromax Canvas 2 Plus A110Q")
        elif x=="F":
            f.write("Micromax Canvas 4")
        elif x=="G":
            f.write("Samsung Galaxy S Duos 2 GT-S7582")
        elif x=="H":
            f.write("Samsung Galaxy Core GT-I8262")
        elif x=="I":
            f.write("Xolo Q1000s")
        elif x=="J":
            f.write("Sony Xperia C (White)")

        f.close()

    if flag ==2:
        if  x == "A":
            frec.write("Nokia Lumia 520")
        elif x=="B":
            frec.write("Sony Xperia M")
        elif x=="C":
            frec.write("Apple iPhone 4")
        elif x=="D":
            frec.write("Nokia Lumia 525")
        elif x=="E":
            frec.write("Micromax Canvas 2 Plus A110Q")
        elif x=="F":
            frec.write("Micromax Canvas 4")
        elif x=="G":
            frec.write("Samsung Galaxy S Duos 2 GT-S7582")
        elif x=="H":
            frec.write("Samsung Galaxy Core GT-I8262")
        elif x=="I":
            frec.write("Xolo Q1000s")
        elif x=="J":
            frec.write("Sony Xperia C (White)")

        frec.close()

'''

def rev(x):
    f=open("reco.txt","w")    
    if  x == "A":
        f.write("Nokia Lumia 520")
    elif x=="B":
        f.write("Sony Xperia M")
    elif x=="C":
        f.write("Apple iPhone 4")
    elif x=="D":
        f.write("Nokia Lumia 525")
    elif x=="E":
        f.write("Micromax Canvas 2 Plus A110Q")
    elif x=="F":
        f.write("Micromax Canvas 4")
    elif x=="G":
        f.write("Samsung Galaxy S Duos 2 GT-S7582")
    elif x=="H":
        f.write("Samsung Galaxy Core GT-I8262")
    elif x=="I":
        f.write("Xolo Q1000s")
    elif x=="J":
        f.write("Sony Xperia C (White)")

    f.close()

def rev1(x):
    global frec
        
    if  x == "A":
        frec.write("Nokia Lumia 520")
        frec.write("\n")
    elif x=="B":
        frec.write("Sony Xperia M")
        frec.write("\n")
    elif x=="C":
        frec.write("Apple iPhone 4")
        frec.write("\n")
    elif x=="D":
        frec.write("Nokia Lumia 525")
        frec.write("\n")
    elif x=="E":
        frec.write("Micromax Canvas 2 Plus A110Q")
        frec.write("\n")
    elif x=="F":
        frec.write("Micromax Canvas 4")
        frec.write("\n")
    elif x=="G":
        frec.write("Samsung Galaxy S Duos 2 GT-S7582")
        frec.write("\n")
    elif x=="H":
        frec.write("Samsung Galaxy Core GT-I8262")
        frec.write("\n")
    elif x=="I":
        frec.write("Xolo Q1000s")
        frec.write("\n")
    elif x=="J":
        frec.write("Sony Xperia C (White)")
        frec.write("\n")

    
def splitpara1(file):
              import re
              sentenceEnders = re.compile("\n")
              sentenceList = sentenceEnders.split(file)
              return sentenceList
            
def givemax(numlist):
    max = numlist[0]
    index = 0
    for iter in range(1,len(numlist)):
        if numlist[iter] > max:
            max = numlist[iter]
            index = iter
    return index

fw=open("letters.txt","r")
cmp_list=[]#cmp_list stores a list of the three products selected
str=fw.read()
for i in range(0,3):
    cmp_list.append(str[i])



fwr=open("rating.txt","r")
str1 = fwr.read()
ratelist = splitpara1(str1)
ratelist.pop(len(ratelist) - 1)#stores the sentiment scores for the three selected products

rev(cmp_list[givemax(ratelist)])#calls function to select the most optimal product

#print cmp_list[givemax(ratelist)]

ind = givemax(ratelist)

cnet_x=[]#stores the x coodinates for the centroids
cnet_y=[]#stores the y coodinates for the centroids

with open('scores.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        for prod in cmp_list:
            if row[0] == prod:
                cnet_x.append(float(row[1]))
                cnet_y.append(float(row[2]))


list_x=[]#stores the x coodinates for the other points
list_y=[]#stores the x coodinates for the other points



with open('scores.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:

        flag =0
        
        for prod in cmp_list:
            if row[0] == prod:
                flag = 1
                
        if flag ==0:
            list_x.append(float(row[1]))
            list_y.append(float(row[2]))


for iter in range(0,7):
    dist1 = math.hypot(list_x[iter] - cnet_x[0] , list_y[iter] - cnet_y[0])
    dist2 = math.hypot(list_x[iter] - cnet_x[1] , list_y[iter] - cnet_y[1])
    dist3 = math.hypot(list_x[iter] - cnet_x[2] , list_y[iter] - cnet_y[2])
    #print dist1,dist2,dist3

    
    if(min(dist1,dist2,dist3)==dist1):
        pl.plot(list_x[iter],list_y[iter],'or')
        
        
    if(min(dist1,dist2,dist3)==dist2):
        pl.plot(list_x[iter],list_y[iter],'oy')

    if(min(dist1,dist2,dist3)==dist3):
        pl.plot(list_x[iter],list_y[iter],'ob')

def recoprod(index):
    global list_x,list_y,cnet_x,cnet_y

    if index==0:
        for iter in range(0,7):
            dist1 = math.hypot(list_x[iter] - cnet_x[0] , list_y[iter] - cnet_y[0])
            dist2 = math.hypot(list_x[iter] - cnet_x[1] , list_y[iter] - cnet_y[1])
            dist3 = math.hypot(list_x[iter] - cnet_x[2] , list_y[iter] - cnet_y[2])

            if(min(dist1,dist2,dist3)==dist1):
                score = list_x[iter]
                with open('scores.csv', 'rb') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if float(row[1]) == score:
                            #rev(row[0],2)
                            rev1(row[0])
                        
    if index==1:
        for iter in range(0,7):
            dist1 = math.hypot(list_x[iter] - cnet_x[0] , list_y[iter] - cnet_y[0])
            dist2 = math.hypot(list_x[iter] - cnet_x[1] , list_y[iter] - cnet_y[1])
            dist3 = math.hypot(list_x[iter] - cnet_x[2] , list_y[iter] - cnet_y[2])

            if(min(dist1,dist2,dist3)==dist2):
                score = list_x[iter]
                print score
                with open('scores.csv', 'rb') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if float(row[1]) == score:
                            rev1(row[0])

    if index==2:
        for iter in range(0,7):
            dist1 = math.hypot(list_x[iter] - cnet_x[0] , list_y[iter] - cnet_y[0])
            dist2 = math.hypot(list_x[iter] - cnet_x[1] , list_y[iter] - cnet_y[1])
            dist3 = math.hypot(list_x[iter] - cnet_x[2] , list_y[iter] - cnet_y[2])

            if(min(dist1,dist2,dist3)==dist3):
                score = list_x[iter]
                with open('scores.csv', 'rb') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if float(row[1]) == score:
                            rev1(row[0])
    
    


pl.plot(cnet_x[0],cnet_y[0],'sr',markersize=8)
pl.plot(cnet_x[1],cnet_y[1],'sy',markersize=8)
pl.plot(cnet_x[2],cnet_y[2],'sb',markersize=8)
pl.ylabel('Price(in Rupees)')
pl.xlabel('Sentiment Score')
recoprod(ind)
frec.close()

pl.text(cnet_x[0],cnet_y[0],cmp_list[0])
pl.text(cnet_x[1],cnet_y[1],cmp_list[1])
pl.text(cnet_x[2],cnet_y[2],cmp_list[2])

otlist =[]

for iter in range(0,7):
    score = list_x[iter]
    #pl.text(list_x[iter],list_y[iter],cmp_list[0])
    with open('scores.csv', 'rb') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if float(row[1]) == score:
                            otlist.append(row[0])

        
                        


for iter in range(0,7):
    pl.text(list_x[iter],list_y[iter],otlist[iter])
    




                        
#ax.annotate("A", xy=(X,Y), xytext=(-5,5), ha='right', textcoords='offset points',color=c)
#pl.plot(x2, y2,'bo')
#pl.show()
pl.savefig("kmeans.png")
