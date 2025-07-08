'''class Hero:

  def __init__(self, name, health):
    self.name = name
    self.health = health

class mage(Hero):
  def __init__(self,name):
    super().__init__(name, 100)

class marksmam(Hero):
  def __init__(self, name):
    super().__init__(name, 120)

hero1 = mage("lilya")
print(hero1.__dict__)

# contoh 2
class Person:
  name = ""
  age = 0
  def __init__(self, name,age):
    self.name = name
    self.age = age

  def show_name(self):
    print(self.name)

  def show_age(self):
    print(self.age)

class Student(Person):
  studentId = ""
  def __init__(self,student_name,student_age,student_id):
    super().__init__(student_name,student_age )
    self.studentId = student_id

  def get_id(self):
    return self.studentId

s1 = Student("Ika", 17,222)
print(s1.get_id())
'''

# contoh 3
class Parent:
  def __init__(self,name):
    self.name = name

  def greet(self):
    print(f"Hello from parent {self.name}")

class Child(Parent):
  def __init__(self, name,age):
    super().__init__(name)
    self.age = age