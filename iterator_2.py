class FlatIterator:
    """
    Класс FlatIterator вызывает итератор, который принимает
    список списков с любым уровнем вложенности и возвращает
    их плоское представление
    """

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.flat_list = []
        self.flat_iterator = iter(self.list_of_list)
        return self

    def __next__(self):

        while True:
            try:
                self.item = next(self.flat_iterator) #  получаем следующий элемент списка
            except StopIteration: # если следующего элемента нет, то получаем исключение
                if not self.flat_list: # если элементов больше нет, возвращаем исключение
                    raise  StopIteration
                else:
                    self.flat_iterator = self.flat_list.pop()
                    continue
            if type(self.item) == list: # проверка типа элемента списка
                self.flat_list.append(self.flat_iterator)  # если тип элемента - список, то добавляем в очередь итератора
                self.flat_iterator = iter(self.item)  # и смещаем указатель текущего итератора
            else:  # если элемент не является списком, то возвращаем этот элемент
                return self.item



def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    print(list(FlatIterator(list_of_lists_2)))

if __name__ == '__main__':
    test_3()