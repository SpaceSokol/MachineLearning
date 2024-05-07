
def get_date(input_date):
    input_date = input_date.split('-')

    input_year = int(input_date[0])   # год
    input_month = int(input_date[1])  # порядковый номер месяца
    input_day = int(input_date[2])    # число

    print(f'{input_day:02d}.{input_month:02d}.{input_year}')

    for i in range(3):
        new_day = input_day - 7

        if new_day > 0:
            date = (f'{new_day:02d}.{input_month:02d}.{input_year}')
            input_day = new_day
            print(date)
        else:  # (Если новый день == 0 или < 0) то переходим на прерыдущий месяц и/или год
            new_month = input_month - 1
            if new_month == 0:
                new_month = 12
            input_month = new_month
            if new_month > 7 and new_month % 2 == 0:  # то в этом месяце 31 день (август, октябрь, декабрь)
                if new_month == 0 or new_month == 12:  # то значит вернулись к прошлому году
                    new_year = input_year - 1
                    input_year = new_year
                    new_day = 31 - abs(new_day)
                    date = (f'{new_day:02d}.{new_month:02d}.{new_year}')
                    input_day = new_day
                    print(date)
                else:  # значит остались в этом году, но вернулись в прошлый месяц
                    new_day = 31 - abs(new_day)
                    date = (f'{new_day:02d}.{new_month:02d}.{input_year}')
                    input_day = new_day
                    print(date)
            elif new_month > 7 and new_month % 2 != 0:  # то в этом месяце 30 дней (сентябрь, ноябрь)
                new_day = 30 - abs(new_day)
                date = (f'{new_day:02d}.{new_month:02d}.{input_year}')
                input_day = new_day
                print(date)
            elif new_month < 8 and new_month % 2 == 0:  # то в этом месяце 30/29/28 дней (февраль, апрель, июнь)
                if new_month == 2:  # это февраль
                    # проверяем год на високоснсть
                    if input_year == 2000 or (input_year % 4 == 0 and input_year % 100 != 0) or (
                            input_year % 400 == 0):  # то это високосный год
                        new_day = 29 - abs(new_day)
                        date = (f'{new_day:02d}.{new_month:02d}.{input_year}')
                        input_day = new_day
                        print(date)
                    else:  # иначе невисокосный год
                        new_day = 28 - abs(new_day)
                        date = (f'{new_day:02d}.{new_month:02d}.{input_year}')
                        input_day = new_day
                        print(date)
                else:
                    new_day = 30 - abs(new_day)
                    date = (f'{new_day:02d}.{new_month:02d}.{input_year}')
                    input_day = new_day
                    print(date)
            elif new_month < 8 and new_month % 2 != 0:  # то в этом месяце 31 дней (январь, март, май, июль)
                new_day = 31 - abs(new_day)
                date = (f'{new_day:02d}.{new_month:02d}.{input_year}')
                input_day = new_day
                print(date)

input_date = input()
get_date(input_date)




