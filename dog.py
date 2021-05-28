class Dog:
     def __init__(self,breed,name,age):
         self.breed=breed
         self.name=name
         self.age=age
     def details(self):
         return f"The dog {self.name} which is {self.age} years old is a {self.breed}" 
     def birthYear(self):
         return 2021-self.age        
         