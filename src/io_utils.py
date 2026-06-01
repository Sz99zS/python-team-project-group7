def read_sales_data(path: str) -> list[dict]:
    """
    Зчитує дані про продажі з текстового файлу.
    :param path: Шлях до файлу з даними.
    :return: Список словників з інформацією про товари.
    """
    sales = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                parts = line.strip().split(",")
                if len(parts) == 2:
                    sales.append({
                        "product": parts[0].strip(),
                        "profit": float(parts[1].strip())
                    })
        return sales
    except FileNotFoundError:
        print(f"Помилка: Файл {path} не знайдено!")
        return []
    except ValueError:
        print("Помилка: Некоректний формат числових даних у файлі!")
        return []