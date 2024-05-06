import re
from typing import Callable

def generator_numbers(text: str):
    # Шукаємо дійсні числа у тексті через регулярний вираз
    pattern = r'\b\d+\.\d+\b'  # Формула пошуку дійсних чисел
    for match in re.finditer(pattern, text):
        yield float(match.group())  # Повертаємо знайдене число як генератор

def sum_profit(text: str, func: Callable):
    # Робота функції generator_numbers по отриманню генератора чисел
    numbers_generator = func(text)
    total_profit = sum(numbers_generator)  # Визначаєм суму чисел, знайдених у тексті
    return total_profit

# Як приклад використання
text = "Profit: 100.25, expenses: 50.75, revenue: 150.50"
total_profit = sum_profit(text, generator_numbers)
print("Total profit:", total_profit)
