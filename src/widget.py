from datetime import datetime

from src.mask import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account: str) -> str:
    """Маскирует номер карты или банковского счёта вместе с названием."""

    name, number = card_or_account.rsplit(" ", 1)

    if name == "Счет":
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{name} {masked_number}"


def get_date(date_string: str) -> str:
    """Преобразует дату из ISO-формата в формат ДД.ММ.ГГГГ."""

    date = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f")
    return date.strftime("%d.%m.%Y")