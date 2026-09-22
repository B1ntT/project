from src.mask import get_mask_account, get_mask_card_number


def test_mask_card_function() -> None:
    """Тест для проверки маскирования карты."""
    card = "1234567812345678"
    result = get_mask_card_number(card)

    print(f"Исходная карта: {card}")
    print(f"Результат маски: {result}")


def test_mask_account_function() -> None:
    """Тест для проверки маскирования счета."""
    account = "73654108436587612345"
    result = get_mask_account(account)

    print(f"Исходный счет: {account}")
    print(f"Результат маски: {result}")


# Запуск проверок
if __name__ == "__main__":
    print("--- Тестирование функции маскирования карт ---")
    test_mask_card_function()

    print("\n--- Тестирование функции маскирования счетов ---")
    test_mask_account_function()
    print("\nВсе импорты и функции работают корректно")
