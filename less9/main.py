# import threading
# import threading

# def writer(x, event_for_wait, event_for_set):
#     for i in range(10):
#         event_for_wait.wait() 
#         event_for_wait.clear() 
#         print(x)
#         event_for_set.set() 


# e1 = threading.Event()
# e2 = threading.Event()
# e3 = threading.Event()


# t1 = threading.Thread(target=writer, args=(0, e1, e2))
# t2 = threading.Thread(target=writer, args=(1, e2, e3))
# t3 = threading.Thread(target=writer, args=(2, e3, e1))


# t1.start()
# t2.start()
# t3.start()

# e1.set()


# t1.join()
# t2.join()
# t3.join()
class RimsAddArabian(Exception):
  def __init__(self, *args: object) -> None:
    if args:
      self.message=args[0]
    else:
      self.message=None
    
  def __str__(self) -> str:
    if self.message:
      return self.message
    else:
      return 'no message' 
class RimsValue:
  #!  это полная шляпа, ее надо исправить или куда то деть 
  # 1 вариант: сделать поле nums приватным , 2 вариант: сделать его отдельным классом или отдельным словарем 
  nums={'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'VII':7,'VIII':8,'IX':9,'X':10}
  def __init__(self,value) -> None:
    self.arabianvalue=self.nums[value]
    self.value  =value
  def __str__(self) -> str:
    return self.value
class ArabianValue:
  def __init__(self,value) -> None:
    self.value=value
    self.arabianvalue=value
class Calculate:
  @staticmethod
  def convert_arabic_to_rim(arabicnum):
    result=str()
    num = [1, 4, 5, 9, 10, 40, 50, 90,
      100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
      "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    while arabicnum:
      div = arabicnum // num[i]
      arabicnum %= num[i]

      while div:
          result+=sym[i]
          div -= 1
      i -= 1
    return result
  @staticmethod
  def operation(first,second,operetion='+'):
    nums={1:'I',5:'V',10:'X'}
    if type(first)!=type(second):
      raise RimsAddArabian('нельзя складывать арабские и римские цифры')
    else:
      res=0
      if type(first)==ArabianValue:
        pass
      else:
        if operetion=='+':
          res=first.arabianvalue+second.arabianvalue
          res=Calculate.convert_arabic_to_rim(res)
          return res
        elif operetion=='-':
          res=first.arabianvalue-second.arabianvalue
          if res<1:
            raise RimsAddArabian('результат меньше 1')
          res=Calculate.convert_arabic_to_rim(res)
          return res

rv=RimsValue('X')
av=RimsValue('IX')

print(Calculate.operation(rv,av,'-'))

# print(rv.arabicvalue)
# raise RimsAddArabian('нельзя складывать арабские и римские цифры')
#Александру 
from math import sqrt
import random
def bSort(array):
    # определяем длину массива
    length = len(array)
    #Внешний цикл, количество проходов N-1
    for i in range(length):
        # Внутренний цикл, N-i-1 проходов
        for j in range(0, length-i-1):
            #Меняем элементы местами
            if sqrt(array[j][0]**2 +array[j][1]**2+array[j][2]**2)> sqrt(array[j+1][0]**2+array[j+1][1]**2+array[j+1][2]**2):
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
l=[[random.randint(1,100) for i in range(3)] for i in range(100)]
bSort(l)


print(l)
