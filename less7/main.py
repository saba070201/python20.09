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
        w_a_f.write('\n'+str(text)+' time: '+str(time))
def comb_sort(arr):
    step=int(len(arr)/1.247)
    swap=1
    while step > 1 or swap>0:
        swap=0
        i=0
        while i+step < len(arr):
            if arr[i] > arr[i+step]:
                arr[i],arr[i+step]=arr[i+step],arr[i]
                swap+=1
            i+=1
        if step>1:
            step=int(step/1.247)
 

# arr100000=[]
# read_from_file(arr100000,path100000)
# st=time.time()
# bSort(arr100000)
# et=time.time()
# ft=et-st
# write_results(res,'arr100000-bubble',ft)
arr1=[3,1,2]
print(comb_sort(arr1))
