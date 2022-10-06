# import abc 
# class Thing(abc.ABC):
#   def __init__(self,size) :
#     self.size=size
#   @abc.abstractclassmethod
#   def break__(self):
#     pass
# class Atom(Thing):
#   def __init__(self, size,weight):
#     super().__init__(size)
#     self.weight=weight
#   def break__(self):
#     pass
# # thing=Thing()
# H=Atom(0.0000001,0.00000000002)
# import abc
# class Sky_object(abc.ABC):
#   def __init__(self,radius,mass) -> None:
#     super().__init__()
#     self.radius=radius
#     self.mass=mass
   
#   @abc.abstractclassmethod
#   def make_gravity(self):
#     print('make gravity ')
# class Star(Sky_object):
#   def __init__(self, radius, mass,type) -> None:
#     super().__init__(radius, mass)
#     self.type=type
#   def make_gravity(self):
#     print('make gravity ')
# class Planet(Sky_object):
#   def __init__(self, radius, mass,aborigens) -> None:
#     super().__init__(radius, mass)
#     self.aborigens=aborigens
#   def make_gravity(self):
#     print('make gravity ')
#   @staticmethod
#   def test_static():
#     print('you used static method')
# def collide(obj1:Sky_object,obj2:Sky_object):
#   print(f'объект с радиусом {obj1.radius} столкнулся с объектом радиусом {obj2.radius}')
# earth=Planet(4000,1000,'люди')
# bethelgeize=Star(10000000,100000,'красный гигант')

# class Calculation():
#   @staticmethod
#   def calc_gravity_force(obj1:Sky_object,obj2:Sky_object,R):
#     G=6.67*(10**-11)
#     force=(G*obj1.mass*obj2.mass)/R**2
#     return force
# force=Calculation.calc_gravity_force(earth,bethelgeize,1000)
# print(force)
## Создать структуру классов, где есть все отношения(ассоциация, агрегация, реализация,наседование)
import time 
import numpy as np 
import random
path='less6/files/arrays.txt'
def write_to_file(path_to_file,arr):
  with open(path_to_file,'w') as f:
    for i in arr:
      f.write(str(i)+'\n')
def bubble_sort(arr):
  last_index=len(arr)-1
  for i in range(last_index):
    for j in range (last_index):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1]=arr[j+1],arr[j]
def read_from_file(path_to_file,arr):
  with open(path_to_file,'r') as f:
    for i in f:
      arr.append(int(i))
# N=10000
# a=[random.randint(0,100000) for i in range(N)]
arr=[]
read_from_file(path,arr)
arr_numpy=np.array(arr)
st0=time.time()
bubble_sort(arr_numpy)
et0=time.time()
ft0=et0-st0
print(ft0)
# # arr_numpy=np.array(arr)
# # bubble_sort(arr)



