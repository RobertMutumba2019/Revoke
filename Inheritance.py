#In python, classes can inherit where by the child class can have attributes of the Parent class.
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)