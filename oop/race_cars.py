class Driver:

    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
    
class Car:

    def __init__(self, driver):
        self.driver = driver
        self.rank = 0

driver1 = Driver('Petar', 'Petrovic')
car1 = Car(driver1)
#object attribute attribute
print(car1.driver.name)