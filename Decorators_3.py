from datetime import datetime

def logger(old_function):
    
    def new_function(*args, **kwargs):

        result = old_function(*args, **kwargs)
        with open ('mylog.log', 'a', encoding ='utf-8') as file:
            data = [f'Время вызова функции: {datetime.now()}\n', f'Имя функции: {old_function.__name__}\n',
                    f'Аргументы функции: {args}, {kwargs}\n', f'Вернувшееся значение: {result}\n\n']
            file.writelines(data)

        return result

    return new_function


class FlatIterator:

    @logger
    def __init__(self, list_of_lists):
        self.flatten_list = [item for sublist in list_of_lists for item in sublist]
        self.number_of_elements = len(self.flatten_list)
                
    @logger
    def __iter__(self):
        self.counter = 0
        return self
    
    @logger
    def __next__(self):
        if self.counter >= self.number_of_elements:
            raise StopIteration
        item = self.flatten_list[self.counter]
        self.counter += 1
             
        return item


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


if __name__ == '__main__':
    
    my_test_list = [
        [],
        [1,2,3,'a'],
        []
    ]

    for i in FlatIterator(my_test_list):
        print(i, end =',')
     
    test_1()