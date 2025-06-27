class hero: # ini adalah template
  pass


marksmam = hero() # ini adalah object(instance)
mage= hero()
fighter = hero()

marksmam.name = "Miya"
marksmam.health = 10

mage.name = "Lilya"
mage.health = 7

fighter.name = "Dyroth"
fighter.health = 8

print(mage.__dict__)
print(mage)
print(mage.name)