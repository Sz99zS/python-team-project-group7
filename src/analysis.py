def calculate_total_profit(sales_data: list[dict]) -> float:
    """
    Підраховує загальний прибуток від усіх продажів.
    :param sales_data: Список словників з даними продажів.
    :return: Сума загального прибутку.
    """
    if not sales_data:
        return 0.0
    return sum(item["profit"] for item in sales_data)


def find_top_product(sales_data: list[dict]) -> str:
    """
    Знаходить найприбутковіший товар.
    :param sales_data: Список словників з даними продажів.
    :return: Назва найприбутковішого товару.
    """
    if not sales_data:
        return "Дані відсутні"

    # Шукаємо товар з максимальним прибутком
    top_item = max(sales_data, key=lambda x: x["profit"])
    return top_item["product"]