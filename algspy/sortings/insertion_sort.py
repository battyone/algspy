from typing import List
from .helpers import swap


def insertion_sort(array: List[int]) -> None:
    n = len(array)
    for i in range(1, n):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            swap(array, j, j - 1)
            j -= 1
