import my_select
from pprint import pprint


COMMANDS = {
    "1": my_select.select_1(),
    "2": my_select.select_2(),
    "3": my_select.select_3(),
    "4": my_select.select_4(),
    "5": my_select.select_5(),
    "6": my_select.select_6(),
    "7": my_select.select_7(),
    "8": my_select.select_8(),
    "9": my_select.select_9(),
    "10": my_select.select_10()
}

print(
    """
    1 - Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    2 - Знайти студента із найвищим середнім балом з певного предмета.
    3 - Знайти середній бал у групах з певного предмета.
    4 - Знайти середній бал на потоці (по всій таблиці оцінок).
    5 - Знайти які курси читає певний викладач.
    6 - Знайти список студентів у певній групі.
    7 - Знайти оцінки студентів у окремій групі з певного предмета.
    8 - Знайти середній бал, який ставить певний викладач зі своїх предметів.
    9 - Знайти список курсів, які відвідує певний студент.
    10 - Список курсів, які певному студенту читає певний викладач.
    """
)

while True:
    user_input = input('Type the number (type "exit" for exit): ').strip()

    if user_input == 'exit':
        print('Bye!')
        break

    if user_input not in COMMANDS.keys():
        print('Please type number from 1 to 10.')
        continue
    
    result = COMMANDS[user_input]
    pprint(result)

    



