import pathlib

def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        total = 0
        count = 0

        for line in lines:
            name, salary = line.strip().split(',')
            total += float(salary)
            count += 1

        if count == 0:
            return 0, 0  # якщо файл порожній

        average = total / count

        return total, average

    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
        return 0, 0
    except ValueError:
        print("Помилка: некоректні дані у файлі.")
        return 0, 0
    except Exception as e:
        print(f"Невідома помилка: {e}")
        return 0, 0
# Приклад використання функції:
if __name__ == "__main__":
    total, average = total_salary("/Users/halynalekhnovska/Documents/Study/Pyton/goit-pycore-hw-04/salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")