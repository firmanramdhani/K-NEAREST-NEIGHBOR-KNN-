import math
import sys
import csv
import collections

#menghitung jarak antara dua data
def jarak(ax,ay):
    a = map(lambda x,y: (x - y)**2, ax, ay)
    return math.sqrt(sum(a))

#membaca data train dan data test
def loadData():
    dataHasil1=[]
    dataHasil2=[]
    with open('DataTrain_Tugas3_AI.csv') as dataTrain:
            reader1 = csv.reader(dataTrain, delimiter=',')
            next(reader1)
            for row in reader1:
                dataHasil1.append(list(map(lambda x: float(x), row[1:])))
    with open('DataTest_Tugas3_AI.csv') as dataTest:
            reader2 = csv.reader(dataTest, delimiter=',')
            next(reader2)
            
            for row in reader2:
                dataHasil2.append(list(map(lambda x: float(x), row[1:6])))  
    return dataHasil1,dataHasil2

#menyimpan data
def dataHasil(hasil):
    with open('TebakanTugas3.csv', mode='w') as dHasil:
        writer = csv.writer(dHasil, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        i = 1
        for n in hasil:
            writer.writerow([n])
            i += 1

#main program
k = 7
dataTrain, dataTest = loadData()
hasil = []
for test in dataTest:
    list_distance = []
    for train in dataTrain:
        list_distance.append([jarak(test, train[:5]), train[5]]) 
    list_distance.sort(key=(lambda x:x[0]))         
    nearest_distance = list_distance[:k]            
    distance, class_type = zip(*nearest_distance)   
    counter = collections.Counter(class_type)       
    result = counter.most_common(1)[0][0]           
    print (result)                                
    hasil.append(int(result))                      
dataHasil(hasil)
        

