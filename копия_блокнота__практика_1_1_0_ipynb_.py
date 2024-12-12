# -*- coding: utf-8 -*-
"""Копия блокнота "Практика 1.1.0.ipynb"

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1INjaArxTzf9yERlBzGK7KeCBVKpWsT5w

**ФИО:**
"""

print("Кучерявин Кирилл Владимирович")

"""# Задание 1

**Описание:** Создайте иерархию классов для разных типов сотрудников в компании. Реализуйте родительский класс Employee и дочерние классы Manager и Developer. Каждый класс должен иметь метод для расчета зарплаты на основе различных критериев класса.


Отрабатываемый принцип: Наследование
"""

class Employee:
    tax = 0.87
    prize = 1.25

    def __init__(self, salary):
        self.salary = salary

    def salary_itog(self):
        return f"Ваша зарпалата после вычета налогов, учитывая премию: {self.salary * self.prize * self.tax}"


class Manager(Employee):
    tax = 0.93
    prize = 1.15

    def __init__(self, salary):
        super().__init__(salary)

    def salary_itog(self):
        return f"Ваша зарпалата после вычета налогов, учитывая премию: {self.salary * self.prize * self.tax}"


class Developer(Employee):
    tax = 0.95
    prize = 1.99

    def __init__(self, salary):
        super().__init__(salary)

    def salary_itog(self):
        return f"Ваша зарпалата после вычета налогов, учитывая премию: {self.salary * self.prize * self.tax}"


employee = Employee(100000)
manager = Manager(80000)
developer = Developer(15000)

print(employee.salary_itog())
print(manager.salary_itog())
print(developer.salary_itog())

"""**Описание:** Создайте иерархию классов для различных типов транспортных средств (Необходим один родительский класс и 3 дочерних). Реализуйте метод, который позволяет каждому транспортному средству возвращать собственное описание (Метод в каждом классе должен иметь одинаковое название). Продемонстрируйте вызов данного метода для каждого транспортного средства.


Отрабатываемый принцип: Полиморфизм
"""

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe(self):
        return f"Это {self.year} {self.make} {self.model}."


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def describe(self):
        return f"Это {self.year} {self.make} {self.model} с {self.num_doors} дверями."


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_size):
        super().__init__(make, model, year)
        self.engine_size = engine_size

    def describe(self):
        return f"Это {self.year} {self.make} {self.model} с двигателем объёмом {self.engine_size} куб. см."


class Bicycle(Vehicle):
    def __init__(self, make, model, year, num_gears):
        super().__init__(make, model, year)
        self.num_gears = num_gears

    def describe(self):
        return f"Это {self.year} {self.make} {self.model} с {self.num_gears} передачами."




vehicles = [
    Car("Toyota", "Camry", 2023, 4),
    Motorcycle("Harley-Davidson", "Sportster", 2022, 1200),
    Bicycle("Giant", "Defy", 2024, 22),
]

for vehicle in vehicles:
    print(vehicle.describe())

"""# Задание 3

Онлайн-магазин:
- Создайте модель для онлайн-магазина с классами Product, Order, Customer, и ShoppingCart.
- Product включает информацию о цене, наличии на складе и категории товара.
Order обрабатывает процесс покупки, включая расчет цены с учетом скидок и налогов.
- Customer управляет информацией о пользователе и его истории заказов.
- ShoppingCart позволяет добавлять, удалять и обновлять количество товаров перед оформлением заказа.
"""

class Product:
    def __init__(self, price, how, name, category):
        self.price = price
        self.how = how
        self.name = name
        self.category = category

    def input(self):
        return f"В наличии имеется {self.name} ({self.category}) по цене {self.price} в количестве {self.how}."


class Order(Product):
    tax = 0.87
    discount = 0.10

    def __init__(self, price, how, name, category, how_many):
        super().__init__(price, how, name, category)
        self.how_many = how_many

        if how_many > how:
            print('На складе нет столько товара!')



class Customer:
    order_dict = {}

    def __init__(self, name):
        self.name = name
        self.orders = []
        self.total_price = 0

    def add_order(self, order):
        self.orders.append(order)
        self.total_price += order.price * order.how_many * order.tax * (1 - order.discount)
        self.order_dict[self.name] = len(self.orders)

    def summary(self):
        print(f"У пользователя {self.name} {len(self.orders)} покупок")
        return f"Сумма ваших покупок {self.total_price:.2f}"


