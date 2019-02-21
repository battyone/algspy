from typing import List


def merge_sort(array: List[int]) -> None:
    aux = array.copy()
    _sort(array, aux, 0, len(array) - 1)


def _sort(array: List[int], aux: List[int], lo: int, hi: int) -> None:
    if hi <= lo:
        return

    # Divide ...
    mid = (lo + hi) // 2
    _sort(array, aux, lo, mid)
    _sort(array, aux, mid + 1, hi)
    # ... and conquer
    _merge(array, aux, lo, mid, hi)


def _merge(array: List[int], aux: List[int], lo: int, mid: int, hi: int) -> None:
    for k in range(lo, hi + 1):
        aux[k] = array[k]

    i = lo
    j = mid + 1

    for k in range(lo, hi + 1):
        if i > mid:
            array[k] = aux[j]
            j += 1
        elif j > hi:
            array[k] = aux[i]
            i += 1
        elif aux[i] <= aux[j]:
            array[k] = aux[i]
            i += 1
        else:
            array[k] = aux[j]
            j += 1
