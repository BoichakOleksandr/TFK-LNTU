# Лабораторна робота №2
# Консольна міні-програма для перегляду оцінок

users = {
    "student1": {
        "password": "1111",
        "grades": [10, 8, 12, 7, 5, 3, 9, 11]
    },
    "student2": {
        "password": "2222",
        "grades": [6, 7, 4, 3, 10, 8, 12, 5]
    },
    "student3": {
        "password": "3333",
        "grades": [12, 11, 9, 8, 7, 10, 4, 2]
    },
    "student4": {
        "password": "4444",
        "grades": [5, 6, 3, 4, 8, 9, 10, 1]
    }
}


# Введення логіну та пароля
login = input("Введіть логін: ")
password = input("Введіть пароль: ")


# Перевірка користувача
if login in users and users[login]["password"] == password:

    grades = users[login]["grades"]

    print("\nВхід успішний!")
    print("Ваші оцінки:")

    # Виведення всіх оцінок
    for grade in grades:
        print(grade, end=" ")

    # Підрахунок оцінок
    satisfactory = 0
    unsatisfactory = 0

    for grade in grades:
        if 5 <= grade <= 12:
            satisfactory += 1
        elif 1 <= grade <= 4:
            unsatisfactory += 1

    print("\n\nКількість задовільних оцінок:", satisfactory)
    print("Кількість незадовільних оцінок:", unsatisfactory)

else:
    print("\nПомилка! Неправильний логін або пароль.")
