def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты.

    Принимает строку из 16 цифр.
    Возвращает строку в формате: XXXX XX** **** XXXX
    """
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета.

    Принимает строку (длиной не менее 4 символов).
    Возвращает строку в формате: **XXXX (только последние 4 цифры)
    """
    return f"**{account_number[-4:]}"
