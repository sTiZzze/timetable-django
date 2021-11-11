import datetime

def day():

    day = datetime.datetime.today().isoweekday()

    if day == 1:
        day = "Понедельник"
    elif day == 2:
        day = "Вторник"
    elif day == 3:
        day = "Среда"
    elif day == 4:
        day = "Четверг"
    elif day == 5:
        day = "Пятница"
    elif day == 6:
        day = "Суббота"
    elif day == 7:
        day = "Воскресенье"

    return day

print(day())