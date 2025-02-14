class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

  
 

car1 = Car(brand="Brand :chevrolet", model="Model: Blazer",year= "Year :2018")
car2 = Car(brand="Brand : Audi",model="Model: e-tron GT", year= "Year: 2020")

print(car1.brand,car1.model,car1.year)
print(car2.brand,car2.model,car2.year)

