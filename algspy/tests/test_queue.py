from hypothesis import given
import hypothesis.strategies as st

from ..collections import LinkedListQueue


@given(st.lists(st.integers()))
def test_stack_size(array):
    queue = LinkedListQueue()
    for elem in array:
        queue.enqueue(elem)

    assert queue.size == len(array)

    while not queue.is_empty():
        queue.dequeue()

    assert queue.size == 0


@given(st.lists(st.integers()))
def test_ordering_in_queue(array):
    queue = LinkedListQueue()
    for elem in array:
        queue.enqueue(elem)

    popped = []
    while not queue.is_empty():
        popped.append(queue.dequeue())

    assert popped == array
