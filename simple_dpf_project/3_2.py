# create_data.py
import random
from datetime import datetime
from random import sample
from project_first_app.models import CarOwner, DriverLicense, Car, Possession

# Создаем 6-7 новых автовладельцев
owners_data = [
    {'surname': 'Иванов', 'name': 'Иван', 'date_birth': datetime(1990, 1, 1)},
    {'surname': 'Петров', 'name': 'Петр', 'date_birth': datetime(1985, 5, 15)},
    {'surname': 'Сидоров', 'name': 'Алексей', 'date_birth': datetime(1988, 3, 10)},
    # Добавьте остальных владельцев аналогичным образом
]

owners = []
for owner_info in owners_data:
    owner = CarOwner.objects.create(**owner_info)
    owners.append(owner)

# Создаем 5-6 автомобилей
cars_data = [
    {'state_number': 'ABC123', 'brand': 'Toyota', 'model': 'Camry', 'color': 'Blue'},
    {'state_number': 'XYZ789', 'brand': 'Honda', 'model': 'Civic', 'color': 'Red'},
    {'state_number': '123XYZ', 'brand': 'Ford', 'model': 'Focus', 'color': 'Black'},
    # Добавьте остальные автомобили аналогичным образом
]

cars = []
for car_info in cars_data:
    car = Car.objects.create(**car_info)
    cars.append(car)

# Назначаем каждому автовладельцу удостоверение и от 1 до 3 автомобилей
for owner in owners:
    # Создаем удостоверение
    license_info = {'id_owner': owner, 'license_number': '1234567890', 'license_type': 'Category B',
                    'date_issue': datetime.now()}
    driver_license = DriverLicense.objects.create(**license_info)

    # Назначаем случайное количество автомобилей владельцу (от 1 до 3)
    cars_for_owner = sample(cars, random.randint(1, 3))

    # Создаем записи в ассоциативной сущности "владение"
    for car in cars_for_owner:
        possession_info = {'id_owner': owner, 'id_car': car, 'date_start': datetime.now()}
        Possession.objects.create(**possession_info)

# Теперь приступим к выполнению запросов

# 1. Вывести все машины марки "Toyota"
toyota_cars = Car.objects.filter(brand='Toyota')
print("Машины марки Toyota:", toyota_cars)

# 2. Найти всех водителей с именем "Олег"
oleg_drivers = CarOwner.objects.filter(name='Олег')
print("Водители с именем Олег:", oleg_drivers)

# 3. Взяв любого случайного владельца, получить его ID и по этому ID получить экземпляр удостоверения
random_owner = CarOwner.objects.order_by('?').first()
owner_id = random_owner.id_owner
driver_license = DriverLicense.objects.get(id_owner=owner_id)
print("Удостоверение владельца с ID", owner_id, ":", driver_license)

# 4. Вывести всех владельцев красных машин
red_car_owners = CarOwner.objects.filter(possession__id_car__color='Red')
print("Владельцы красных машин:", red_car_owners)

# 5. Найти всех владельцев, чей год владения машиной начинается с 2010
owners_2010 = CarOwner.objects.filter(possession__date_start__year=2010)
print("Владельцы с годом владения начиная с 2010:", owners_2010)
