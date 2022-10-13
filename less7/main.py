import random
import time
def bSort(array):
    # определяем длину массива
    length = len(array)
    #Внешний цикл, количество проходов N-1
    for i in range(length):
        # Внутренний цикл, N-i-1 проходов
        for j in range(0, length-i-1):
            #Меняем элементы местами
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
# arr=[random.randint(1,1000000) for i in range(1000)]
# print(bSort(arr))
path100='less7/files/arr100.txt'
path1000='less7/files/arr1000.txt'
path5000='less7/files/arr5000.txt'
path10000='less7/files/arr10000.txt'
path100000='less7/files/arr100000.txt'
res='less7/files/results.txt'
# arr=[random.randint(1,1000000) for i in range(100000)]
def write_to_file(arr,path):
    with open(path,'w') as wf:
        for i in range(len(arr)):
            wf.write(str(arr[i])+'\n')
def read_from_file(arr,path):
    with open(path,'r') as rf:
        for i in rf:
            arr.append(int(i))
def write_results(path,text,time):
    with open(path,'a') as w_a_f:
        w_a_f.write(str(text)+' time: '+str(time))

arr100=[]
read_from_file(arr100,path100)
st=time.time()
bSort(arr100)
et=time.time()
ft=et-st
write_results(res,'arr100-bubble',ft)
