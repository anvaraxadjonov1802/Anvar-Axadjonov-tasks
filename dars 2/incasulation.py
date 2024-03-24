class Car:
    model = "Maluba"
    __price = 25000
    color = "black"

    def  getter(self):
        return self.__price
    
    def setter(self, new_price):
        self.__price = new_price
        return self.__price
    
    def __hello(self):
        return "Hello World"

car1 = Car()

print(car1.getter())

# print(car1.__price) #Error
# print(car1.__hello) #Error

car1.setter(26000)
print(car1.getter())