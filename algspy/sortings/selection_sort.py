from typing import List
from .helpers import swap


def selection_sort(array: List[int]) -> None:
    n = len(array)
    for i in range(n):
        for j in range(i + 1, n):
            if array[i] > array[j]:
                swap(array, i, j)
