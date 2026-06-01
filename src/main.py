from io_utils import read_sales_data
from analysis import calculate_total_profit, find_top_product


def main():
    print("--- Системний аналітик продажів (Група 7) ---")
    data_path = "data/input.txt"

    sales = read_sales_data(data_path)

    if not sales:
        print("Неможливо провести аналіз. Перевірте вхідні дані.")
        return

    total_profit = calculate_total_profit(sales)
    top_product = find_top_product(sales)

    print(f"\nЗагальний прибуток компанії: {total_profit:.2f} грн")
    print(f"Найприбутковіший товар сезону: {top_product}")


if __name__ == "__main__":
    main()