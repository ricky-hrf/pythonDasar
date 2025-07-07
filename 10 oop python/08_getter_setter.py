class Hero:

  def __init__(self, name, health, armor):
    self.name = name
    self.__health = health
    self.__armor = armor

  @property
  def info(self):
    return "name {} : \n\thealth: {}".format(self.name,self.__health)
  
  @property
  def armor(self):
    return self.__armor
  
  @armor.setter
  def armor(self, input):
    self.__armor = input

  @armor.deleter
  def armor(self):
    print("armor dihapus")
    self.__armor = None

fighter = Hero("Aldous", 100, 10)

print("merubah info")
print(fighter.info)
fighter.name = "Balmond"
print(fighter.info)

print("getter dan setter untuk armor")
print(fighter.armor)
fighter.armor = 50
print(fighter.armor)