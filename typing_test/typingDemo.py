from typing import List, Union, Optional, Callable


def process_data(data: List[Union[int, str]]) -> Optional[List[str]]:
    processed_data = []
    for item in data:
        if isinstance(item, int):
            processed_data.append(str(item))
        elif isinstance(item, str):
            processed_data.append(item.upper())
    return processed_data


def greet(name: str) -> None:
    print("Hello, " + name)


def math_operation(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)


def plus(x, y):
    return x + y


if __name__ == '__main__':
    process_data(list())
    # greet('PyCharm')
    print(math_operation(plus, 3, 4))
