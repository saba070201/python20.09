# # class Phone():
# #   def __init__(self,display,camera,corpus,battery,CPU):
# #     self.display=display
# #     self.camera=camera
# #     self.corpus=corpus
# #     self.battery=battery
# #     self.CPU=CPU
# #     print('init was created ')
# #   def __del__(self):
# #     print('object was deleted')
# #   def call(self):
# #     print('phone is calling')
# #   def show_info(self):
# #     print(self.display,self.camera,self.corpus,self.battery,self.CPU,sep='|')
# # Xiaomi=Phone('supep puper amoled','100000mp','draharis super puper armored','100000mah','processor')
# # Iphone14=Phone('Retina','sony 64mp','glass','5000mah','A15 bionic')
# # # Xiaomi.show_info()
# # phones=[Xiaomi,Iphone14]
# # print(phones[1].camera)
# import random 
# class Sword:
#   def __init__(self,damage,crit,chance):
#     self.damage=damage
#     self.crit=crit
#     self.chance=chance
#   def crit_or_not(self):
#     arr=list(range(1,101))
#     random_value=random.randint(1,100)
#     if random_value<=self.chance:
#       damage=self.crit*self.damage
#       print('Выпал крит!!!')
#       return damage
#     else:
#       damage=self.damage
#       return damage 
# class Hero:
#   def __init__(self,name,health,sword:Sword) -> None:
#     self.name=name
#     self.health=health
#     self.sword=sword
#   def Attack(self,hero:'Hero'):
#     hero.health-=self.sword.crit_or_not()
# def battle(hero1:Hero,hero2:Hero,sword_hero1:Sword,sword_hero2:Sword):
#   while True:
#     if hero1.health<=0 :
#       print(f'{hero2.name} победил')
#       break
#     hero1.Attack(hero2)
#     print(f'{hero1.name} ударил!',hero2.health)
#     if hero2.health<=0:
#       print(f'{hero1.name}победил')
#       break
#     hero2.Attack(hero1)
#     print(f'{hero2.name} ударил!',hero1.health)
# frostmorn=Sword(10,1.5,50)
# peace_of_shit=Sword(10,3,50)
# Artes=Hero('Artes',100,frostmorn)
# Illidan=Hero('Illidan',100,peace_of_shit)
# battle(Artes,Illidan,frostmorn,peace_of_shit)
class Thing(object):
  def eat(self):
    print('eating')
  def breathe(self):
    print('breathe')
  def multiply(self):
    print('multiply')
  def exude(self):
    print('exude')
  def __init__(self,cell):
    self.cell=cell
  def show_info(self):
    print(self.cell)
class Human(Thing):
  def __init__(self, cell,brain):
    self.brain=brain
    super().__init__(cell)
  def learn_python(self):
    print('learn python')
  def show_info(self):
    print(self.cell,self.brain)
ameba=Thing('a1414mxg')
person=Human('b120','200iq')
# ameba.breathe()
# person.breathe()
# print(ameba.brain,person.cell)
ameba.show_info()
person.show_info()


    