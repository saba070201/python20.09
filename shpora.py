import math

from colorama import Fore, Back, Style

V = [[0, 2, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf,
      math.inf],
     [2, 0, 2, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf],
     [math.inf, 2, 0, 2, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf],
     [math.inf, math.inf, 2, 0, 2, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf],
     [math.inf, math.inf, math.inf, 2, 0, 2, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf],
     [math.inf, math.inf, math.inf, math.inf, 2, 0, 2, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf],
     [math.inf, math.inf, math.inf, math.inf, math.inf, 2, 0, 2, math.inf, math.inf, math.inf, math.inf, math.inf],
     [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 2, 0, 2, math.inf, math.inf, math.inf,
      math.inf],
     [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 2, 0, 2, math.inf,
      math.inf, math.inf],
     [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 2, 0, 2,
      math.inf, math.inf],
     [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 1, math.inf, math.inf, math.inf, 0,
      2, math.inf],
     [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 2,
      0, 2],
     [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf,
      1, 0],
     ]


def get_path(P, u, v):
    if u > v:
        path = [u]
        while u != v:
            u = P[u][v]

            path.append(u)
        return path



    else:
        value = u
        value1 = v
        u = value1
        v = value
        path = [u]
        while u != v:
            u = P[u][v]

            path.append(u)
        return path[::-1]


def get_time(path):
    time = 0
    for index, value in enumerate(path):
        if index == len(path) - 1:
            break
        else:
            time = V[value][path[index + 1]] + time
    realtime = time * 3
    print(Fore.CYAN + '~' + str(realtime) + 'минут')


# 9


N = len(V)  # число вершин в графе
P = [[v for v in range(N)] for u in range(N)]  # начальный список предыдущих вершин для поиска кратчайших маршрутов

for k in range(N):
    for i in range(N):
        for j in range(N):
            d = V[i][k] + V[k][j]
            if V[i][j] > d:
                V[i][j] = d
                P[i][j] = k

Metro_Dictionary = {1: 'красная ветка', 2: 'синяяя ветка', 3: 'зеленая ветка'}
Stations = ((0, 'проспект ветеранов', 1), (1, 'ленинский проспект', 1), (2, 'автово', 1), (3, 'кировский завод', 1),
            (4, 'нарвская', 1), (5, 'балтийская', 1), (6, 'технологический институт I', 1), (7, 'пушкинская', 1),
            (8, 'владимрская', 1), (9, 'площадь востания', 1), (10, 'технологический институт II', 2),(11,'невский проспект',2),(12,'сенная площадь',2))


def MakeDict(S):
    Stat_Dictionary = {}
    for i in range(len(S)):
        Stat_Dictionary[S[i][1]] = i
    return Stat_Dictionary


print(Fore.BLUE)
St_dict = MakeDict(Stations)
s1 = input('Введите начальную станцию ')
s2 = input('Введите конечную станцию ')
try:
    start = St_dict[s1]
    end = St_dict[s2]
    resu = get_path(P, end, start)[::-1]
except:
    print('такой/таких станций не существует , попробуйте еще раз')
    s1 = input('Введите начальную станцию ')
    s2 = input('Введите конечную станцию ')
    start = St_dict[s1]
    end = St_dict[s2]
    resu = get_path(P, end, start)[::-1]

colors = [Fore.RED, Fore.BLUE, Fore.GREEN, Fore.YELLOW, Fore.MAGENTA, Fore.WHITE]

for i in resu:
    if Stations[i][2] == 1:
        print(colors[0], Stations[i][1], end=colors[5] + ' ->')
    elif Stations[i][2] == 2:
        print(colors[1], Stations[i][1], end=colors[5] + ' ->')
    elif Stations[i][2] == 3:
        print(colors[2], Stations[i][1], end=colors[5] + ' ->')
    elif Stations[i][2] == 4:
        print(colors[4], Stations[i][1], end=colors[5] + ' ->')
    elif Stations[i][2] == 5:
        print(colors[5], Stations[i][1], end=colors[5] + ' ->')

get_time(resu)

print(P)
#код с пары
# import math

# from colorama import Fore, Back, Style

# V = [[0, 2, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf,
#       math.inf],
#      [2, 0, 2, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf],
#      [math.inf, 2, 0, 2, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf],
#      [math.inf, math.inf, 2, 0, 2, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf],
#      [math.inf, math.inf, math.inf, 2, 0, 2, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf],
#      [math.inf, math.inf, math.inf, math.inf, 2, 0, 2, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf],
#      [math.inf, math.inf, math.inf, math.inf, math.inf, 2, 0, 2, math.inf, math.inf, math.inf, math.inf, math.inf],
#      [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 2, 0, 2, math.inf, math.inf, math.inf,
#       math.inf],
#      [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 2, 0, 2, math.inf,
#       math.inf, math.inf],
#      [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 2, 0, 2,
#       math.inf, math.inf],
#      [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 1, math.inf, math.inf, math.inf, 0,
#       2, math.inf],
#      [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 2,
#       0, 2],
#      [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf,2,
#       2, 0],
#      ]


# def get_path(P, u, v):
#     if u > v:
#         path = [u]
#         while u != v:
#             u = P[u][v]

