class Person:

  def __init__(self, name, address, job):
    self.name = name
    self.address = address
    self.job = job

    # private variable
    self.__age = 43

nias = Person("Ododogo","Kampung","CEO")
print(nias.name)    
print(nias.__age)    