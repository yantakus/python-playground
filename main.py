import pyfiglet
from colorama import Fore, Style, init
from fractions import Fraction
import os

# Инициализация colorama
init(autoreset=True)

def clear_screen():
    """Очищает экран"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Печатает красивый баннер"""
    ascii_banner = pyfiglet.figlet_format("Python Tasks")
    print(Fore.CYAN + ascii_banner)

def power_sum():
    n = int(input("Введите целое число: "))
    result = n**2 + n**3 + n**4
    print(f"{Fore.GREEN}Результат: {result}")

def filter_positives():
    numbers = list(map(int, input("Введите числа через пробел: ").split()))
    result = []
    for num in numbers:
        if num < 0:
            break
        if num > 0:
            result.append(num)
    print(f"{Fore.GREEN}Положительные числа до первого отрицательного: {result}")

def approximate_fraction():
    x = 9.75
    frac = Fraction(x).limit_denominator()
    print(f"{Fore.GREEN}{x:.2f} ≈ {frac.numerator}/{frac.denominator}")

def format_time():
    total_minutes = int(input("Введите общее количество минут: "))
    days = total_minutes // (24 * 60)
    hours = (total_minutes % (24 * 60)) // 60
    minutes = total_minutes % 60
    print(f"{Fore.GREEN}Формат дней:часов:минут: {days}:{hours}:{minutes}")

def check_divisible_by_5():
    n = int(input("Введите целое число: "))
    if n % 5 == 0:
        print(f"{Fore.GREEN}Число делится на 5 без остатка.")
    else:
        print(f"{Fore.RED}Число не делится на 5 без остатка.")

def convert_distance():
    choice = input("Выберите конвертацию (1 - км в мили, 2 - мили в км): ")
    if choice == "1":
        km = float(input("Введите расстояние в километрах: "))
        miles = km * 0.621371
        print(f"{Fore.GREEN}{km} км = {miles:.2f} миль")
    elif choice == "2":
        miles = float(input("Введите расстояние в милях: "))
        km = miles / 0.621371
        print(f"{Fore.GREEN}{miles} миль = {km:.2f} км")
    else:
        print(f"{Fore.RED}Неверный выбор.")

def print_menu():
    border = f"{Fore.BLUE}" + "+" + "-"*40 + "+"
    print(border)
    print(f"{Fore.YELLOW}|{'МЕНЮ ВЫБОРА ЗАДАЧ'.center(40)}|")
    print(border)
    print(f"{Fore.CYAN}| 1 | Степенная сумма".ljust(41) + "|")
    print(f"{Fore.CYAN}| 2 | Фильтрация положительных чисел".ljust(41) + "|")
    print(f"{Fore.CYAN}| 3 | Дробь с округлением для 9.75".ljust(41) + "|")
    print(f"{Fore.CYAN}| 4 | Форматирование времени".ljust(41) + "|")
    print(f"{Fore.CYAN}| 5 | Проверка делимости на 5".ljust(41) + "|")
    print(f"{Fore.CYAN}| 6 | Конвертация расстояний".ljust(41) + "|")
    print(f"{Fore.CYAN}| 0 | Выход".ljust(41) + "|")
    print(border)

def main():
    clear_screen()
    print_banner()
    while True:
        print_menu()
        choice = input(f"{Fore.MAGENTA}Введите номер задачи: {Style.RESET_ALL}")
        
        if choice == "1":
            power_sum()
        elif choice == "2":
            filter_positives()
        elif choice == "3":
            approximate_fraction()
        elif choice == "4":
            format_time()
        elif choice == "5":
            check_divisible_by_5()
        elif choice == "6":
            convert_distance()
        elif choice == "0":
            print(f"{Fore.GREEN}Выход из программы. До свидания!")
            break
        else:
            print(f"{Fore.RED}Неверный ввод. Попробуйте снова.")
        
        input(f"\n{Fore.YELLOW}Нажмите Enter для продолжения...")
        clear_screen()
        print_banner()

if __name__ == "__main__":
    main()