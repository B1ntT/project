def filter_by_state(data: list, state: str = 'EXECUTED') -> list:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param data: список словарей для фильтрации
    :param state: значение ключа 'state' для фильтрации (по умолчанию 'EXECUTED')
    :return: новый список словарей, у которых ключ 'state' равен заданному значению
    """
    return [item for item in data if item.get('state') == state]
