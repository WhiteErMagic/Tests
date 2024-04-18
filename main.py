from typing import List


def check_triangle(side1: int, side2: int, side3: int):
    if (side1 + side2 <= side3) or (side2 + side3 <= side1) or (side1 + side3 <= side2) or side1 <= 0 or side3 <= 0 or side2 <= 0: # условие, что треугольник существует
        result = "Треугольник не существует"
    elif side1 == side2 and side2 == side3: # условие, что треугольник равносторонний
        result = "Равносторонний треугольник"
    elif (side1 == side2) or (side2 == side3) or (side3 == side1):# условие, что треугольник равнобедренный
        result = "Равнобедренный треугольник"
    else: # во всех остальных случаях треугольник разносторонний
        result = "Разносторонний треугольник"
    return result


def longest_film(film_1: str, film_2: str,film_3: str) -> bool:
    if len(film_1) >= len(film_2) and len(film_1) >= len(film_3):
        return film_1
    elif len(film_2) >= len(film_1) and len(film_2) >= len(film_3):
        return film_2
    elif len(film_3) >= len(film_1) and len(film_3) >= len(film_2):
        return film_3


def fio(initials: List[str]) -> str:
    return initials[0][0]+initials[1][0]+initials[2][0]


if __name__ == '__main__':
    print('start')