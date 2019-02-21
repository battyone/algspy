import random

from hypothesis import given
import hypothesis.strategies as st

from ..collections import LinkedListDeque


@given(st.lists(st.integers()))
def test_deque_size(array):
    deque = LinkedListDeque()
    for elem in array:
        if random.random() < 0.42:
            deque.add_first(elem)
        else:
            deque.add_last(elem)

    assert deque.size == len(array)

    while not deque.is_empty():
        if random.random() < 0.42:
            deque.remove_first()
        else:
            deque.remove_last()

    assert deque.size == 0
