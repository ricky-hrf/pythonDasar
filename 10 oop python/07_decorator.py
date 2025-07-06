class Hero:

  __jumlah = 0;

  def __init__(self, name):
    self.__name = name
    Hero.__jumlah += 1

  @staticmethod
  def getJumlah():
    return Hero.__jumlah
    
  @classmethod
  def getJumlah2(cls):
    return cls.__jumlah
  
mage = Hero("Lilya")
print(Hero.getJumlah())
tank = Hero("Tigreal")
print(Hero.getJumlah2())
print(tank.getJumlah2())
