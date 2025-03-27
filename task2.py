
def get_cats_info(path):
    cats = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines:
            cat_id, name, age = line.strip().split(',')
            cats.append({"id": cat_id, "name": name, "age": age})

        return cats

    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
        return []
    except ValueError:
        print("Помилка: некоректні дані у файлі.")
        return []
    except Exception as e:
        print(f"Невідома помилка: {e}")
        return []


if __name__ == "__main__":
    cats_info = get_cats_info("/Users/halynalekhnovska/Documents/Study/Pyton/goit-pycore-hw-04/cats_info.txt")
    print(cats_info)
