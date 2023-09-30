import collections
import random

# ************************


def ex1():
    numbers = [2, 4, 14, 24, 124]
    n = int(input("Введите число\n"))

    if n in numbers:
        print("Поздравляю, Вы угадали число!")
    else:
        print("Нет такого числа!")

# ************************


def ex2():
    a = ""
    unordered_list = [1, 2, 3, 1]
    count = dict(collections.Counter(unordered_list))

    for i in count:
        if count[i] > 1:
            a = i
            print("Повторяющийся элемент ", a)

    if a == "":
        print("Повторяющихся элементов не найдено!")

# ************************


def ex3():
    week = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
    weekends = []
    working_days = []
    weekends_count = int(input("Сколько вы хотите выходных?\n"))
    i = len(week)

    while i > (len(week) - weekends_count):
        i -= 1
        weekends += [week[i]]

    while i > 0:
        i -= 1
        working_days += [week[i]]

    weekends.reverse()
    working_days.reverse()
    print("Ваши выходные дни: ", weekends)
    print("Ваши рабочие дни: ", working_days)

# ************************


def ex4():
    group_20 = ["Абадовский", "Аленик", "Бурдов", "Дубовец", "Дюбарев",
                "Лопухов", "Магдесян", "Машичев", "Фаттахов", "Шапран"]
    group_25 = ["Бадминов", "Бобков", "Выдровский", "Давлетов", "Денисенко",
                "Лащёв", "Ринчинов", "Сергеев", "Шакиров", "Шорников"]
    team = []
    j = 0

    rand_students(group_20, team)
    rand_students(group_25, team)
    print(group_20)
    print(group_25)
    print(team)
    print(len(team))
    team.sort()
    print(team)

    for i in team:
        if i == "Иванов":
            j += 1

    if j >= 1:
        print("В команде есть Иванов, ", j, "шт")
    else:
        print("В комнаде нет Ивановых")

# ************************


def rand_students(group, team):
    i = 0
    us_num = []

    while i < 5:
        stud_num = random.randint(0, 9)
        if str(stud_num) in us_num:
            continue
        else:
            us_num += str(stud_num)
            team += [group[stud_num]]
        i += 1

# ************************


ex4()
