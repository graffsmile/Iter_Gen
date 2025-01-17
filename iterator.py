class FlatIterator:
    """
    Класс FlatIterator вызывает итератор, который принимает
    список списков и возвращает их плоское представление
    """
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.flat_list = []
        self.cursor = -1
        self.flat_iterator = iter(self.list_of_list)
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.flat_list):
            self.flat_list = next(self.flat_iterator)
            self.cursor = 0

        return self.flat_list[self.cursor]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    print(list(FlatIterator(list_of_lists_1)))

if __name__ == '__main__':
    test_1()