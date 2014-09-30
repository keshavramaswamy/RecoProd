import csv

list1 =[]
with open('output1.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        list1.append(row)

list1.pop(0)
sum1 = 0


for iter in range(0,len(list1)):
    sc1 = float(list1[iter][len(list1[iter])-2])
    sum1 = sum1 + sc1*5

average1 = sum1/ len(list1)

list2 =[]
with open('output2.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        list2.append(row)

list2.pop(0)
sum2 = 0

print list2


for iter in range(0,len(list2)):
    sc1 = float(list2[iter][len(list2[iter])-2])
    sum2 = sum2 + sc1*5

average2 = sum2/ len(list2)

list3 =[]
with open('output3.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        list3.append(row)

list3.pop(0)
sum3 = 0


for iter in range(0,len(list3)):
    sc1 = float(list3[iter][len(list3[iter])-2])
    sum3 = sum3 + sc1*5

average3 = sum3/ len(list3)


'''
print  average1
print  average2
print  average3

'''
fw = open("rating.txt","w")
fw.write(str(average1))
fw.write("\n")
fw.write(str(average2))
fw.write("\n")
fw.write(str(average3))
fw.write("\n")
fw.close()







