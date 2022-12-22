car = 'mitsubishi'
print(car == 'mitsubishi')
print(car == 'nissan')

car = 'BMW'
print(car == 'BMW')
print(car.lower() == 'BMW')

age = 13
print(age > 11)
print(age > 15)
print(age < 17)
print(age < 12)
print(age >= 13)
print(age >= 16)
print(age <= 12)
print(age <= 14)

age_0 = 13
age_1 = 20
print(age_0 >= 12 and age_1 >= 20)
print(age_0 <= 14 and age_1 <= 14)
print(age_0 >= 19 or age_1 <= 19)
print(age_0 <= 11 or age_1 >= 11)

cars = ['Honda', 'Toyota', 'Mitsubishi']
print('Honda' in cars)
print('Volkswagen' in cars)
