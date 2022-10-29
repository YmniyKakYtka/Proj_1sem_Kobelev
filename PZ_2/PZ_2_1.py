def operation(): #Возврат в начало при ошибке осуществлен с помощью функции
    try:
        main_line_leght = float(input("Введите длинну основного отрезка: "))  # Ввод значений
        secondary_line_leght = float(input("Введите длину второстепенного отрезка: "))

        if main_line_leght > secondary_line_leght:  #Условие, при котором основной отрезок должен быть больше второстепенного
            secondary_line_count = int(main_line_leght // secondary_line_leght)  #Деление нацело
            print(f"Кол-во второстепенных отрезков, находящихся внутри основного: {secondary_line_count}")
        else:
            print("Основный отрезок должнен быть БОЛЬШЕ второстепенного")
            operation() #Возврат в начало
    except ValueError: #При ошибке ValueError
        print("Неправильно введены данные")
        operation() #Возврат в начало

operation() #Запуск программы