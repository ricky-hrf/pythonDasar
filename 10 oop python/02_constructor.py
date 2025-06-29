class Hero:
  def __init__(self, name, health, magicPower):
    self.name = name
    self.health = health
    self.power = magicPower

mage = Hero("Lilya", 9, 85)
print(mage.__dict__)