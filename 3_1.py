from datetime import datetime
from random import random
from project_first_app.models import CarOwner, DriverLicense, Car, Possession

# Создаем 6-7 новых автовладельцев
owners_data = [
    {'surname': 'Иванов', 'name': 'Иван', 'date_birth': datetime(1990, 1, 1)},
    {'surname': 'Петров', 'name': 'Петр', 'date_birth': datetime(2000, 1, 1)},
    {'surname': 'Сидоров', 'name': 'Сидор', 'date_birth': datetime(1980, 3, 11)},
    {'surname': 'Иванов', 'name': 'Иван', 'date_birth': datetime(1990, 12, 21)},
    {'surname': 'Иванов', 'name': 'Иван', 'date_birth': datetime(2001, 10, 30)},
    {'surname': 'Иванова', 'name': 'Кристина', 'date_birth': datetime(1995, 4, 5)},

]

owners = []
for owner_info in owners_data:
    owner = CarOwner.objects.create(**owner_info)
    owners.append(owner)

# Создаем 5-6 автомобилей
cars_data = [
    {'state_number': 'ABC123', 'brand': 'Toyota', 'model': 'Camry', 'color': 'Blue'},
    {'state_number': 'EFG456', 'brand': 'Ford', 'model': 'Mustang', 'color': 'Red'},
    {'state_number': 'HIJ789', 'brand': 'Chevrolet', 'model': 'Cruze', 'color': 'Black'},
    {'state_number': 'KLM012', 'brand': 'Audi', 'model': '6', 'color': 'Grey'},
    {'state_number': 'NOP345', 'brand': 'Nissan', 'model': 'Altima', 'color': 'Yellow'},
    {'state_number': 'QRS678', 'brand': 'Chevrolet', 'model': 'Cruze', 'color': 'Green'},

]

cars = []
for car_info in cars_data:
    car = Car.objects.create(**car_info)
    cars.append(car)

# Назначаем каждому автовладельцу удостоверение и от 1 до 3 автомобилей
for owner in owners:
    # Создаем удостоверение
    license_info = {'id_owner': owner, 'id_number': '1234567890', 'type': 'Category B', 'date_issue': datetime.now()}
    driver_license = DriverLicense.objects.create(**license_info)

    # Назначаем случайное количество автомобилей владельцу (от 1 до 3)
    cars_for_owner = random.sample(cars, random.randint(1, 3))

    # Создаем записи в ассоциативной сущности "владение"
    for car in cars_for_owner:
        possession_info = {'id_owner': owner, 'id_car': car, 'date_start': datetime.now()}
        Possession.objects.create(**possession_info)
