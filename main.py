sys_dict = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
sys_dict_rev = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}


# Проверка корректности введенной системы счисления
def is_valid_num_sys(sys_number):
    try:
        sys_number = int(sys_number)
        if 2 <= sys_number <= 16:
            return sys_number
        else:
            print("Введите корректную систему счисления 2 - 16")
            sys_number = input()
            sys_number = is_valid_num_sys(sys_number)
            return sys_number

    except ValueError:
        print("Введите корректную систему счисления 2 - 16")
        sys_number = input()
        sys_number = is_valid_num_sys(sys_number)
        return sys_number


# Проверка правильности введенного числа
def is_valid_number(num, f_num_sys):
    for i in range(len(num)):
        if num[i].isdigit():
            if int(num[i]) > f_num_sys - 1:
                print("Число содержит символы, отсутствующие в выбранной системе счисления. Введите корректное "
                      "число:")
                num = input().upper()
                num = is_valid_number(num, f_num_sys)
                return str(num)
        else:
            if int(sys_dict.get(num[i], 100)) > f_num_sys - 1:
                print("Число содержит символы, отсутствующие в выбранной системе счисления. Введите корректное "
                      "число:")
                num = input().upper()
                num = is_valid_number(num, f_num_sys)
                return num
    return num


# Функция ковертации систем счисления
# Часть перевода в десятичную систему счисления
def converter(num, f_num_sys, t_num_sys):
    decimal_num = 0
    for i in range(1, len(num) + 1):
        if num[i - 1].isdigit():
            decimal_num += int(num[i - 1]) * pow(f_num_sys, len(num) - i)
        else:
            decimal_num += int(sys_dict.get(num[i - 1])) * pow(f_num_sys, len(num) - i)

    # Часть перевода в требуемую систему счисления
    final_num = ''
    while decimal_num != 0:
        remains = decimal_num % t_num_sys
        if remains > 9:
            final_num += str(sys_dict_rev.get(remains))
        else:
            final_num += str(remains)
        decimal_num = decimal_num // t_num_sys
    return final_num[::-1]


# Главная программа
print("Введите систему счиcления ИЗ которой необходимо перевести: 2 - 16 ")
from_num_sys = input()
from_num_sys = is_valid_num_sys(from_num_sys)
print("Введите число, которое необходимо преобразовать:")
number = input().upper()
number = is_valid_number(number, from_num_sys)
print("Ввдите систему счисления В которую необходимо перевести: 2 - 16")
to_num_sys = input()
to_num_sys = is_valid_num_sys(to_num_sys)
print(converter(number, from_num_sys, to_num_sys))