#             path.append(u)
#         return path



#     else:
#         value = u
#         value1 = v
#         u = value1
#         v = value
#         path = [u]
#         while u != v:
#             u = P[u][v]

#             path.append(u)
#         return path[::-1]


# def get_time(path):
#     time = 0
#     for index, value in enumerate(path):
#         if index == len(path) - 1:
#             break
#         else:
#             time = V[value][path[index + 1]] + time
#     realtime = time * 3
#     print(Fore.CYAN + '~' + str(realtime) + 'минут')


# # 9


# N = len(V)  # число вершин в графе
# P = [[v for v in range(N)] for u in range(N)]  # начальный список предыдущих вершин для поиска кратчайших маршрутов
# for k in range(N):
#     for i in range(N):
#         for j in range(N):
#             d = V[i][k] + V[k][j]
#             if V[i][j] > d:
#                 V[i][j] = d
#                 P[i][j] = k

# Metro_Dictionary = {1: 'красная ветка', 2: 'синяяя ветка', 3: 'зеленая ветка'}
# Stations = ((0, 'проспект ветеранов', 1), (1, 'ленинский проспект', 1), (2, 'автово', 1), (3, 'кировский завод', 1),
#             (4, 'нарвская', 1), (5, 'балтийская', 1), (6, 'технологический институт I', 1), (7, 'пушкинская', 1),
#             (8, 'владимрская', 1), (9, 'площадь востания', 1), (10, 'технологический институт II', 2),(11,'невский проспект',2),(12,'сенная площадь',2))


# def MakeDict(S):
#     Stat_Dictionary = {}
#     for i in range(len(S)):
#         Stat_Dictionary[S[i][1]] = i
#     return Stat_Dictionary


# print(Fore.BLUE)
# St_dict = MakeDict(Stations)
# s1 = input('Введите начальную станцию ')
# s2 = input('Введите конечную станцию ')
# try:
#     start = St_dict[s1]
#     end = St_dict[s2]
#     resu = get_path(P, end, start)[::-1]
# except:
#     print('такой/таких станций не существует , попробуйте еще раз')
#     s1 = input('Введите начальную станцию ')
#     s2 = input('Введите конечную станцию ')
#     start = St_dict[s1]
#     end = St_dict[s2]
#     resu = get_path(P, end, start)[::-1]

# colors = [Fore.RED, Fore.BLUE, Fore.GREEN, Fore.YELLOW, Fore.MAGENTA, Fore.WHITE]

# for i in resu:
#     if Stations[i][2] == 1:
#         print(colors[0], Stations[i][1], end=colors[5] + ' ->')
#     elif Stations[i][2] == 2:
#         print(colors[1], Stations[i][1], end=colors[5] + ' ->')
#     elif Stations[i][2] == 3:
#         print(colors[2], Stations[i][1], end=colors[5] + ' ->')
#     elif Stations[i][2] == 4:
#         print(colors[4], Stations[i][1], end=colors[5] + ' ->')
#     elif Stations[i][2] == 5:
#         print(colors[5], Stations[i][1], end=colors[5] + ' ->')

# get_time(resu)
# balance=input()
# try: 
#   balance=int(balance)
#   print('все ок ')
# except Exception as e :
#   print(e)
#   balance=0
# finishbalance=0.95*balance
# print(finishbalance)
# print('start')
# raise 
# print('end')
# class VE(ValueError):
#   def __init__(self, *args: object) -> None:
#     super().__init__(*args)
#   def __str__(self) -> str:
#     return super().__str__()
# ve=VE('sfaf')
# print(ValueError)
# # try: 
# #   balance=int(balance)
# #   print('все ок ')
# # except Exception as e :
# #   print(e)
# #   balance=0
class Card():
  def __init__(self,number,balance):
    self.number=number
    self.balance=balance
class Terminal():
  def __init__(self,balance) -> None:
    self.balance=balance
  def pay(self,card,terminal,price,status=False):
    return Tranzaction(price,card,terminal,status)
  def get_query(self,tranzaction):
    if tranzaction.status==True:
      del tranzaction
    else:
      print('Упс что то пошло не так')

class Tranzaction():
  def __init__(self,price,card:Card,terminal:Terminal,status:bool) -> None:
    self.price=price
    self.card=card
    self.terminal=terminal
    self.status=status
  def __del__(self):
    print('транзакция была удалена')
class MyServer():
  def __init__(self,cards) -> None:
    self.cards=cards
  def get_query(self,tranzaction:Tranzaction):
    try:
      assert(tranzaction.card.balance>=tranzaction.price)
      tranzaction.status=True
      tranzaction.card.balance-=tranzaction.price
      tranzaction.terminal.balance+=tranzaction.price
    except:
      tranzaction.status=False
  # def post_query(self,tranzaction:Tranzaction):
  #   if tranzaction.status==True:
  #     return True
  #   else:
  #     return False
card=Card(123,150)
terminal=Terminal(0)
server=MyServer(1)
tranzaction=terminal.pay(card,terminal,200)
server.get_query(tranzaction)
terminal.get_query(tranzaction)
print(card.balance)
print(terminal.balance)


    

