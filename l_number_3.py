from random import randint
import time


"""
Вопрос №3
На языке Python предложить алгоритм, который быстрее всего (по процессорным тикам) отсортирует данный ей массив 
чисел. Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). Объяснить, 
почему вы считаете, что функция соответствует заданным критериям."""

massive_list = [randint(0, 1_000_000) for _ in range(1_000_000)]


def fast_sort(arr: list) -> list:
    """"""
    """Время выполнения сортировки рекурсивным методом составляет -  4.80915 сек. на 1_000_000 итераций"""
    # if len(arr) <= 1:
    #     return arr
    # element = arr[0]
    # left_element = list(filter(lambda x: x < element, arr))
    # center_element = [i for i in arr if i == element]
    # right_element = list(filter(lambda x: x > element, arr))
    # return fast_sort(left_element) + center_element + fast_sort(right_element)
    """Время выполнения сортировки пузырьковым методом составляет -  5.0457 сек. на  10_000 итераций что очевидно 
    хуже"""
    # for x in range(len(arr) - 1):
    #     for y in range(len(arr) - x - 1):
    #         if arr[y] > arr[y + 1]:
    #             arr[y], arr[y + 1] = arr[y + 1], arr[y]
    # return arr
    """Время выполнения сортировки используя sorted(*args) составляет - 0.40109 сек. на 1_000_000 итераций что 
    является самым быстрым способом сортировки"""
    return sorted(arr, key=len)


"""
Исходя из проведенных мною экспериментов я на личном опыте выяснил что, для самой быстрой сортировки 
большого массива желательно использовать sorted(*args). 

Из дополнительных плюсов такого метода сортировки это возможность указать 
необязательный параметр key для сортировки по какому-либо критерию или результату выполнения функции lambda/def func.

Я не знаю более быстрого способа (возможно это связанно с небольшим опытом). 

"""

start_operation = time.time()
fast_sort(massive_list)
print(f"{round(float(time.time() - start_operation), 5):*^20}")
