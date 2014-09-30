def splitpara1(file):
              import re
              sentenceEnders = re.compile("\n\n")
              sentenceList = sentenceEnders.split(file)
              return sentenceList

fn = "D:\\Academics\\Project\\Files\\output1\\"
f1 = open("D:\\Academics\\Project\\Files\\output1.txt","r")
list1 = splitpara1(f1.read())
print list1.pop(len(list1)-1)

ct = 1

for iter1 in list1:
    f2 = open(fn+"1_"+str(ct)+".txt","w")
    f2.write(iter1)
    print "1_"+str(ct)+"written"
    ct = ct+1
    
fn = "D:\\Academics\\Project\\Files\\output2\\"            
f1 = open("D:\\Academics\\Project\\Files\\output2.txt","r")
list1 = splitpara1(f1.read())
print list1.pop(len(list1)-1)

ct = 1

for iter1 in list1:
    f2 = open(fn+"2_"+str(ct)+".txt","w")
    f2.write(iter1)
    print "2_"+str(ct)+"written"
    ct = ct+1
    
fn = "D:\\Academics\\Project\\Files\\output3\\"            
f1 = open("D:\\Academics\\Project\\Files\\output3.txt","r")
list1 = splitpara1(f1.read())
print list1.pop(len(list1)-1)

ct = 1

for iter1 in list1:
    f2 = open(fn+"3_"+str(ct)+".txt","w")
    f2.write(iter1)
    print "3_"+str(ct)+"written"
    ct = ct+1
    
