def degree():
    num_degree = float(input("твое число:"))
    num2_degree = num_degree
    degree_degree = int(input("твоя степень:"))
    degree_degree = degree_degree - 1

    for x in range(degree_degree):
        num_degree = num_degree * num2_degree

    print(num_degree)


def plus():
    num_plus = float(input("твое число:"))
    plus_plus = float(input("добавок к нему:"))

    print(num_plus + plus_plus)


def minus():
    num_minus = float(input("твое число:"))
    minus_minus = float(input("отнимание от него:"))

    print(num_minus - minus_minus)


def divide():
    num_divide = float(input("твое число:"))
    divide_divide = float(input("деление на него:"))

    print(num_divide / divide_divide)


def multiply():
    num_multiply = float(input("твое число:"))
    multiply_multiply = float(input("умножение на него:"))

    print(num_multiply * multiply_multiply)


def nsk():
    num_pm = 2
    nums_nsk = []
    amount = 1
    amount_num_nsk = int(input("количество чисел в НСК:"))
    for x in range(amount_num_nsk):
        nums_nsk.append(int(input("твое %s число:" % amount)))
        amount += 1
        for x2 in range(nums_nsk[x] - 2):
            num_nsk = nums_nsk[x]
            num_nsk = num_nsk / num_pm
            if num_nsk % 1 == 0:
                print(num_pm)

            num_nsk = nums_nsk[x]
            num_pm += 1


kalkul = input("команда:")

if kalkul == "/degree" or kalkul == "/.^":
    degree()

if kalkul == "/plus" or kalkul == "/.+":
    plus()

if kalkul == "/minus" or kalkul == "/.-":
    minus()

if kalkul == "/multiply" or kalkul == "/.*":
    multiply()

if kalkul == "/divide" or kalkul == "/./":
    divide()

if kalkul == "/nsk":
    nsk()
