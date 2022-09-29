# # # less4
# # import colorama 
# # print(colorama.Fore.YELLOW)
# # print('this is yellow !!!')
# # def bad_print(word):
# #   print(word)
# # def good_print(*args):
# #   print(args[0])
# # # bad_print('misha','python')
# # good_print('misha','python','=love')
# # def calculator(a,b,operation='+'):
# #   if operation=='+':
# #     c=a+b
# #     print(c)
# #   elif operation=='-':
# #     c=a-b
# #     print(c)
# # calculator(3,2)
# # print('a','b')
# import random
# path='less4/files/text.txt'
# # with open(path,'r')as f : 
# #   data=f.read()
# # print(data)
# # file=open(path,'w')
# # file.write('hello world!')
# # file.close()
# def write_to_file(path,size=100):
#   with open(path,'w') as wf:
#     for i in range(size):
#       wf.write(str(random.randint(1,1000))+'\n')
# def read_from_file(path,array:list):
#     with open(path,'r') as rf:
#       for i in rf:
#         array.append(int(i))
# arr=[]
# read_from_file(path,arr)
# print(arr)
# a=1
# print(type(a))
from cmath import sqrt


# class Rectangle():
#   weight=None
#   height=None
# rectangle=Rectangle()
# rectangle.height=10
# rectangle.weight=5
# print(rectangle.height,rectangle.weight)
# sqrt()
import math
# class Triangle:
#   def __init__(self,a,b,c):
#     self.a=a
#     self.b=b
#     self.c=c
#     p=(a+b+c)/2
#     self.area=math.sqrt(p*(p-a)*(p-b)*(p-c))
#   def show_info(self):
#     print(self.a,self.b,self.c,self.area)
# triangle=Triangle(3,2,4)
# triangle.show_info()
# def run(thing):
#   print('run!')
# class Cat():
#   def __init__(self):
#     pass
#   def run(self,thing):
#     print('run!')
# cat=Cat()
# apple='apple'
# cat.run('blabla')
# run(cat)
# run(apple)
# apple.r
class Point():
  def __init__(self,x,y) -> None:
    self.x=x
    self.y=y

    


