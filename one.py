def caching_fibonacci():
    cache = {}  # Створимо порожній словник для кешування результатів

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:  # Для перевірки чи є вже результат у кеші
            return cache[n]
        else:
            # Рекурсивно обчислюємо числа Фібоначчі
            result = fibonacci(n - 1) + fibonacci(n - 2)
            cache[n] = result  # Для збереження результату у кеші
            return result

    return fibonacci  # Повертаємо внутрішню функцію
