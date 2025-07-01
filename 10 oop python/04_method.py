class Hero:
  jumlah_hero = 0 # Class variable to count heroes
  def __init__(self, nama, health, mana):
    # variables to store hero attributes
    self.nama = nama
    self.health = health
    self.mana = mana
    Hero.jumlah_hero += 1

  def info(self):
    # method to display hero information
    print(f"Nama: {self.nama}, Health: {self.health}, Mana: {self.mana}")

  def attack(self, target):
    # method to attack another hero
    print(f"{self.nama} menyerang {target.nama}!")
    target.health -= 10  # reduce target's health by 10
    print(f"{target.nama} sekarang memiliki {target.health} health.")

  def heal(self):
    # method using return statement to heal the hero
    self.health += 20
    return self.health

mage = Hero("Lilya", 100, 50)
tank = Hero("Grock", 200, 0)
fighter = Hero("Aldous", 150, 25)
marksman = Hero("Miya", 120, 10)
jungler = Hero("Hayabusa", 80, 30)
print(f"Jumlah hero: {Hero.jumlah_hero}")


mage.info()
tank.info()
fighter.info()
marksman.info()
jungler.info() 
mage.attack(tank)
print(f"{mage.nama} telah menyembuhkan dirinya sendiri, health sekarang: {mage.heal()}")
tank.attack(fighter)