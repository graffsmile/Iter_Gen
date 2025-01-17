import types

"""
Функция flat_generator создает генератор, который 
принимает список списков и возвращает их плоское представление
"""

def flat_generator(list_of_lists):
    for list in list_of_lists:
        for item in list:
            yield item



def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

    print(list(flat_generator(list_of_lists_1)))

if __name__ == '__main__':
    test_2()