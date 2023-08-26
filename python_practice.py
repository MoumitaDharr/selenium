class Person :
    name = ""
    age  = ""

    def display (self):
         print(f"name: {self.name}, age : {self.age}" )



person1 = Person ()
person1.name = "moumita"
person1.age = 25
person1.display ()

class Car:
    carsmake = ""
    model = ""
    year = ""

    def display (self):
        print(f"carsmake : {self.carsmake}, model : {self.model}, year : {self.year}")

car1 = Car()
car1.carsmake = "mhhjgj"
car1.model = "porche 911 GT"
car1.year = 2020
car1.display ()
