from datetime import datetime
import functools


def logger(old_function):
    @functools.wraps(old_function)
    def new_function(*args, **kwargs):
        call = datetime.now().strftime("%H:%M %d-%m-%Y")
        print(call)
        f_name = old_function.__name__
        result = old_function(*args, **kwargs)
        with open("task3.log", "a", encoding="UTF-8") as log_file:
            print(f"Время вызова функции: {call}", f"Имя функции: {f_name}",
                  f"Аргументы функции: {args, kwargs}",
                  f"Возвращаемое значение функции: {result}", sep="\n", end="\n"+"*" * 10 + "\n", file=log_file)
        return result
    return new_function


@logger
def flat_generator(list_of_lists):
    a = [element for innerList in list_of_lists for element in innerList]
    yield from a


if __name__ == "__main__":
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    flat_generator(list_of_lists_1)
