class Hero:
  jumlah = 0 # global variables yang dimiliki oleh class
  def __init__(self, name, health, magicPower):
    # instance variables, yang dimiliki oleh objek
    self.name = name
    self.health = health
    self.power = magicPower
    Hero.jumlah += 1
    print("Membuat hero dengan nama ", name)

mage = Hero("Lilya", 9, 85)
print(mage.__dict__)
print(Hero.jumlah)
marksmam = Hero("Miya", 4, 134)
print(marksmam.__dict__)
print(Hero.jumlah)