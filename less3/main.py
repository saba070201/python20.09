# # def print_alert(name,sum):
# #   print(f'{name}, ты должен заплатить {sum}!')
# # test_value=100
# # print_alert(input('name:'),-2000,1313)
# print(1,2,3,4,5,6,7,7,8,9,)
# import random 
# def add_to_array_random_values(array:list,lenght:int):
#   for i in range(lenght):
#     array.append(random.randint(1,1000))
#   return array 
# array=[]
# array_full=add_to_array_random_values(array,5)
# print(array_full)
# from less3.foos.functions import * 
# summator(1,2)
from typing import List


def create_array(array:list,size:int):
  for i in range(size):
    array.append(i)
def change_indexes(array:list,index1:int,index2:int):
  array[index1],array[index2]= array[index2],array[index1]

array=[]
succesfull_array=[1,2,3,4]
create_array(array,10)
change_indexes(array,0,9)
change_indexes(succesfull_array,0,3)
print(succesfull_array)



