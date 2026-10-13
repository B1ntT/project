def filter_by_state(data: list, state: str = 'EXECUTED') -> list:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param data: список словарей для фильтрации
    :param state: значение ключа 'state' для фильтрации (по умолчанию 'EXECUTED')
    :return: новый список словарей, у которых ключ 'state' равен заданному значению
    """
    return [item for item in data if item.get('state') == state]
def sort_by_date(data: list, reverse: bool = True) -> list:
    """
    Сортирует список словарей по значению ключа 'date'.

    :param data: список словарей для сортировки
    :param reverse: порядок сортировки. По умолчанию True — убывание (от новых к старым).
                    Если False — возрастание (от старых к новым).
    :return: новый отсортированный список словарей
    """
    return sorted(data, key=lambda item: item['date'], reverse=reverse)