class ShoppingCart:
    def __init__(self):
        self.cart_items = []

    def add_product(self, product, how_many):
        if product.how >= how_many:
            order = Order(product.price, product.how, product.name, product.category, how_many)
            self.cart_items.append(order)
            product.how -= how_many
            print(f"{how_many} шт. {product.name} добавлено в корзину.")
        else:
            print('Недостаточно товара на складе!')

    def update_product(self, product, how_many):
        for order in self.cart_items:
            if order.name == product.name:
                order.how_many += how_many
                product.how -= how_many
                print(f"Количество {product.name} обновлено до {order.how_many} шт.")
                return
        print('Товар не найден в корзине!')

    def display_cart(self):
        if self.cart_items:
            print("Ваши товары в корзине:")
            for order in self.cart_items:
                print(f"{order.name}: {order.how_many} шт. по цене {order.price:.2f}")
        else:
            print("Корзина пуста.")


product1 = Product(price=100, how=50, name="Книга", category="Литература")
product2 = Product(price=200, how=30, name="Ноутбук", category="Электроника")


print(product1.input())
print(product2.input())

cart = ShoppingCart()

cart.add_product(product1, 2)
cart.add_product(product2, 1)

cart.display_cart()

customer = Customer(name="Иван")

for order in cart.cart_items:
    customer.add_order(order)

print(customer.summary())

"""# Задание 4

Симулятор космического корабля:
- Создайте симулятор управления космическим кораблем с классами SpaceShip, CrewMember, и Mission.
- SpaceShip имеет атрибуты для управления топливом, состоянием корпуса, и текущей скоростью.
- CrewMember контролирует здоровье, навыки, и роли в команде (например, пилот, инженер).
- Mission определяет цели, ресурсы, и возможные события (например, аварии, встречи с астероидами).
"""

import random

class SpaceShip:
    def __init__(self, name, fuel, hull, speed=0):
        self.name = name
        self.fuel = fuel
        self.hull = hull
        self.speed = speed

    def accelerate(self, amount):
        fuel_used = min(self.fuel, amount)
        self.fuel -= fuel_used
        self.speed += fuel_used
        return fuel_used

    def decelerate(self, amount):
        self.speed = max(0, self.speed - amount)

    def damage(self, amount):
        self.hull = max(0, self.hull - amount)
        if self.hull == 0:
            print("Корпус поврежден!")

    def __str__(self):
        return f"{self.name}: соляра={self.fuel}, корпус={self.hull}, скорость={self.speed}"


class CrewMember:
    def __init__(self, name, role, health, skills):
        self.name = name
        self.role = role
        self.health = health
        self.skills = skills

    def damage(self, amount):
        self.health = max(0, self.health - amount)
        if self.health == 0:
            print(f"{self.name} хана типу")

    def __str__(self):
        return f"{self.name} ({self.role}): здоровье={self.health}, навыки={self.skills}"


class Mission:
    def __init__(self, objective, events):
        self.objective = objective
        self.events = events

    def run(self, spaceship, crew):
        print(f"Миссия „{self.objective}“ начинается...")
        for event in self.events:
            event(spaceship, crew)
        print("Миссия завершена.")


def asteroid_impact(spaceship, crew):
    damage = random.randint(10, 30)
    spaceship.damage(damage)
    print(f"Столкновение с астероидом! Повреждение корпуса: {damage}")

def engine_failure(spaceship, crew):
    spaceship.decelerate(spaceship.speed)
    print("Отказ двигателя! Остановлен.")


ship = SpaceShip("Выносливость", 100, 100)
crew = [CrewMember("иван", "капитан", 100, {"пилотирование": 90, "командование": 80}),
        CrewMember("каламбер", "инженер", 90, {"инженеринг": 95, "ремонт": 75})]

mission = Mission("Спасти рядового Райна", [asteroid_impact, engine_failure, asteroid_impact])
mission.run(ship, crew)
print(ship)
for member in crew:
    print(member)

"""# Дополнительно:

**Описание:** создайте консольную версию игры крестики-нолики, используя классы
"""

