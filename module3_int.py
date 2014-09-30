per = '.'

def clas(inp,word):
    global i
    fr1 = open(str(i)+"_allrev.txt","r")
    fw1 = open(inp,"w")

    if word =="camera":
        word2 ="Camera"

    if word =="screen":
        word2 ="Screen"

    if word =="battery":
        word2 ="Battery"

    if word =="performance":
        word2 ="Performance"

    if word =="phone":
        word2 ="Phone"

    for line in fr1:
         if word in line:
             fw1.write(line)

    fw2 = open(inp,"a")
    fr2 = open(str(i)+"_allrev.txt","r")
    
    for line in fr2:
         if word2 in line:
             fw2.write(line)

             
    fw1.close()
    fw2.close()
    fr1.close()
    fr2.close()

def splitpara1(file):
              import re
              sentenceEnders = re.compile("."+"\n")
              sentenceList = sentenceEnders.split(file)
              return sentenceList

def splitfile(flag,aspect):
    #fwrite = "C:\\Python27\\Project FIles 3.3\\module 3\\"
    fwrite = "D:\\Academics\\Project\\Files\\"

    if flag == 1:
        
        if aspect =="camera":
            fname1    = "1_camera\\split"
            f1 = open("1_camera.txt","r")
            list1 = splitpara1(f1.read())
            list1.pop(len(list1) - 1)
            ct = 1

            for iter1 in list1:
                f2 = open(fwrite+fname1+"1_"+str(ct)+".txt","w")
                f2.write(iter1)
                print "1_"+str(ct)+"written"
                ct = ct+1


        if aspect =="screen":
            fname1    = "1_screen\\split"
            f1 = open("1_screen.txt","r")
            list1 = splitpara1(f1.read())
            list1.pop(len(list1) - 1)
            ct = 1

            for iter1 in list1:
                f2 = open(fwrite+fname1+"1_"+str(ct)+".txt","w")
                f2.write(iter1)
                print "1_"+str(ct)+"written"
                ct = ct+1

        if aspect =="battery":
            fname1    = "1_battery\\split"
            f1 = open("1_battery.txt","r")
            list1 = splitpara1(f1.read())
            list1.pop(len(list1) - 1)
            ct = 1

            for iter1 in list1:
                f2 = open(fwrite+fname1+"1_"+str(ct)+".txt","w")
                f2.write(iter1)
                print "1_"+str(ct)+"written"
                ct = ct+1

        if aspect =="performance":
            fname1    = "1_performance\\split"
            f1 = open("1_performance.txt","r")
            list1 = splitpara1(f1.read())
            list1.pop(len(list1) - 1)
            ct = 1

            for iter1 in list1:
                f2 = open(fwrite+fname1+"1_"+str(ct)+".txt","w")
                f2.write(iter1)
                print "1_"+str(ct)+"written"
                ct = ct+1

    if flag == 2:
        
        if aspect =="camera":
            fname1    = "2_camera\\split"
            f1 = open("2_camera.txt","r")
            list1 = splitpara1(f1.read())
            list1.pop(len(list1) - 1)
            ct = 1

            for iter1 in list1:
                f2 = open(fwrite+fname1+"2_"+str(ct)+".txt","w")
                f2.write(iter1)
                print "2_"+str(ct)+"written"
                ct = ct+1


        if aspect =="screen":
            fname1    = "2_screen\\split"
            f1 = open("2_screen.txt","r")
            list1 = splitpara1(f1.read())
            list1.pop(len(list1) - 1)
            ct = 1

            for iter1 in list1:
                f2 = open(fwrite+fname1+"2_"+str(ct)+".txt","w")
                f2.write(iter1)
                print "2_"+str(ct)+"written"
                ct = ct+1

        if aspect =="battery":
            fname1    = "2_battery\\split"
            f1 = open("2_battery.txt","r")
            list1 = splitpara1(f1.read())
            list1.pop(len(list1) - 1)
            ct = 1

            for iter1 in list1:
                f2 = open(fwrite+fname1+"2_"+str(ct)+".txt","w")
                f2.write(iter1)
                print "2_"+str(ct)+"written"
                ct = ct+1

        if aspect =="performance":
            fname1    = "2_performance\\split"
            f1 = open("2_performance.txt","r")
            list1 = splitpara1(f1.read())
            list1.pop(len(list1) - 1)
            ct = 1

            for iter1 in list1:
                f2 = open(fwrite+fname1+"2_"+str(ct)+".txt","w")
                f2.write(iter1)
                print "2_"+str(ct)+"written"
                ct = ct+1

    if flag == 3:
        
        if aspect =="camera":
            fname1    = "3_camera\\split"
            f1 = open("3_camera.txt","r")
            list1 = splitpara1(f1.read())
            list1.pop(len(list1) - 1)
            ct = 1

            for iter1 in list1:
                f2 = open(fwrite+fname1+"3_"+str(ct)+".txt","w")
                f2.write(iter1)
                print "3_"+str(ct)+"written"
                ct = ct+1


        if aspect =="screen":
            fname1    = "3_screen\\split"
            f1 = open("3_screen.txt","r")
            list1 = splitpara1(f1.read())
            list1.pop(len(list1) - 1)
            ct = 1

            for iter1 in list1:
                f2 = open(fwrite+fname1+"3_"+str(ct)+".txt","w")
                f2.write(iter1)
                print "3_"+str(ct)+"written"
                ct = ct+1

        if aspect =="battery":
            fname1    = "3_battery\\split"
            f1 = open("3_battery.txt","r")
            list1 = splitpara1(f1.read())
            list1.pop(len(list1) - 1)
            ct = 1

            for iter1 in list1:
                f2 = open(fwrite+fname1+"3_"+str(ct)+".txt","w")
                f2.write(iter1)
                print "3_"+str(ct)+"written"
                ct = ct+1

        if aspect =="performance":
            fname1    = "3_performance\\split"
            f1 = open("3_performance.txt","r")
            list1 = splitpara1(f1.read())
            list1.pop(len(list1) - 1)
            ct = 1

            for iter1 in list1:
                f2 = open(fwrite+fname1+"3_"+str(ct)+".txt","w")
                f2.write(iter1)
                print "3_"+str(ct)+"written"
                ct = ct+1


for i in range(1,4):
    f=open("output"+str(i)+".txt","r")
    filew= open(str(i)+"_allrev.txt","w")

    for line in f:
         for x in line:
             filew.write(x)
             if x is per:
                 filew.write("\n")

    
    clas(str(i)+"_camera.txt","camera")
    clas(str(i)+"_screen.txt","screen")
    clas(str(i)+"_battery.txt","battery")
    clas(str(i)+"_performance.txt","performance")
    clas(str(i)+"_performance.txt","phone")
    
    f.close()
    filew.close()
    
    #clas(str(i)+"_camera.txt","Camera")
    '''clas(str(i)+"_screen.txt","screen")
    #clas(str(i)+"_screen.txt","Screen")
    clas(str(i)+"_battery.txt","battery")
    #clas(str(i)+"_battery.txt","Battery")
    clas(str(i)+"_performance.txt","performance")
    #clas(str(i)+"_performance.txt","Performance")
    clas(str(i)+"_performance.txt","phone")
    #clas(str(i)+"_performance.txt","Phone")

filew.close()'''

for j in range(1,4):
    splitfile(j,"camera")
    splitfile(j,"screen")
    splitfile(j,"battery")
    splitfile(j,"performance")

print "Test"    

