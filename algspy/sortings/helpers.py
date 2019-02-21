from typing import List


def swap(array: List[int], i: int, j: int):
    array[i], array[j] = array[j], array[i]


def is_sorted(array: List[int]) -> bool:
    n = len(array)
    for i in range(n - 1):
        if array[i] > array[i + 1]:
            return False
    return True
