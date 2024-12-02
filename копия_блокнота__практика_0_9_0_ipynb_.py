# -*- coding: utf-8 -*-
"""Копия блокнота "Практика 0.9.0.ipynb"

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mP8tJBYkSS3iYmfv_1gCNq9eRrONgTuL

ФИО
"""

Кучерявин Кирилл Владимирович

"""# Дисклеймер

В данной практике вам необходимо применить все ваши знания по темам:

- Функции
- Словари
- Списки
- Множества
- Условные конструкции
- Запросы

и все что было изучено на прошлых практических занятиях

В каждом задании кратко описаны функции, которые необходимо реализовать, детали реализации вы должны продумать самостоятельно

# Задание 0

Создайте функцию по нахождению уникальных элементов из двух списков



```
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
```
"""

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
c = []
for i in a:
    for k in b:
        c.append(i)
        c.append(k)

def one_element(n):
    my_set = set()
    for i in n:
        my_set.add(i)
    return(my_set)


print(*one_element(c))

"""# Задание 1

Симулятор виртуального питомца

Цель: создать виртуальный симулятор домашних животных, в котором пользователи смогут заводить питомцев и ухаживать за ними.

Требования:

- Функция для усыновления питомца (имя, тип, возраст).
- Функция для того, чтобы покормить питомца, поиграть с ним или уложить его спать.
- Функция для отображения состояния питомца (голод, радость, энергия).
"""

def adopt_pet():
    name = input("Введите имя питомца: ")
    type_pet = input("Введите тип питомца (например, собака, кошка): ")
    age = int(input("Введите возраст питомца (в годах): "))
    return {
        "name": name,
        "type": type_pet,
        "age": age,
        "hunger": 5,
        "happiness": 5,
        "energy": 5
    }


def feed_pet(pet):
    pet["hunger"] -= 1
    pet["happiness"] += 1
    pet["energy"] += 1
    print(f"{pet['name']} покормлен!")


def play_with_pet(pet):
    pet["happiness"] += 1
    pet["energy"] -= 1
    print(f"{pet['name']} поиграл!")


def put_pet_to_sleep(pet):
    pet["energy"] += 2
    print(f"{pet['name']} уснул!")


def display_pet_status(pet):
    print(f"Состояние питомца {pet['name']}:")


    print(f"Тип: {pet['type']}, Возраст: лет")
    print(f"Голод: {pet['hunger']}, Радость: {pet['happiness']}, Энергия: {pet['energy']}")


def main():
    pet = adopt_pet()

    while True:
        print("\nВыберите действие:")
        print("1. Покормить питомца")
        print("2. Поиграть с питомцем")
        print("3. Уложить питомца спать")
        print("4. Показать состояние питомца")
        print("5. Выйти")

        choice = input("Ваш выбор: ")

        if choice == "1":
            feed_pet(pet)
        elif choice == "2":
            play_with_pet(pet)
        elif choice == "3":
            put_pet_to_sleep(pet)
        elif choice == "4":
            display_pet_status(pet)
        elif choice == "5":
            print("Выход из программы...")
            break
        else:
            print("Некорректный выбор. Пожалуйста, попробуйте снова.")


main()

"""# Задание 2

Рыцарь и дракон

Цель: создать небольшую игру, в которой вам необходимо играть за рыцаря и сразиться с драконом

Требования:

- Создание персонажа (имя, информация о доспехах, оружии, урон, здоровье)
- Управление персонажем и мини сюжет
- Создание дракона (Имя, информация о здоровье и уроне)
- Боевая система (нанесение и получение урона, урон должен быть случайным в заданном диапазоне)
- Реализовать бой между драконом и рыцарем
"""

import random



def create_knight():
    name = input("Введите имя рыцаря: ")
    armor = input("Введите информацию о доспехах: ")
    weapon = input("Введите название оружия: ")
    damage = random.randint(5, 15)
    health = 100
    return {"name": name, "armor": armor, "weapon": weapon, "damage": damage, "health": health}



def create_dragon():
    name = "Дракон"
    health = 80
    damage = random.randint(10, 20)
    return {"name": name, "health": health, "damage": damage}


