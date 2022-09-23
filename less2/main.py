# Цикл - это последовательность действий 
# k=1
# n=10
# while k<10: 
#   print(f' до сложения с 1 k- {k}')
#   k=k+1
#   print(f' после сложения с 1 k-{k}')
from ctypes import wstring_at
from lib2to3.pgen2.token import VBAR


k=0
# while k<5:
#   if k==3:
#     print('k=3')
#     k+=1
#     continue
#   print(k)
#   k+=1
# flag=True
# n=10
# while flag:
#   print(k)
#   if k==n-5:
    
#     flag=False
#   k+=1
# a=int(input())
# b=int(input())
# while a<=b:
#   if a==4:
#     print(a**3)
#     a+=1
#     continue
#   elif a%2==0:
#     print(a**2)
#   a+=1
# salaries=[1000,2000,5000]
# # salaries.append(99)
# salaries[3]=99
# print(salaries)
# arr=[1,2,3,4]
# # while True:
# #   a=int(input())
# #   if a==0:
# #     break
# #   arr.append(a)
# # for i in arr:
# #   print(i) 
# print(arr[1:3])
# arr=[]
# a=int(input())
# b=int(input())
# while a<=b:
#   arr.append(a)
#   a+=1
# print(arr)
# arr1=[1,2,3]
# arr2=arr1.copy()
# arr1[0]=4
# print(id(arr1),id(arr2))
# import random 
# arr=[random.randint(0,1000) for i in range (10)]
#1 -ПОСЧИТАТЬ СУММУ ЭЛЕМЕНТОВ В МАССИВЕ 
#2 - ПОМЕНЯТЬ МЕСТАМИ  ПЕРВЫЙ И ПОСЛЕДНИЙ ЭЛЕМЕНТ МАССИВА 
#-------------
# sum=0
# arr=[1,2,3,4,5]
# for i in arr:
#   sum+=i
# print(sum)
a=int(input())
b=int(input())
arr=[1,2,3,4,5]
# value1=arr[a]
# value2=arr[b]
# arr[a]=value2
# arr[b]=value1
arr[a],arr[b]=arr[b],arr[a]
print(arr)
#-------------

