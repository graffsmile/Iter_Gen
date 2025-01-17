import types


def flat_generator(list_of_list):
    """
    Функция flat_generator создает генератор, который
    принимает список списков с любым уровнем вложенности
    и возвращает их плоское представление
    """
    for item in list_of_list: # проверяем каждый элемент списка
        if type(item) == list: # если тип элемента - список, то рекурсивно запускаем генератор по вложенному списку
            yield from flat_generator(item)
        else: # или возвращаем элемент списка
            yield item

def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)

    print(list(flat_generator(list_of_lists_2)))

if __name__ == '__main__':
    test_4()
