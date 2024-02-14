def get_birthdate():
    """
    Функция запрашивает у пользователя дату рождения в формате ДД.ММ.ГГГГ и возвращает ее.
    """
    birthdate = input("Введите вашу дату рождения в формате ДД.ММ.ГГГГ: ")
    return birthdate


def get_date():
    """
    Функция запрашивает у пользователя текущую дату в формате ДД.ММ.ГГГГ и возвращает ее.
    """
    date = input("Введите сегодняшнюю дату в формате ДД.ММ.ГГГГ: ")
    return date


def calculate_days_until_birthday(birthdate, date):
    """
    Функция принимает дату рождения и текущую дату, разбивает их на день, месяц и год, 
    подсчитывает оставшиеся дни до дня рождения и возвращает количество дней.
    """
    day, month, year = map(int, birthdate.split('.'))
    current_day, current_month, current_year = map(int, date.split('.'))
    if (current_month, current_day) == (month, day):
        days_until_birthday = 0
    elif (current_month, current_day) > (month, day):
        days_until_birthday = (365 - (current_month * 30 + current_day) + (month * 30 + day))
    else:
        days_until_birthday = (month * 30 + day) - (current_month * 30 + current_day)
    return days_until_birthday


def print_days_until_birthday(days_until_birthday):
    """
    Функция принимает количество оставшихся дней до дня рождения и выводит его на экран.
    """
    print("До вашего дня рождения осталось дней:", days_until_birthday,)


def get_zodiac_sign(birthdate):
    """
    Функция принимает дату рождения, определяет знак зодиака по дате рождения и возвращает его.
    """
    day, month, year = map(int, birthdate.split('.'))
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        zodiac_sign = "Овен"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        zodiac_sign = "Телец"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        zodiac_sign = "Близнецы"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        zodiac_sign = "Рак"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        zodiac_sign = "Лев"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        zodiac_sign = "Дева"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        zodiac_sign = "Весы"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        zodiac_sign = "Скорпион"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        zodiac_sign = "Стрелец"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        zodiac_sign = "Козерог"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        zodiac_sign = "Водолей"
    else:
        zodiac_sign = "Рыбы"
    return zodiac_sign


def print_zodiac_sign(zodiac_sign):
    """
    Функция принимает знак зодиака и выводит его на экран.
    """
    print("По гороскопу вы -", zodiac_sign)


def main():
    """
    Основная функция, которая вызывает все остальные функции и выводит результаты на экран.
    """
    birthdate = get_birthdate()
    date = get_date()
    days_until_birthday = calculate_days_until_birthday(birthdate, date)
    print_days_until_birthday(days_until_birthday)
    zodiac_sign = get_zodiac_sign(birthdate)
    print_zodiac_sign(zodiac_sign)


if __name__ == '__main__':
    main()