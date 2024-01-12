
from django.db.models import Count, Max, Min
from project_first_app.models import CarOwner, DriverLicense, Car, Possession

# Вывод даты выдачи самого старшего водительского удостоверения
oldest_license_date = DriverLicense.objects.aggregate(oldest_date=Min('date_issue'))
print("Дата выдачи самого старшего водительского удостоверения:", oldest_license_date['oldest_date'])

# Укажем самую позднюю дату владения машиной, имеющую какую-то из существующих моделей в вашей базе
latest_possession_date = Possession.objects.aggregate(latest_date=Max('date_start'))
print("Самая поздняя дата владения машиной:", latest_possession_date['latest_date'])

# Выведим количество машин для каждого водителя
cars_per_owner = CarOwner.objects.annotate(num_cars=Count('possession__id_car')).values('id_owner', 'num_cars')
print("Количество машин для каждого водителя:", cars_per_owner)

# Подсчитаем количество машин каждой марки
cars_per_brand = Car.objects.values('brand').annotate(num_cars=Count('id_car'))
print("Количество машин каждой марки:", cars_per_brand)

# Отсортируем всех автовладельцев по дате выдачи удостоверения
sorted_owners = CarOwner.objects.order_by('driverlicense__date_issue').distinct()
print("Отсортированные автовладельцы по дате выдачи удостоверения:", sorted_owners)
