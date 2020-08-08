objs = []


def create_objects(name):
    objs.append(f"object[{name}]")


def print_objects():
    print("Все добавленные объекты")
    for obj in objs:
        print(obj, end=', ')



def foo(x):
    print(f'foo={x}')


def bar(a: int, b: int) -> int:
    """Функция суммирует 2 числа

    :param a: int
    :param b: int
    :rtype: int
    """
    return a + b


if __name__ == "__main__":
    print('Executed separately', __name__)
    if bar(2, 2) == 4:
        print('OK')
    else:
        print('Fail')
else:
    print("imported", __name__)