def battle(knight, dragon):
    print(f"{knight['name']} сражается с {dragon['name']}!")
    while knight["health"] > 0 and dragon["health"] > 0:

        knight_attack = random.randint(0, knight["damage"])
        dragon["health"] -= knight_attack


        print(f"{knight['name']} наносит удар и наносит урона драку.")
        print(f"Здоровье дракона: {dragon['health']}")


        if dragon["health"] <= 0:
            print(f"{dragon['name']} повержен! победил!")
            break

        dragon_attack = random.randint(0, dragon["damage"])
        knight["health"] -= dragon_attack
        print(f"{dragon['name']} наносит удар и наносит урона рыцарю.")
        print(f"Здоровье рыцаря: {knight['health']}")


        if knight["health"] <= 0:
            print(f"{knight['name']} пал в бою. победил!")
            break


def main():
    print("Добро пожаловать в игру 'Рыцарь и Дракон'!")
    knight = create_knight()
    dragon = create_dragon()

    print("\nПриготовьтесь к бою!")
    battle(knight, dragon)


main()

"""# Задание 3

Цель - создать менеджера команды Pokémon, который позволит пользователям:

- Добавлять покемонов в свою команду. (если такого покемона еще нет в команде)
- Удалять покемонов из их команды.
- Просматривать подробную информацию обо всех покемонах в команде.
- Находить покемона по имени.
- Устраивать тренировочный бой между двумя покемонами

Для данной задачи используйте: https://pokeapi.co/
"""

import requests

def get_pokemon_data(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Покемон с именем '{name}' не найден.")
        return None

def add_pokemon(team, name):
    if name not in team:
        data = get_pokemon_data(name)
        if data:
            team[name] = {
                'id': data['id'],
                'base_experience': data['base_experience'],
                'height': data['height'],
                'weight': data['weight']
            }
            print(f"Покемон '{name}' добавлен в команду.")
        else:
            print(f"Не удалось добавить покемона '{name}'.")
    else:
        print(f"Покемон '{name}' уже есть в команде.")

def remove_pokemon(team, name):
    if name in team:
        del team[name]
        print(f"Покемон '{name}' удален из команды.")
    else:
        print(f"Покемон '{name}' не найден в команде.")

def view_team(team):
    if team:
        for name, data in team.items():
            print(f"Имя: {name}, ID: {data['id']}, Опыт: {data['base_experience']}, Рост: {data['height']}, Вес: {data['weight']}")
    else:
        print("Команда пуста.")

def find_pokemon(team, name):
    if name in team:
        data = team[name]
        print(f"Покемон найден: Имя: {name}, ID: {data['id']}, Опыт: {data['base_experience']}, Рост: {data['height']}, Вес: {data['weight']}")
    else:
        print(f"Покемон '{name}' не найден в команде.")

def battle(pokemon1, pokemon2):
    if pokemon1['base_experience'] > pokemon2['base_experience']:
        print(f"{pokemon1['name']} выигрывает!" )
    elif pokemon1['base_experience'] < pokemon2['base_experience']:
        print(f"{pokemon2['name']} выигрывает!" )
    else:
        print("Ничья!")

def main():
    team = {}
    while True:
        print("1. Добавить покемона")
        print("2. Удалить покемона")
        print("3. Просмотреть команду")
        print("4. Найти покемона")
        print("5. Устроить тренировочный бой")
        print("6. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            name = input("Введите имя покемона для добавления: ")
            add_pokemon(team, name)
        elif choice == '2':
            name = input("Введите имя покемона для удаления: ")
            remove_pokemon(team, name)
        elif choice == '3':
            view_team(team)
        elif choice == '4':
            name = input("Введите имя покемона для поиска: ")
            find_pokemon(team, name)
        elif choice == '5':
            name1 = input("Введите имя первого покемона: ")
            name2 = input("Введите имя второго покемона: ")
            pokemon1 = team.get(name1)
            pokemon2 = team.get(name2)
            if pokemon1 and pokemon2:
                battle(pokemon1, pokemon2)
            else:
                print("Один или оба покемона не найдены в команде.")
        elif choice == '6':
            break
        else:
            print("Некорректный выбор. Пожалуйста, попробуйте снова.")

main()