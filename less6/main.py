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
import abc
class Sky_object(abc.ABC):
  def __init__(self,radius,mass) -> None:
    super().__init__()
    self.radius=radius
    self.mass=mass
   
  @abc.abstractclassmethod
  def make_gravity(self):
    print('make gravity ')
class Star(Sky_object):
  def __init__(self, radius, mass,type) -> None:
    super().__init__(radius, mass)
    self.type=type
  def make_gravity(self):
    print('make gravity ')
class Planet(Sky_object):
  def __init__(self, radius, mass,aborigens) -> None:
    super().__init__(radius, mass)
    self.aborigens=aborigens
  def make_gravity(self):
    print('make gravity ')
def collide(obj1:Sky_object,obj2:Sky_object):
  print(f'объект с радиусом {obj1.radius} столкнулся с объектом радиусом {obj2.radius}')
earth=Planet(4000,1000,'люди')
bethelgeize=Star(10000000,100000,'красный гигант')
collide(earth,bethelgeize)

