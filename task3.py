import sys
from pathlib import Path
from colorama import init, Fore, Style

def print_tree(directory: Path, prefix: str = '') -> None:
    """
    Рекурсивна функція для виведення структури директорії.
    Директорії виводяться синім, файли – зеленим.
    """
    # Отримуємо всі елементи в директорії, спочатку директорії, потім файли (за алфавітом)
    items = sorted(directory.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))
    count = len(items)
    for i, item in enumerate(items):
        # Вибір символу для виводу: "┣" для проміжних елементів, "┗" для останнього
        connector = "┣ " if i < count - 1 else "┗ "
        if item.is_dir():
            # Виводимо назву директорії синім кольором
            print(prefix + connector + Fore.BLUE + item.name + Style.RESET_ALL)
            # Змінюємо префікс для наступного рівня вкладеності
            new_prefix = prefix + ("┃ " if i < count - 1 else "  ")
            # Рекурсивно виводимо вміст вкладеної директорії
            print_tree(item, new_prefix)
        else:
            # Виводимо назву файлу зеленим кольором
            print(prefix + connector + Fore.GREEN + item.name + Style.RESET_ALL)

def main() -> None:
    # Ініціалізація colorama
    init()

    # Перевірка наявності аргументу командного рядка
    if len(sys.argv) != 2:
        print("Використання: python task3.py /Users/halynalekhnovska/Documents/Study/Pyton/goit-pycore-hw-04")
        sys.exit(1)

    # Отримуємо шлях до директорії
    dir_path = Path(sys.argv[1])

    # Перевірка чи шлях існує та є директорією
    if not dir_path.exists():
        print("Помилка: Вказаний шлях не існує.")
        sys.exit(1)
    if not dir_path.is_dir():
        print("Помилка: Вказаний шлях не є директорією.")
        sys.exit(1)

    # Виводимо назву головної директорії з піктограмою "📦"
    print(Fore.BLUE + f"📦{dir_path.name}" + Style.RESET_ALL)
    # Рекурсивно виводимо всю структуру директорії
    print_tree(dir_path)

if __name__ == "__main__":
    main()
