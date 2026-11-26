from typing import Any


def mean(data: tuple) -> float:
    return sum(data) / len(data)

def median(data: tuple) -> float:
    data = sorted(data)
    n = len(data)
    middle = n // 2

    if n % 2 == 0:
        return (data[middle - 1] + data[middle]) / 2
    else:
        return data[middle]

def quartile(data: tuple) -> tuple:
    data = sorted(data)
    n = len(data)

    return [data[int((n-1)/4)], data[int((3*n-1)/4)]]

def std(data: tuple) -> float:
    return var(data) ** 0.5

def var(data: tuple) -> float:
    m = mean(data)
    amount = 0
    
    for x in data:
        amount += (x - m) ** 2
    return amount / len(data)

def ft_statistics(*args: Any, **kwargs: Any) -> None:
    ""

    for value in kwargs.items():
        try:
            match value[1]:
                case "mean":
                    print("mean :", mean(args))
                case "median":
                    print("median :", median(args))
                case "quartile":
                    print("quartile :", quartile(args))
                case "std":
                    print("std :", std(args))
                case "var":
                    print("var :", var(args))
                case _:
                    pass
        except (IndexError, ZeroDivisionError) as e:
            print("ERROR")



